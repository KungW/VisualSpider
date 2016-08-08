import sae

from vs_proj import wsgi

application = sae.create_wsgi_app(wsgi.application)
