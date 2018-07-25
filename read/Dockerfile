FROM python:3
ADD . /app
WORKDIR /app
RUN mkdir database
RUN pip3 install flask 
EXPOSE 7777
CMD ["python3","read.py"]
