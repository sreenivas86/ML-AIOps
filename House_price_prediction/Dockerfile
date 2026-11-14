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

CMD [ "uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8080" ]