import asyncio
import aiohttp
from server_otvet import random_bool
async def checking_server_response():
    url = "https://ya.ru"
    time_out = 60
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, allow_redirects=True, timeout=time_out) as response:
                if response.status == 200 or response.status == 301:
                    return True
    except asyncio.TimeoutError:
        return False
    except aiohttp.ClientError:
        return False

# функция запроса r серверу с имитацией ответа:
async def requst_server(json):
    url =  "https://ya.ru"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json, timeout=60) as respons:
             response_text = await respons.text()
            #так как сервер вернет ошибку именно этот то с имитируем работу сервера заранее подготовленной функцией
            return {'status': random_bool()}
    except asyncio.TimeoutError:
        return {'status': 'Error'}
    except aiohttp.ClientError:
        return {'status': 'Error'}



