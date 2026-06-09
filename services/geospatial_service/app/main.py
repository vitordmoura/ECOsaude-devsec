from os import getenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="EcoSaude - Processamento geoespacial e dados de satélite", version="1.0.0")

class RiskResponse(BaseModel):
    service: str
    region_id: str
    risk_index: int
    trend: str
    recommendation: str

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "geospatial_service"}

@app.get("/risk/{region_id}", response_model=RiskResponse)
def get_risk(region_id: str):
    satellite_key = getenv("SATELLITE_API_KEY")
    if not satellite_key:
        raise HTTPException(status_code=500, detail="SATELLITE_API_KEY não configurada")
    return RiskResponse(service="geospatial_service", region_id=region_id, risk_index=82, trend="crescente", recommendation="priorizar vistoria preventiva e alerta comunitário")
