# Python imports

# Core Flask imports
from flask import Flask
# Third-Party imports
from celery import Celery
# Apps Imports
import settings
from app.aggregators.tasks import my_background_task

app = Flask(__name__)
app.config.from_object(settings)

app.config['CELERY_BROKER_URL'] = 'amqp://vanellope:vanellope@localhost:5672/vanellope_vhost'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

celery.autodiscover_tasks((
	'data_collector.app.aggregators.tasks',
))
