import random
import string

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/foo")
async def get_foo():
    random_string = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    # 필독 🙋 🙋 🙋
    # "my_message"는 main 브랜치 코드를 따라가고 (바꾸지 말고),
    # Howard는 자기 이름으로 바꿀 것
    return {"my_message": f"hello, Howard world! {random_string}"}


@app.get("/bar")
async def get_bar():
    random_string = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    # 필독 🙋 🙋 🙋
    # "my_message"는 main 브랜치 코드를 따라가고 (바꾸지 말고),
    # Howard는 자기 이름으로 바꿀 것
    return {"my_message": f"hello, Howard world! {random_string}"}


@app.get("/spam")
async def get_spam():
    random_string = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    # 필독 🙋 🙋 🙋
    # "my_message"는 main 브랜치 코드를 따라가고 (바꾸지 말고),
    # Howard는 자기 이름으로 바꿀 것
    return {"my_message": f"hello, Howard world! {random_string}"}


@app.get("/eggs")
async def get_eggs():
    random_string = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    # 필독 🙋 🙋 🙋
    # "my_message"는 main 브랜치 코드를 따라가고 (바꾸지 말고),
    # Howard는 자기 이름으로 바꿀 것
    return {"my_message": f"hello, Howard world! {random_string}"}


@app.get("/bacon")
async def get_bacon():
    random_string = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    # 필독 🙋 🙋 🙋
    # "my_message"는 main 브랜치 코드를 따라가고 (바꾸지 말고),
    # Howard는 자기 이름으로 바꿀 것
    return {"my_message": f"hello, Howard world! {random_string}"}
