from fastapi.responses import JSONResponse

from app import app
from app.business_logics import StreamLogic
from app.exceptions.user import UnregisteredUser


@app.get('/tft/stream_up/{nickname}')
def get_stream_up(nickname: str):
    """
    Маршут для подтверждения начала стриме.
    """
    try:
        content = StreamLogic(nickname).tft_stream_up()
    except UnregisteredUser:
        content = \
            {
                'successful': False,
                'error':
                    {
                        'description': 'Пользователь не зарегистрирован'
                    }
            }
    return JSONResponse(content=content)


@app.get('/tft/registration/{nickname}')
def registration(nickname):
    content = StreamLogic(nickname).registrate()
    return JSONResponse(content=content)


@app.options('/tft/steam_up/{nickname}')
def opt_stream_up(nickname: str):
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

