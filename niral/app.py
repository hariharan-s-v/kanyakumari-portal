"""
app.py — Kanyakumari Tourism Portal Backend
Run: python app.py
Open: http://localhost:5000
"""

from niral.data import ATTRACTIONS, ACCOMMODATIONS, TRAVEL_TIPS
from datetime import datetime
import uuid
import json
import socket

from data import ATTRACTIONS, ACCOMMODATIONS, TRAVEL_TIPS

app = Flask(__name__)
BOOKINGS = []  # In-memory; swap with DB in production


# ── Helpers ──────────────────────────────────────────────────
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


@app.template_filter("commas")
def commas_filter(v):
    return "{:,}".format(int(v))


# ── Pages ─────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template(
        "index.html",
        attractions=ATTRACTIONS[:6],
        accommodations=ACCOMMODATIONS[:4],
        travel_tips=TRAVEL_TIPS,
    )


@app.route("/attractions")
def attractions_page():
    cat = request.args.get("cat", "All")
    cats = ["All"] + sorted(set(a["category"] for a in ATTRACTIONS))
    filtered = ATTRACTIONS if cat == "All" else [a for a in ATTRACTIONS if a["category"] == cat]
    return render_template("attractions.html", attractions=filtered, categories=cats, selected_cat=cat)


@app.route("/attraction/<int:att_id>")
def attraction_detail(att_id):
    att = next((a for a in ATTRACTIONS if a["id"] == att_id), None)
    if not att:
        return "<h2>Attraction not found</h2><a href='/attractions'>Back</a>", 404

    other_markers = [a for a in ATTRACTIONS if a["id"] != att_id]
    markers_json = json.dumps([
        {"id": a["id"], "name": a["name"], "lat": a["lat"],
         "lng": a["lng"], "icon": a["icon"], "cat": a["category"]}
        for a in other_markers
    ])
    all_acc_json = json.dumps([
        {"id": a["id"], "name": a["name"], "icon": a["icon"],
         "type": a["type"], "price": a["price"], "stars": a["stars"],
         "contact": a["contact"], "villa": a.get("villa", False),
         "available": a["available"]}
        for a in ACCOMMODATIONS
    ])
    fee_str = "Free Entry" if att["entry_fee"] == 0 else f"Rs. {att['entry_fee']}"
    stars_filled = int(att["rating"])
    rating_stars = "★" * stars_filled + "☆" * (5 - stars_filled)

    return render_template(
        "attraction_detail.html",
        att=att,
        fee_str=fee_str,
        rating_stars=rating_stars,
        markers_json=markers_json,
        all_acc_json=all_acc_json,
        accommodations=ACCOMMODATIONS,
    )


@app.route("/accommodations")
def accommodations_page():
    acc_type = request.args.get("type", "All")
    types = ["All"] + sorted(set(a["type"] for a in ACCOMMODATIONS))
    filtered = ACCOMMODATIONS if acc_type == "All" else [a for a in ACCOMMODATIONS if a["type"] == acc_type]
    return render_template("accommodations.html", accommodations=filtered, types=types, selected_type=acc_type)


@app.route("/stay/<int:acc_id>")
def stay_detail(acc_id):
    acc = next((a for a in ACCOMMODATIONS if a["id"] == acc_id), None)
    if not acc:
        return "<h2>Stay not found.</h2><a href='/accommodations'>Back</a>", 404

    att_markers_json = json.dumps([
        {"id": a["id"], "name": a["name"], "lat": a["lat"], "lng": a["lng"], "icon": a["icon"]}
        for a in ATTRACTIONS
    ])
    other_stays_json = json.dumps([
        {"id": a["id"], "name": a["name"], "icon": a["icon"], "type": a["type"],
         "price": a["price"], "stars": a["stars"], "lat": a["lat"], "lng": a["lng"],
         "villa": a.get("villa", False)}
        for a in ACCOMMODATIONS if a["id"] != acc_id
    ])
    stars_str = "★" * acc["stars"] + "☆" * (5 - acc["stars"])

    return render_template(
        "stay_detail.html",
        acc=acc,
        stars_str=stars_str,
        att_markers_json=att_markers_json,
        other_stays_json=other_stays_json,
        attractions=ATTRACTIONS[:4],
    )


@app.route("/villas")
def villas_page():
    villa_stays = [a for a in ACCOMMODATIONS if a.get("villa")]
    villa_spots = [a for a in ATTRACTIONS if "tribal" in a.get("tags", [])]
    return render_template("villas.html", villa_stays=villa_stays, villa_spots=villa_spots)


