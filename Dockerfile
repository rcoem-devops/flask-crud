
FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN python create_table.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
