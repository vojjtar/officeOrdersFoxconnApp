FROM python:3.8-slim-buster


WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
RUN export FLASK_APP=app
EXPOSE 5000

COPY . ./app
RUN pip3 install -e ./app

CMD ["flask" "run"]
