import os
import logging
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_TEMPLATE = os.path.join(APP_ROOT, 'template')
APP_CONFIG= os.path.join(APP_ROOT, 'config')
APP_EXPORT= os.path.join(APP_ROOT, 'export')
APP_LOGS= os.path.join(APP_ROOT, 'logs')
APP_ASSETS= os.path.join(APP_ROOT, 'assets')
#LOG_FILE=os.path.join(APP_ROOT,"logs/my_bandit.log")
LOG_LEVEL=logging.DEBUG
