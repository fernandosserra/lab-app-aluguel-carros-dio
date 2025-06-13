import datetime
import json
import azure.functions as func  # requires azure-functions package

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Simulação de dados — em produção você consultaria um DB
    rentals = [
        {"id": 1, "customer": "Ana", "due_date": "2025-06-10"},
        {"id": 2, "customer": "Bruno", "due_date": "2025-06-20"},
        {"id": 3, "customer": "Carlos", "due_date": "2025-06-09"}
    ]

    hoje = datetime.date.today()
    pendentes = []
    for r in rentals:
        due = datetime.datetime.fromisoformat(r["due_date"]).date()
        days_left = (due - hoje).days
        if days_left < 0 or days_left <= 1:
            pendentes.append({**r, "days_left": days_left})

    body = json.dumps({"notify": pendentes})
    return func.HttpResponse(body, status_code=200, mimetype="application/json")