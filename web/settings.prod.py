import dj_database_url
from .settings import *

SECRET_KEY = os.environ.get(
    'SECRET_KEY', default='1ef68649e6429d5074d7138346477ef2')
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': dj_database_url.config(
        # N'hésitez pas à modifier cette valeur en fonction de vos besoins.
        default='postgres://itdevsuccess:9hhbXch99Elsl9Db42p7yDV90WT8ClYL@dpg-ci07lgj3cv20nhscapc0-a/web_25oz',
        conn_max_age=600
    )
}

STATIC_URL = '/static/'

# Ce paramètre indique à Django à quelle URL les fichiers statiques seront servis à l'utilisateur.
# Ici, ils seront bien accessibles sur votre-domaine.onrender.com/static/...

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Dites à Django de copier les statiques dans le répertoire `staticfiles`
    # dans votre répertoire d'application sur Render.
    # Activez le backend de stockage WhiteNoise qui prend en charge la compression des fichiers statiques
    # et en créant des noms uniques pour chaque version afin qu'ils puissent être mis en cache en toute sécurité pour toujours.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
