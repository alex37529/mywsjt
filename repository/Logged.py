from WSJTXClass import WSJTX_Decode
from models.WSJTX_models import WSJTX_Logged as WSJTX_LoggedModel


class WSJTX_LoggedRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **filters):
        pass

    def list(self):
        return [
            obj.dict() for obj in self.session.query(WSJTX_LoggedModel).all()
        ]

    def add(self, obj):
        self.session.add(obj)
        return obj

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
