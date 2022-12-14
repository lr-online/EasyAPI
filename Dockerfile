# help: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple -r /app/requirements.txt

COPY ./app /app