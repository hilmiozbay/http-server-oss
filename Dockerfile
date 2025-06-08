FROM python:3.8-slim

WORKDIR /app

COPY server.py .
COPY static/ static/


EXPOSE 8080

CMD ["python", "server.py"] 