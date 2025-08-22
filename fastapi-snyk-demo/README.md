# FastAPI + Snyk Demo

This is a dummy FastAPI project with intentional vulnerabilities for testing Snyk.

## Run FastAPI
```bash
uvicorn app.main:app --reload --port 8000
```

Visit [http://localhost:8000](http://localhost:8000)

## Snyk Scans
```bash
snyk test --file=requirements.txt --python
snyk code test
snyk test --file=requirements.txt --python --json > snyk_report.json
```
