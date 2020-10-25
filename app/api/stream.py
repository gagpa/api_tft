from fastapi.responses import JSONResponse

from .. import app
from ..business_logics import StreamLogic


@app.get('/tft/stream_up/{nickname}')
def get_stream_up(nickname: str):
    """
    Маршут для подтверждения начала стриме.
    """
    content = StreamLogic(nickname).tft_stream_up(nickname)
    return JSONResponse(content=content)
