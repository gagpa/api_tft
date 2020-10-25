from app.db import session


class ModelFacade:

    def __init__(self, model=None):
        self.model = model

    def init_model(self, model):
        self.model = model

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.model, key, value)
        session.add(self.model)
        session.commit()
