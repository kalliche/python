from fastapi import FastAPI

# instanciamos a fastapi
app = FastAPI()

# hacemos una operación con fastapi
@app.get("/")
async def root():
    return '!Hola FastAPI'

@app.get("/url")
async def root():
    return {'url_curso':'https://mouredev.com/python'}