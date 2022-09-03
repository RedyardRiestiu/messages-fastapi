from fastapi import FastAPI

app = FastAPI()


@app.get('/')      # http://messenger.updomain/ >>app.get<<
def root():
    return {'message': 'It works!'}

