from .db import DbRecordNotExist


class TftStreamNotUp(DbRecordNotExist):
    """
    Исключения стрим не запущен.
    """
    pass
