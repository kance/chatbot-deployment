from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


# el code del decorator es para flask 2.0 sino deberia ser @app.route("/", methods=["GET"])

@app.get("/")
#@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    print("input text!")
    print(text)
    # AGREGAR por nuestro lado: check if text is valid
    response = get_response(text)
    print("da respuesta?")
    print(response)
    message = {"answer": response}
    print("answer")
    print(message)
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

