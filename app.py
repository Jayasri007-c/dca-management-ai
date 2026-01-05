from flask import Flask, render_template, request
from model import predict_priority

app = Flask(__name__)

cases = []  # in-memory storage

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        case_id = len(cases) + 1
        amount = int(request.form["amount"])
        days = int(request.form["days"])
        priority = predict_priority(amount, days)

        cases.append({
            "id": case_id,
            "amount": amount,
            "days": days,
            "priority": priority,
            "status": "Pending"
        })

    return render_template("index.html", cases=cases)

@app.route("/update/<int:case_id>")
def update(case_id):
    for case in cases:
        if case["id"] == case_id:
            case["status"] = "Recovered"
    return render_template("index.html", cases=cases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

