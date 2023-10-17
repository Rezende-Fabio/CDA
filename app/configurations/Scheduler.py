from flask_apscheduler import APScheduler
from ..extensions.Integracao import Integracao

scheduler = APScheduler()

def init_app(app):
    scheduler.init_app(app)
    scheduler.start()

    @scheduler.task('cron', id='my_job', day_of_week='sun', hour=17, minute=0)
    def my_job():
        intergracao = Integracao()
        intergracao.integraFunc()
    
