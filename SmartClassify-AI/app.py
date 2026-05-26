from flask import Flask, render_template, request
from model import predict_flower

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        features = [

            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"])
        ]

        prediction = predict_flower(features)

    return render_template(

        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)