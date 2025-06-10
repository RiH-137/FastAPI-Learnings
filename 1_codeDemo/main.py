from fastapi import FastAPI

app=FastAPI()

@app.get("/")       ## route, path, url

def hello():
    return {"message": "Hello, World!"}


## run --> uvicorn main:app --reload
### behind the scenes, uvicorn is running the ASGI app
### ASGI --> Asynchronous Server Gateway Interface  


@app.get('/about')
def abpout_function():
    return {"message": "This is the about page."}
