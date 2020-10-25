from app.db import session
from .model_facade import ModelFacade


class ModelFacadeStreamTFT(ModelFacade):

    @property
    def last_match_id(self):
        model = session.query(self.model).order_by(self.model.id).limit(1).first()
        match_id = model.match_id
        return match_id
