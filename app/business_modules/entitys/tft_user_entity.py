from .base_entity import BaseEntity
from app.business_components.facades import FacadeModel
from app.business_components.models import TftUserModel


class TftUserEntity(BaseEntity):

    def __init__(self):
        self.__model_facade = FacadeModel()

    def save(self, **kwargs):
        """
        Сохранить запись
        """
        self.__model_facade.init_model(TftUserModel)
        self.__model_facade.set(**kwargs)
