from os import getenv
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health_check():
    return jsonify({
        "status": "ok",
        "service": "ecosaude-forecast-service"
    })


@app.get("/risk/<region_id>")
def get_region_risk(region_id):
    satellite_api_key = getenv("SATELLITE_API_KEY")
    climate_api_key = getenv("CLIMATE_API_KEY")
    database_url = getenv("DATABASE_URL")

    return jsonify({
        "region_id": region_id,
        "risk_index": 82,
        "trend": "crescente",
        "recommendation": "priorizar alerta preventivo e vistoria sanitária",
        "satellite_api_configured": bool(satellite_api_key),
        "climate_api_configured": bool(climate_api_key),
        "database_configured": bool(database_url)
    })
