from app.business_modules import MatchesInfoDealer, UserInfoDealer
from app.business_modules.entitys import TftStreamEntity, TftUserEntity
from app.exceptions.db import DbRecordNotExist
from app.exceptions.user import UnregisteredUser


class StreamLogic:
    """
    Класс отвечающий за взаимодействия со стримом.
    """

    def __init__(self, streamer_nickname: str):
        self.streamer_nickname = streamer_nickname

    def tft_stream_up(self):
        """
        Обозначить стрим заущен.
        """
        user_dealer = UserInfoDealer(self.streamer_nickname)
        match_dealer = MatchesInfoDealer()
        stream = TftStreamEntity()

        puuid = user_dealer.get_puuid()
        last_match_id = match_dealer.get_last_match_id(puuid)

        try:
            stream.up(self.streamer_nickname, last_match_id)
        except DbRecordNotExist:
            raise UnregisteredUser

        return {'successful': True}

    def registrate(self):
        user_dealer = UserInfoDealer(self.streamer_nickname)
        puuid = user_dealer.get_puuid()

        user = TftUserEntity()

        user.save(nickname=self.streamer_nickname, puuid=puuid)
