from fastapi.responses import JSONResponse

from app import app
from app.business_logics import MatchLogic
from app.exceptions.tft import TftStreamNotUp


@app.get('/tft/score/{nickname}')
def get_last_match(nickname):
    """
    Маршут для получения информации о сыгранных матчах на стриме.
    """
    try:
        content = MatchLogic().get_stats_per_stream(nickname)
    except TftStreamNotUp:
        content = \
            {
                'successful': False,
                'error':
                    {
                        'description': 'Стрим не запущен'
                    }
            }
    return JSONResponse(content=content)


@app.options('/tft/score/{nickname}')
def opt_last_match(nickname):
    """
    Маршут для исправления бага с AJAX запроса.
    Необходимо в будущем исправить данный костыль.
    """
    content = \
        {
            'successful': True,
            'data':
                {
                    'nickname': nickname
                }
        }

    return JSONResponse(content=content)


@app.get('/tft/count_places/{nickname}')
def get_count_places(nickname):
    """
    Маршут для получения статистики побед.
    """
    content = MatchLogic().get_count_places(nickname)
    return JSONResponse(content=content)


@app.options('/tft/count_places/{nickname}')
def opt_count_places(nickname):
    """
    Маршут для исправления бага с AJAX запроса.
    Необходимо в будущем исправить данный костыль.
    """
    content = \
        {
            'successful': True,
            'data':
                {
                    'nickname': nickname
                }
        }

    return JSONResponse(content=content)
