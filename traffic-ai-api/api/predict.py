# api/predict.py
import json

def handler(request, response):
    try:
        data = request.json()

        savings = int(data.get("savings", 0))
        goal = data.get("goal", "").lower()
        scheme = data.get("scheme", "").lower()

        # Basic example logic
        if savings >= 500000:
            color = "green"
            tip = "You are well on track!"
        elif 200000 <= savings < 500000:
            color = "orange"
            tip = "Consider increasing your savings."
        else:
            color = "red"
            tip = "High risk. Choose safer schemes or save more."

        return response.json({"color": color, "tip": tip})
    except Exception as e:
        return response.json({"error": str(e)}, status=400)
