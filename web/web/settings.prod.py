from .settings import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-d4c*s#i%@!&k+p$svf3(pq9yr2kf20#0g)4u@0h26wh861r#9l')
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME') 

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)