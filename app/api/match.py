from fastapi.responses import JSONResponse

from .. import app
from ..business_logics import MatchLogic


@app.get('/tft/match_per_stream/{nickname}')
def get_last_match(nickname):
    """
    Маршут для получения информации о сыгранных матчах на стриме.
    """
    content = MatchLogic().get_stats_per_stream(nickname)
    return JSONResponse(content=content)


@app.options('/tft/match_per_stream/{nickname}')
def opt_last_match(nickname):
    """
    Маршут для исправления бага с AJAX запроса.
    Необходимо в будущем исправить данный костыль.
    """
    return {'1': 1}
