from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def load_locations():
    """Load locations from JSON file"""
    try:
        with open('locations.json', 'r') as f:
            data = json.load(f)
            return data.get('locations', [])
    except FileNotFoundError:
        print("Warning: locations.json not found. Using empty list.")
        return []
    except json.JSONDecodeError:
        print("Warning: Error parsing locations.json. Using empty list.")
        return []

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
    locations = load_locations()
    return render_template("map.html", locations=locations)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/api/locations")
def get_locations():
    locations = load_locations()
    return jsonify(locations)

if __name__ == "__main__":
    app.run(debug=True)