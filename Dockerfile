FROM python:3.8
ADD requirements.txt /app/requirements.txt
RUN apk update && pip install -r requirements.txt
COPY . /app/
WORKDIR /app
COPY requirements.txt /requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]