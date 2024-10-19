from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/students", status_code=201)
async def create_student():
	return {"id": "0"}
