from fastapi import FastAPI

@app.route('/')
def root():
    return "Hello World"