from app.db import db, Base


class TftUserModel(Base):
    """
    Модель таблицы tft_user.
    Здесь записывается основная информация о пользователе.
    """
    __tablename__ = 'tft_user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.VARCHAR(25), unique=True)
    server_name = db.Column(db.CHAR(3), default='RU')
    puuid = db.Column(db.VARCHAR(78), unique=True)
