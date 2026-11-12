
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
