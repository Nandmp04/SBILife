# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    savings = int(data.get("savings"))
    goal = data.get("goal")
    scheme = data.get("scheme")

    # Dummy Logic (replace with ML model)
    if savings >= 200000:
        result = "green"
        tip = "You're financially ready for this goal!"
    elif savings >= 100000:
        result = "orange"
        tip = "You're getting close, consider boosting your SIP."
    else:
        result = "red"
        tip = "Consider saving more or choosing a lighter plan."

    return jsonify({"color": result, "tip": tip})

if __name__ == '__main__':
    app.run()
