from fastapi import FastAPI, Body, Response

app = FastAPI()

@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "name - value"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)