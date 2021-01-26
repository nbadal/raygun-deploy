FROM python:3-alpine

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY deployment.py /

ENTRYPOINT ["python", "/deployment.py"]