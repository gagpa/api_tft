from ..business_modules import InfoDealer


class MatchLogic:
    """
    Бизнес логика работы с инорфмацией матчей.
    """

    def get_stats_per_stream(self, nickname):
        """
        Выдать информацию о матчах за стрим
        """
        dealer = InfoDealer(nickname)
        personal_stats = dealer.get_personal_stat_per_stream()
        placements = [stat['placement'] for stat in personal_stats]
        response = {
            'data': {
                'tickerTitle': 'Матчей за стрим',
                'tickerData': placements,
            }
        }
        return response
