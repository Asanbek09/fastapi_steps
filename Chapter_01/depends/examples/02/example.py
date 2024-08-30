from fastapi import FastAPI, Depends, params

app = FastAPI()

def check_dep(name: str = params, password: str = params):
    if not name:
        raise

@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("example:app", reload=True)