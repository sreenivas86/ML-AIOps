
## Automated Testing

This project uses Pytest and FastAPI TestClient
to validate the prediction API.

### Install dependencies

pip install -r requirements.txt

### Run tests

python -m pytest tests/ -v

### Test coverage

- Health endpoint validation
- Successful house price prediction
- Invalid numerical input
- Negative feature validation
- Missing feature validation


# Day 10 Evening - Docker Validation

## Image versions
- v1:
- v2:

## Build validation
- Initial build:
- Cached rebuild:

## Security
- Non-root execution: Pass/Fail
- Dockerignore configured: Yes/No

## API validation
- Health endpoint:
- Prediction endpoint:
- Swagger:
- v1 vs v2 comparison:

## Interview preparation
- Docker layer caching
- Image vs model versioning
- Container security
- Production rollback

# Day 10 - Docker Health Checks

## New image
house-price-api:v2.1

## Health check
- Endpoint: /health
- Interval: 10 seconds
- Timeout: 3 seconds
- Retries: 3

## Validation
- Container started:
- Docker health status:
- Swagger test:
- Prediction test:
- v1 vs v2.1 comparison:

## Learning
- Difference between running and healthy
- Docker HEALTHCHECK
- Kubernetes readiness and liveness