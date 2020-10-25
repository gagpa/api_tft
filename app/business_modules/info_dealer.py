from ..business_components import Requester, ParserTFT, ModelFacade, ModelFacadeStreamTFT
from ..business_components.models import StreamTFTModel


class InfoDealer:
    """
    Класс для получения и обработки данных матча.
    """

    def __init__(self, nickname: str):
        self.nickname = nickname
        self.requester = Requester()

    def get_personal_stat_per_stream(self):
        """
        Выдать информации о матчах.
        """
        personal_stats = []
        parser = ParserTFT()

        user_info = self.requester.get_user_info(nickname=self.nickname)
        puuid = parser.find_puuid(user_info)
        count = self.get_count_matches_per_stream(puuid)

        matches_id = self.requester.get_matches_id(puuid=puuid, count=count)

        for match_id in matches_id:
            match_info = self.requester.get_match_info(match_id)
            personal_stat = parser.find_personal_stat(puuid, match_info)
            personal_stats.append(personal_stat)
        return personal_stats

    def get_count_matches_per_stream(self, puuid):
        count = 0
        matches_id = self.requester.get_matches_id(puuid=puuid, count=40)
        model = ModelFacadeStreamTFT(StreamTFTModel)
        stream_match_id = model.last_match_id
        for match in matches_id:
            if stream_match_id != match:
                count += 1
            else:
                break
        return count

    def get_last_match_id(self):
        """
        Получить последний матч id
        """
        parser = ParserTFT()
        user_info = self.requester.get_user_info(self.nickname)
        puuid = parser.find_puuid(user_info)
        match_id = self.requester.get_matches_id(puuid, count=1)[0]
        return match_id
