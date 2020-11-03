from app.db import db, Base
from .tft_user_model import TftUserModel
from app.exceptions.db import DbRecordNotExist


class TftUserHistoryModel(Base):
    """
    Модель таблицы tft_user_history.
    Здесь записывается информация о матчах пользователя.
    """
    __tablename__ = 'tft_user_history'
    id = db.Column(db.Integer, primary_key=True)
    placement = db.Column(db.CHAR(1))
    match_id = db.Column(db.VARCHAR(25), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tft_user.id'))

    @property
    def nickname(self):
        user = TftUserModel.query.filter_by(id=self.user_id).first()
        return user.nickname

    @nickname.setter
    def nickname(self, value):
        user = TftUserModel.query.filter_by(nickname=value).first()
        if user:
            self.user_id = user.id
        else:
            raise DbRecordNotExist
