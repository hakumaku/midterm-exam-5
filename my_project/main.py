from fastapi import FastAPI


app = FastAPI()

import random

@app.get("/")
async def root():
    return {"message": "Hello World"}

import string
@app.get('/foo')
async def get_foo():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    return {'my_message': f'hello, foo world! {random_string}'}
@app.get('/bar')
async def get_bar():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    return {'my_message': f'hello, bar world! {random_string}'}
@app.get('/spam')
async def get_spam():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    return {'my_message': f'hello, spam world! {random_string}'}
@app.get('/eggs')
async def get_eggs():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    return {'my_message': f'hello, eggs world! {random_string}'}
@app.get('/bacon')
async def get_bacon():
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    return {'my_message': f'hello, bacon world! {random_string}'}
