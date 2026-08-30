from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Simple In‑Memory Inventory (später DB ersetzen) ---
inventory = []


# -------------------------------------------------------
# GET / — API Info
# -------------------------------------------------------
@app.route("/", methods=["GET"])
def api_info():
    return jsonify({
        "name": "Inventory API",
        "version": "1.0.0",
        "status": "running"
    })


# -------------------------------------------------------
# GET /health — Health Status
# -------------------------------------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# -------------------------------------------------------
# GET /inventory — Produktliste zurückgeben
# -------------------------------------------------------
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# -------------------------------------------------------
# POST /inventory — Produkt hinzufügen
# -------------------------------------------------------
@app.route("/inventory", methods=["POST"])
def add_product():
    data = request.get_json()

    # Minimalvalidierung
    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "name and quantity required"}), 400

    product = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "quantity": data["quantity"]
    }

    inventory.append(product)
    return jsonify(product), 201


# -------------------------------------------------------
# Start
# -------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
