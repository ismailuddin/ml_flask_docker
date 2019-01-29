FROM python:3.6

EXPOSE 5000
ENV FLASK_APP /app/app.py

WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt

CMD python app.py