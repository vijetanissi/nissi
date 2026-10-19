import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! My app is running successfully on OpenShift!"}

if __name__ == "__main__":
    # OpenShift requires listening on 0.0.0.0 and port 8080 by default
    uvicorn.run(app, host="0.0.0.0", port=8080)
