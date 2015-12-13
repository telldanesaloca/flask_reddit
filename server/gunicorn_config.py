# Refer to the following link for help:
# http://docs.gunicorn.org/en/latest/settings.html
command = '/home/red/Projects/reddit-env/bin/gunicorn'
pythonpath = '/home/red/Projects/reddit-env/flask_reddit'
bind = '127.0.0.1:8040'
workers = 1
user = 'red'
accesslog = '/home/red/Projects/reddit-env/flask_reddit/logs/gunicorn-access.log'
errorlog = '/home/red/Projects/reddit-env/flask_reddit/logs/gunicorn-error.log'
