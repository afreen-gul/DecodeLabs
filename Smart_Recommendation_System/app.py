from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        user_input = request.form["interests"]

        recommendations = get_recommendations(user_input)

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)