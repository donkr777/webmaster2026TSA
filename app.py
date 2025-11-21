from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/references")
def references():
    return render_template("references.html")

if __name__ == "__main__":
    app.run(debug=True)


