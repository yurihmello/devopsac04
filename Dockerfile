FROM python:3.6.1-alpine
RUN pip install flask
COPY fibonaci.py /fibonaci.py
CMD ["python","fibonaci.py"]
