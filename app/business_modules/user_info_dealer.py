from app.business_components import ParserTFT, Requester


class UserInfoDealer:
    """
    Дилер информации о пользователе.
    """
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.requester = Requester()

    def get_puuid(self):
        """
        Получить puuid от RiotApi.
        """
        parser = ParserTFT()
        user_info = self.requester.get_user_info(self.nickname)
        puuid = parser.find_puuid(user_info)
        return puuid
