from sqladmin import ModelView
from ModelDB import CadastralNumbers

class CadastrAdmin(ModelView, model=CadastralNumbers):
    can_delete = False
    name = "Кадастровый номер"
    name_plural = "Кадастровые номера"
    icon = "fa-sharp fa-regular fa-folder-open"
    column_list = [
        CadastralNumbers.id,
        CadastralNumbers.number,
        # CadastralNumbers.latitude,
        # CadastralNumbers.the_length,
        CadastralNumbers.data_time
    ]