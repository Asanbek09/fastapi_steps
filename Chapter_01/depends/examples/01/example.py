from fastapi import FastAPI, Depends, params

app = FastAPI()

def user_dep(name: str = params, password: str = params):
    return {"name": name, "valid": True}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("example:app", reload=True)