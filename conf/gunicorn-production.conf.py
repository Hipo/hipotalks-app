chdir = "/hipotalks"
bind = "0.0.0.0:8000"
env = "DJANGO_SETTINGS_MODULE=hipotalks.settings.production"
pid = "/tmp/project-master.pid"
workers = 2
timeout = 80
max_requests = 5000
accesslog = '-'  # log to stdout
errorlog = '-'  # log to stderr