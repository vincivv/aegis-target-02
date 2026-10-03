# aegis-target-02 · notes service

Flask + SQLite notes API.

Monitored by [AEGIS](https://github.com/vincivv): every push to this repo is scanned autonomously by an AEGIS sentinel agent.

## Run

```bash
pip install -r requirements.txt && python app.py
```

## Routes

- `GET /health`
- `GET /notes`
- `GET /notes/<id>`
- `POST /notes {title, body}`
