from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/students", status_code=201)
async def create_student():
	return {"id": "0"}
