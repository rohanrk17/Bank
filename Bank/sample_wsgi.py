'''
Created on Jan 30, 2018

@author: Rohan
'''
import os
import sys

path='/home/pythonanywhererohanKarwar/Bank'

if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTING_MODULE']='Bank.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application=StaticFilesHandler(get_wsgi_application())