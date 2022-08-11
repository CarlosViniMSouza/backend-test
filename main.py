from fastapi import FastAPI, applications

app = FastAPI()


@app.get("/")
async def hello():
    return {"status": "project inited"}
