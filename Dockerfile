FROM python:3.6.1-alpine
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","assistant.py"]