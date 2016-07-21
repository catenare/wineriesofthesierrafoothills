import sys
import subprocess
from application import app
from flask_frozen import Freezer
from livereload import Server, shell


def freeze_the_app():
    app.config['JSMAIN'] = 'main-built'
    freezer = Freezer(app)
    subprocess.call(['compass compile -e production --force'], shell=True)
    subprocess.call(['r.js -o build.js'], shell=True)
    freezer.freeze()


def do_livereload():
    server = Server(app.wsgi_app)
    server.watch('sass',shell("compass compile -c config.rb"),delay="forever")
    server.watch('application/static')
    server.watch('application/templates')
    server.serve(liveport=35729,debug=True,restart_delay=2)

if __name__ == "__main__":
    console_arg = ""
    if len(sys.argv) > 1:
        console_arg = sys.argv[1]
        
    if console_arg == "build":
        freeze_the_app()
        
    elif console_arg == "livereload":
        do_livereload()
        
    else:
        app.run(debug=True)
