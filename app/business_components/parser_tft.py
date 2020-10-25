class ParserTFT:
    """
    Парсер всей информации по ТФТ.
    """

    def find_personal_stat(self, puuid: str, match_info: dict) -> dict:
        """
        Найти личную статистику в json матча
        """
        players_stat = match_info['info']['participants']
        for player_stat in players_stat:
            if player_stat['puuid'] == puuid:
                personal_stat = player_stat
                return personal_stat

        raise ModuleNotFoundError

    def find_puuid(self, user_info: dict) -> str:
        """
        Найти puuid в json пользователя.
        """
        puuid = user_info['puuid']
        return puuid
