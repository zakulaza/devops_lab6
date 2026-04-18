from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def get_orders():
    return {"status": "success", "data": "Тут будуть замовлення"}

@app.get("/")
def read_root():
    return {"message": "Hello from Docker and CI/CD!"}