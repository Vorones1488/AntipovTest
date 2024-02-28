from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from src.function.function import checking_server_response, requst_server
from src.cadastr import shema as vm
from src.cadastr.model import CadastralNumbers
from typing import List
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from sqladmin import Admin
from src.admin.admin import CadastrAdmin
from src.database import get_asinc_sesiion, engin

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler("../app.log", encoding="utf-8", maxBytes=100000, backupCount=1)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



app = FastAPI()
admin = Admin(app, engin)
admin.add_view(CadastrAdmin)




@app.on_event('startup')
async def startup():
    await get_asinc_sesiion()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.post("/ping", response_class=JSONResponse)
async def ping_server():
    logger.info('отработал запрос ping')
    if await checking_server_response():
        value = "доступен"
    else:
        value = "недоступен"
    return JSONResponse({"staus": value})


@app.post("/query", response_class=RedirectResponse)
async def query(item: vm.IncomingRequest):
    logger.info('отработал запрос query')
    query_server = item.dict()
    respons_server = await requst_server(query_server)
    if respons_server['status'] == 'error':
        logger.error('сервер не отвечает')
        return JSONResponse({'status': 'сервер не отвечает попробуйте позднее'})
    else:
        logger.info('отработал запрос к базе данных')
        query_bd = CadastralNumbers.__table__.insert().values(**item.dict(), request_status=respons_server['status'],
                                                              data_time=datetime.now())
        await database.execute(query_bd)
        return RedirectResponse('/result', status_code=200)

@app.get('/result', response_model=vm.FeedBack)
async def result():
    logger.info('отработал запрос result')
    last_bd = CadastralNumbers.__table__.select().order_by(CadastralNumbers.__table__.c.id.desc()).limit(1)
    return await database.fetch_one(last_bd)


@app.get('/history', response_model=List[vm.FeedBack])
async def history():
    logger.info('отработал запрос history')
    list_bd = CadastralNumbers.__table__.select()
    if list_bd is None:
        logger.error('записи не обнаружены')
        return RedirectResponse('/query')
    return await database.fetch_all(list_bd)


if __name__ == "__main__":
    app()