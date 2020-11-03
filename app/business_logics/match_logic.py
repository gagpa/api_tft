from app.business_modules import MatchesInfoDealer, UserInfoDealer
from app.business_modules.entitys import TftStreamEntity, TftUserHistoryEntity
from app.exceptions.db import DbRecordNotExist
from app.exceptions.tft import TftStreamNotUp
from collections import defaultdict


class MatchLogic:
    """
    Бизнес логика работы с инорфмацией матчей.
    """

    def get_stats_per_stream(self, nickname: str) -> dict:
        """
        Выдать информацию о матчах за стрим
        """
        user_dealer = UserInfoDealer(nickname)
        match_dealer = MatchesInfoDealer()
        stream = TftStreamEntity()
        user_history = TftUserHistoryEntity()

        puuid = user_dealer.get_puuid()  # TODO реализовать сохранение поьзователя.

        try:
            stream_rim = stream.stream_match_id(nickname)
        except DbRecordNotExist:
            raise TftStreamNotUp

        try:
            saved_rim = user_history.last_saved_match(nickname)
        except DbRecordNotExist:
            saved_rim = None

        stream_matches = match_dealer.matches_to_rim(puuid, stream_rim)

        if stream_matches:
            try:
                index_rim = stream_matches.index(saved_rim)
            except ValueError:
                index_rim = None

            for match_id in reversed(stream_matches[:index_rim]):
                placement = match_dealer.get_placement(puuid, match_id)
                user_history.save(nickname=nickname, placement=placement, match_id=match_id)
            placements = user_history.last_placements_to(nickname, stream_matches[-1])
            response = {
                'data': {
                    'tickerTitle': 'Счёт За Стрим',
                    'tickerData': placements,
                }
            }
        else:
            response = {
                'data': {
                    'tickerTitle': 'Счёт За Стрим',
                    'tickerData': 'Первая Игра!',
                }
            }
        return response

    def get_count_places(self, nickname: str) -> dict:
        """
        Выдать статистику занимаемых мест.
        """
        dealer = MatchesInfoDealer()
        user_dealer = UserInfoDealer(nickname)
        match_dealer = MatchesInfoDealer()
        user_history = TftUserHistoryEntity()

        puuid = user_dealer.get_puuid()

        try:
            last_saved_match = TftUserHistoryEntity().last_saved_match(nickname)
        except DbRecordNotExist:
            last_saved_match = None
        new_matches = dealer.matches_to_rim(puuid, last_saved_match)

        for match_id in reversed(new_matches):
            placement = match_dealer.get_placement(puuid, match_id)
            user_history.save(nickname=nickname, placement=placement, match_id=match_id)
        placements = user_history.all_placements(nickname)
        counter = defaultdict(int)
        for placement in placements:
            counter[placement] += 1

        content = \
            {
                'data': {'count_places': counter}
            }
        return content
