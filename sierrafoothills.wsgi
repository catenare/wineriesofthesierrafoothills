import sys
sys.path.insert(0, '/Users/johan/Projects/clients/wineriesofthesierrafoothills/statichtml/webform')

activate_this = "/Users/johan/Projects/learn/learnwsgi/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from sierrafoothills import app as application
