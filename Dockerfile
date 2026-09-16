FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run as non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000

# Use gunicorn instead of Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
