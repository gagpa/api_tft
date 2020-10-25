from ..business_components import ModelFacade
from ..business_components.models import StreamTFTModel
from datetime import datetime


class Stream:

    def __init__(self, nickname: str):
        self.nickname = nickname
        self.model_facade = ModelFacade()

    def tft_up(self, match_id):
        """
        Включить отсчёт стрима по ТФТ.
        """
        self.model_facade.init_model(StreamTFTModel())
        self.model_facade.set(nickname=self.nickname, match_id=match_id, datetime=datetime.now())
