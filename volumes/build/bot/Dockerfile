FROM python:3.8

COPY ./requirements.txt .
WORKDIR /code

RUN pip install -r /requirements.txt

COPY ./src/ ./src

CMD [ "python", "/code/src/main.py" ]