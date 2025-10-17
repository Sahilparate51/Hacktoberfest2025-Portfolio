from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Base quote dataset
quotes = [
    {"id": 1, "author": "Albert Einstein", "quote": "Imagination is more important than knowledge."},
    {"id": 2, "author": "Marie Curie", "quote": "Nothing in life is to be feared, it is only to be understood."},
    {"id": 3, "author": "Mahatma Gandhi", "quote": "Be the change that you wish to see in the world."},
    {"id": 4, "author": "Nelson Mandela", "quote": "It always seems impossible until it's done."}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Daily Quotes API - Hacktoberfest 2025 🎉",
        "routes": {
            "/quote": "Get a random quote",
            "/quotes": "Get all quotes",
            "/add": "POST a new quote"
        },
        "contributors": "You can contribute by adding quotes, features, or documentation!"
    })

@app.route("/quote")
def random_quote():
    """Return one random quote."""
    return jsonify(random.choice(quotes))

@app.route("/quotes")
def all_quotes():
    """Return all quotes."""
    return jsonify({
        "count": len(quotes),
        "quotes": quotes
    })

@app.route("/add", methods=["POST"])
def add_quote():
    """Add a new quote (expects JSON: {author: '', quote: ''})."""
    data = request.get_json()
    if not data or "author" not in data or "quote" not in data:
        return jsonify({"error": "Invalid format. Use {author: '', quote: ''}"}), 400
    
    new_quote = {
        "id": len(quotes) + 1,
        "author": data["author"].strip(),
        "quote": data["quote"].strip()
    }
    quotes.append(new_quote)
    return jsonify({"message": "Quote added successfully!", "quote": new_quote}), 201

@app.route("/search/<string:author>")
def search_by_author(author):
    """Find quotes by a specific author."""
    results = [q for q in quotes if author.lower() in q["author"].lower()]
    if results:
        return jsonify(results)
    return jsonify({"message": "No quotes found for that author."}), 404

# ---- Run the app ----
if __name__ == "__main__":
    app.run(debug=True)
