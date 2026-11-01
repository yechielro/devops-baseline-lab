# DevOps Course Starter — Flask

## Ubuntu / WSL2

```bash
cd starter
sudo apt update && sudo apt install -y python3-venv python3-pip
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt
.venv/bin/python -m pytest -q
.venv/bin/python app.py
```

From a second Ubuntu terminal:

```bash
curl -s http://127.0.0.1:5000/
curl -s http://127.0.0.1:5000/health
curl -s http://127.0.0.1:5000/version
```

Expected JSON contains `service: devops-course`, `status: ok`, `version: 1.0.0`.

## Docker (meeting 4+)

```bash
docker build -t devops-course:1.0.0 .
docker run --rm -p 127.0.0.1:5000:5000 devops-course:1.0.0
```

Or `docker compose up --build` (do not run both on port 5000).

This is a learning application, not production hardened. The sample CI tests Python only and does not deploy to each student's private laptop.

Workshop completed locally.
