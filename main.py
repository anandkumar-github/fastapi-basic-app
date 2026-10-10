from fastapi import FastAPI

app = FastAPI(
    title="Basic FastAPI App",
    description="A beginner-friendly API with a welcome route and a greeting route.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """Return a welcome message from the root endpoint."""
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}")
def greet(name: str):
    """Greet the person whose name is included in the URL."""
    return {"message": f"Hello, {name}!"}
