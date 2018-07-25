FROM python:3
ADD . /app
WORKDIR /app
RUN mkdir database
RUN pip3 install flask 
EXPOSE 5555
CMD ["python3","write.py"]