@app.route("/book", methods=["GET", "POST"])
def book():
    acc_id = request.args.get("id", 1, type=int)
    acc = next((a for a in ACCOMMODATIONS if a["id"] == acc_id), ACCOMMODATIONS[0])

    if request.method == "POST":
        check_in = request.form.get("check_in", "")
        check_out = request.form.get("check_out", "")
        try:
            ci = datetime.strptime(check_in, "%Y-%m-%d")
            co = datetime.strptime(check_out, "%Y-%m-%d")
            nights = max((co - ci).days, 1)
        except Exception:
            nights = 1
        total = nights * acc["price"]
        booking = {
            "id": str(uuid.uuid4())[:8].upper(),
            "guest_name": request.form.get("name", ""),
            "email": request.form.get("email", ""),
            "phone": request.form.get("phone", ""),
            "accommodation_id": acc_id,
            "accommodation": acc["name"],
            "acc_type": acc["type"],
            "check_in": check_in,
            "check_out": check_out,
            "guests": request.form.get("guests", "2"),
            "special_requests": request.form.get("special_requests", ""),
            "nights": nights,
            "price_per_night": acc["price"],
            "total": total,
            "status": "Confirmed",
            "booked_at": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        }
        BOOKINGS.append(booking)
        return redirect(f"/confirmation/{booking['id']}")

    today = datetime.now().strftime("%Y-%m-%d")
    return render_template("book.html", acc=acc, today=today)


@app.route("/confirmation/<booking_id>")
def confirmation(booking_id):
    booking = next((b for b in BOOKINGS if b["id"] == booking_id), None)
    if not booking:
        return "<h2>Booking not found.</h2><a href='/'>← Home</a>", 404
    acc = next((a for a in ACCOMMODATIONS if a["id"] == booking["accommodation_id"]), {})
    return render_template("confirmation.html", booking=booking, acc=acc)


# ── REST API ──────────────────────────────────────────────────
@app.route("/api/attractions")
def api_attractions():
    cat = request.args.get("category")
    data = [a for a in ATTRACTIONS if a["category"] == cat] if cat else ATTRACTIONS
    return jsonify({"count": len(data), "attractions": data})


@app.route("/api/accommodations")
def api_accommodations():
    acc_type = request.args.get("type")
    data = [a for a in ACCOMMODATIONS if a["type"] == acc_type] if acc_type else ACCOMMODATIONS
    return jsonify({"count": len(data), "accommodations": data})


@app.route("/api/book", methods=["POST"])
def api_book():
    body = request.get_json(force=True)
    acc_id = body.get("accommodation_id", 1)
    acc = next((a for a in ACCOMMODATIONS if a["id"] == acc_id), None)
    if not acc:
        return jsonify({"error": "Accommodation not found"}), 404
    try:
        ci = datetime.strptime(body["check_in"], "%Y-%m-%d")
        co = datetime.strptime(body["check_out"], "%Y-%m-%d")
        nights = max((co - ci).days, 1)
    except Exception:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    booking = {
        "id": str(uuid.uuid4())[:8].upper(),
        "guest_name": body.get("name"),
        "email": body.get("email"),
        "phone": body.get("phone"),
        "accommodation_id": acc_id,
        "accommodation": acc["name"],
        "acc_type": acc["type"],
        "check_in": body["check_in"],
        "check_out": body["check_out"],
        "guests": body.get("guests", 2),
        "nights": nights,
        "price_per_night": acc["price"],
        "total": nights * acc["price"],
        "status": "Confirmed",
        "booked_at": datetime.now().isoformat(),
    }
    BOOKINGS.append(booking)
    return jsonify({"success": True, "booking": booking}), 201


@app.route("/api/bookings")
def api_bookings():
    return jsonify({"count": len(BOOKINGS), "bookings": BOOKINGS})


@app.route("/api/tips")
def api_tips():
    return jsonify(TRAVEL_TIPS)


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":
    PORT = 5000
    local_ip = get_local_ip()
    print("\n+----------------------------------------------------------+")
    print("|      KANYAKUMARI TOURISM PORTAL — Starting Up...        |")
    print("+----------------------------------------------------------+")
    print(f"|  Local:    http://localhost:{PORT}                          |")
    print(f"|  Network:  http://{local_ip}:{PORT}                   |")
    print("+----------------------------------------------------------+")
    print("|  Pages: /  /attractions  /accommodations  /villas       |")
    print("|  API:   /api/attractions  /api/accommodations            |")
    print("+----------------------------------------------------------+\n")
    app.run(debug=True, port=PORT, host="0.0.0.0")
