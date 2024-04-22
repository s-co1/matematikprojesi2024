from flask import Flask

serv = Flask(__name__)
import route
import sourcepush

route.set_app(serv)
if __name__ == "__main__":
    serv.run(debug=True)