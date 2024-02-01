FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

COPY ./prediction_request.py /code/prediction_request.py

COPY ./utils.py /code/utils.py

COPY ./model_1 /code/model_1

COPY ./model_2 /code/model_2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]