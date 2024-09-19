from flask import Flask

app = Flask(__name__)
#Endpoints
@app.route("/", methods=['GET'])

def hola():
    return "Hola mundo"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
