from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    text = data["text"]

    with open("data.json", "r") as file:
        data = json.load(file)
        stories = int(data["stories"])
        library = data["library"]
        stories += 1
        library.append(text)
    with open("data.json", "w") as file:
        json.dump({"stories": str(stories), "library": library}, file, indent=4)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)

