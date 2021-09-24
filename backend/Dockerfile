FROM python:3
ADD requirements-base.txt /app/requirements-base.txt
RUN pip install -r app/requirements-base.txt
COPY .. /app/
WORKDIR /app
