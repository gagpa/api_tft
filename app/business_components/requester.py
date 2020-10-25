import requests

from config.riot_api_urls import links_template


class Requester:
    """
    Класс запросов.
    Делает запросы на API riot и выдаёт информации от них.
    Не обрабатывает данные.
    """

    def get_matches_id(self, puuid, count: int) -> list:
        """
        Выдать id матчей.
        puuid -
        count - количество матчей
        """
        link_template = links_template['matches_id']
        link = link_template.substitute(puuid=puuid, count=count)

        response = requests.get(link)
        matches_id = response.json()
        return matches_id

    def get_user_info(self, nickname: str) -> dict:
        """
        Выдать инофрмацию о пользователе.
        nickname - пвсевдоним в игре
        """
        link_template = links_template['user_info']
        link = link_template.substitute(nickname=nickname)

        response = requests.get(link)
        user_info = response.json()
        return user_info

    def get_match_info(self, match_id) -> dict:
        """
        Выдать информацию о матче.
        match_id - id матча
        """
        link_template = links_template['match_info']
        link = link_template.substitute(match_id=match_id)

        response = requests.get(link)
        match_info = response.json()
        return match_info
