FROM python:3-alpine

COPY health.py /app/health.py

ENTRYPOINT ["python3", "/app/health.py"]