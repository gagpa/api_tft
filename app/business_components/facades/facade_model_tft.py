from app.db import session
from app.exceptions.db import DbRecordNotExist
from .facade_model import FacadeModel
from ..models import TftUserModel


class FacadeStreamTft(FacadeModel):
    """
    Фаса для модели StreamTFT.
    """

    def last_match_id(self, nickname: str):
        query = session.query(self.model)
        model = query.filter(self.model.user_id == TftUserModel.id).order_by(self.model.id.desc()).first()
        if model:
            match_id = model.match_id
            return match_id
        raise DbRecordNotExist

    def placements_to(self, nickname: str, match_id: str):
        """
        Выдать все отфильтрованные матчи
        """
        rim_id = session.query(self.model.id)\
            .filter(self.model.match_id == match_id)\
            .order_by(self.model.id)\
            .first()

        matches = session.query(self.model)\
            .filter(self.model.id >= rim_id)\
            .all()

        if matches:
            placements = [match.placement for match in matches]
            return placements
        raise DbRecordNotExist

    def placements(self, nickname: str) -> list:
        """
        Вернуть все места из базы данных.
        """
        matches = session.query(self.model, TftUserModel)\
            .filter(self.model.user_id == TftUserModel.id)\
            .filter(TftUserModel.nickname == nickname)\
            .all()
        if matches:
            placements = [match[0].placement for match in matches]
            return placements
        raise DbRecordNotExist
