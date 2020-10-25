from app.db import db, Base


class StreamTFTModel(Base):
    """
    Модель стрима
    """
    __tablename__ = 'stream_tft'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.VARCHAR(25))
    datetime = db.Column(db.DateTime())
    match_id = db.Column(db.VARCHAR(25))
