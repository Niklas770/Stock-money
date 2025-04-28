from fastapi import FastAPI

app = FastAPI()

@app.get("/analyze")
def analyze(ticker: str):
    return {"ticker": ticker, "recommendation": "Buy"}