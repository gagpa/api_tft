from app.db import db, Base, session
from .tft_user_model import TftUserModel
from app.exceptions.db import DbRecordNotExist


class TftStreamModel(Base):
    """
    Модель таблицы tft_stream.
    Здесь записывается информации о начале стрима.
    """
    __tablename__ = 'tft_stream'
    id = db.Column(db.Integer, primary_key=True)
    start_datetime = db.Column(db.DateTime())
    match_id = db.Column(db.VARCHAR(25))
    user_id = db.Column(db.Integer, db.ForeignKey('tft_user.id'))
    user = db.orm.relationship('TftUserModel', backref='streams')

    @property
    def nickname(self):
        return

    @nickname.setter
    def nickname(self, value):
        user = TftUserModel.query.filter_by(nickname=value).first()
        print(user)
        if user:
            self.user_id = user.id
        else:
            raise DbRecordNotExist
