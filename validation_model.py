from pydantic import BaseModel, Field
from datetime import datetime

class IncomingRequest(BaseModel):
    number: str = Field(..., title="Кадастровый номер", pattern=r"\d{8}:\d{2}:\d{3}:\d{4}")
    latitude: str = Field(..., title="Широта")
    the_length: str = Field(..., title="Долгота")



class FeedBack(IncomingRequest):
    request_status: bool = Field(..., title="ответ от сервера")
    data_time: datetime




