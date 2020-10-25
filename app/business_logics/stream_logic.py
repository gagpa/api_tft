from ..business_modules import InfoDealer, Stream


class StreamLogic:
    """
    Класс отвечающий за взаимодействия со стримом.
    """

    def __init__(self, streamer_nickname: str):
        self.streamer_nickname = streamer_nickname

    def tft_stream_up(self, nickname):
        """
        Обозначить стрим заущен.
        """
        last_match_id = InfoDealer(nickname=nickname).get_last_match_id()
        Stream(nickname).tft_up(last_match_id)
        return {'successful': True}
