from fastapi import FastAPI

app = FastAPI(title="Workout Tracker API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Powerlifting Workout Tracker API (5/3/1 Periodization)"}
