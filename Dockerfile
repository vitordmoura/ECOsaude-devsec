FROM python:3.11-slim

WORKDIR /app

RUN addgroup --system ecosaude && adduser --system --ingroup ecosaude ecosaude

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

USER ecosaude

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.main:app"]
