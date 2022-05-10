from threading import Thread
from manage import app

if __name__ == "__main__":
    app.run(threaded=True)