FROM python:3-slim
WORKDIR /programas/ingesta
RUN pip3 install boto3 pandas pymysql
COPY . .
CMD [ "python3", "./ingesta.py" ]
