from flask import Flask

app  = Flask("api")

from api.router.router import *