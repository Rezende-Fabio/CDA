from .configurations import Scheduler
from .configurations import Configuration
from .configurations import Blueprint
from .configurations import Database
from .configurations import Auth
from .configurations import FunctionShell
from flask import Flask

app = Flask(__name__)

def create_app():  
    #app = Flask(__name__)

    #Configurações da plicação
    Configuration.init_app(app)
    Database.init_app(app)
    Auth.init_app(app)
    FunctionShell.function_shell(app)
    Scheduler.init_app(app)
    
    #Adicionando as rotas
    Blueprint.rotasMain(app)
    Blueprint.rotasAdm(app)
    Blueprint.rotasTec(app)
    Blueprint.rotasVig(app)
    
    return app