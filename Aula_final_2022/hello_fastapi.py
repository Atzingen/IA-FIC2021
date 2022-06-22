from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/evaluate")
async def run_ml_model():
    '''
    Nesta rota recebemos um pedido de processamento dos dados
    e retornamos a, b ou c
    '''
    return {"message": "overfit !"}