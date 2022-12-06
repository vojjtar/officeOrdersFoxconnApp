FROM python:3.8-slim-buster


WORKDIR /officeOrdersFoxconnApp
ADD . /officeOrdersFoxconnApp

RUN pip3 install -r requirements.txt
RUN export FLASK_APP=run.py


CMD [ "python", "app.py" ]
