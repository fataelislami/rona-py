#!/usr/bin/python
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/kostlab.id/public_html/project/rona-py/')
from rona import app as application
application.secret_key = '421232121'
