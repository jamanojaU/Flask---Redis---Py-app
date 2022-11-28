FROM python:3.10.8
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]