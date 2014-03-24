# def webapp_add_wsgi_middleware(app):
#     from google.appengine.ext.appstats import recording
#     app = recording.appstats_wsgi_middleware(app)
#     return app
import sys
import os

lib_dir = os.path.join(os.path.dirname(__file__), 'fumoufeed')

# add vendor path
sys.path.insert(0, lib_dir)
