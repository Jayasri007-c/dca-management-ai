def predict_priority(amount, days):
    if amount > 100000 or days > 60:
        return "HIGH"
    elif amount > 40000:
        return "MEDIUM"
    else:
        return "LOW"
