# Basic FastAPI App

A small FastAPI application with a welcome endpoint and a URL-parameter greeting endpoint.

## Set up on macOS/Linux

```bash
cd fastapi-basic-app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the app

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/` for the welcome JSON or `http://127.0.0.1:8000/docs` for interactive API documentation. Stop the server with `Ctrl+C` and leave the virtual environment with `deactivate`.

## Endpoints

- `GET /` returns `{"message": "Hello, FastAPI"}`.
- `GET /greet/{name}` returns a greeting containing the name from the URL, such as `{"message": "Hello, Ada!"}` for `/greet/Ada`.

## Manual practice

With the server running, try these in a second terminal:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/greet/Ada
curl -i http://127.0.0.1:8000/greet
```

The third request has no path value, so FastAPI should respond with `404 Not Found`. You can also visit `/docs`, expand each route, select **Try it out**, and execute the request from the browser.
