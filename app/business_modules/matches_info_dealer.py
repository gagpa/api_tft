from ..business_components import Requester, ParserTFT


class MatchesInfoDealer:
    """
    Класс для получения и обработки данных матча.
    """

    def __init__(self):
        self.requester = Requester()
        self.parser = ParserTFT()

    def matches_to_rim(self, puuid: str, rim_id: str) -> list:
        """
        Получить все id матчей до границы.
        """
        matches_id = self.__get_matches_id(puuid)

        if rim_id:
            index_rim = matches_id.index(rim_id)
        else:
            index_rim = -1
        return matches_id[:index_rim]

    def get_last_match_id(self, puuid: str) -> str:
        """
        Получить id последнего матча.
        """
        match_id = self.__get_matches_id(puuid, count=1)[0]
        return match_id

    def __get_matches_id(self, puuid: str, count: int = 10000) -> list:
        """
        Получить id матчей.
        count - количество запрашиваемых матчей.
        Если не передать count, то будут возвращены все id матчей.
        """
        matches_id = self.requester.get_matches_id(puuid, count=count)
        return matches_id

    def get_placement(self, puuid: str, match_id: str) -> int:
        """
        Получить занятое место по id матча от RiotApi.
        """
        match_info = self.requester.get_match_info(match_id)
        placement = self.parser.find_personal_stat(puuid, match_info)['placement']
        return placement
