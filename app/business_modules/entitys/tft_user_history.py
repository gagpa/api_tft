from app.business_components.facades import FacadeStreamTft
from app.business_components.models import TftUserHistoryModel
from .base_entity import BaseEntity


class TftUserHistoryEntity(BaseEntity):
    """
    Класс сущности информации
    """

    def __init__(self):
        self.__model_facade = FacadeStreamTft()

    def last_placements_to(self, nickname: str, rim_match_id: str) -> list:
        """
        Вернуть список матчей от rim_match.
        """
        self.__model_facade.init_model(TftUserHistoryModel)
        placements = self.__model_facade.placements_to(nickname=nickname, match_id=rim_match_id)
        return placements

    def last_saved_match(self, nickname: str):
        """
        Вернуть последний сохраннёный матч id.
        """
        self.__model_facade.init_model(TftUserHistoryModel)
        stream_match_id = self.__model_facade.last_match_id(nickname=nickname)
        return stream_match_id

    def all_placements(self, nickname: str) -> list:
        """
        Вернуть все занимаемые места.
        """
        self.__model_facade.init_model(TftUserHistoryModel)
        placements = self.__model_facade.placements(nickname=nickname)
        return placements

    def save(self, **kwargs):
        """
        Сохранить запись
        """
        self.__model_facade.init_model(TftUserHistoryModel)
        self.__model_facade.set(**kwargs)
