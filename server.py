from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    text = data["text"]

    with open("data.txt", "w") as file:
        file.write(text)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
