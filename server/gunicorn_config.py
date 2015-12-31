# Refer to the following link for help:
# http://docs.gunicorn.org/en/latest/settings.html
command = '/opt/board/venv/bin/gunicorn'
pythonpath = '/opt/board'
bind = '127.0.0.1:8040'
workers = 1
user = 'board'
accesslog = '/var/log/board/gunicorn-access.log'
errorlog = '/var/log/board/gunicorn-error.log'
