FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# create a non root user
RUN addgroup --system app && \
    adduser --system --ingroup app app

# Install dependecies first for better caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy application and model files
COPY --chown=app:app . .
# Run as non-root
USER app

EXPOSE 8080

# health check
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)" || exit 1

CMD [ "uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8080" ]