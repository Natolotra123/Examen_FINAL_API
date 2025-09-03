from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/cars")
def add_car(identifiant: str, brand: str, model: str):
    new_car = {"identifiant": identifiant, "brand": brand, "model": model}
    cars.append(new_car)
    return {"message": "Car créer", "id": identifiant, status: 201}

@app.get("/cars")
def get_cars():
    return cars

@app.get("/cars/{id}")
def get_car_id(id: str):
    for car in cars:
        if car["identifiant"] == id:
            return car
    return {"message": "Car n'éxiste pas"}
