from datetime import datetime
from app.business_components.facades import FacadeStreamTft
from app.business_components.models import TftStreamModel
from .base_entity import BaseEntity


class TftStreamEntity(BaseEntity):
    """
    Класс сущности стрима по ТФТ
    """

    def __init__(self):
        self.__model_facade = FacadeStreamTft()

    def up(self, nickname: str, start_match_id: str):
        """
        Включить отсчёт стрима по ТФТ.
        """
        self.__model_facade.init_model(TftStreamModel)
        self.__model_facade.set(nickname=nickname,
                                match_id=start_match_id,
                                start_datetime=datetime.utcnow(),
                                )

    def stream_match_id(self, nickname):
        """
        Вернуть матч id  с короторого идёт отсчёт стрима.
        """
        self.__model_facade.init_model(TftStreamModel)
        match_id = self.__model_facade.last_match_id(nickname)
        return match_id
