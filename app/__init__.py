from fastapi import FastAPI

from .db import *

app = FastAPI()

from . import routes
