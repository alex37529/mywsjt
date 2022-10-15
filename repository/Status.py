from WSJTXClass import WSJTX_Decode
from models.WSJTX_models import WSJTX_Status as WSJTX_StatusModel


class WSJTX_StatusRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **filters):
        pass

    def list(self):
        return [
            obj.dict() for obj in self.session.query(WSJTX_StatusModel).all()
        ]

    def add(self, obj):
        self.session.add(obj)
        return obj

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
