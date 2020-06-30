FROM python:3.6-alpine

LABEL Version="0.1"
RUN pip3 install boto3
RUN pip3 install awscli --upgrade
COPY files/gen.py /tmp
ENV S3BUCKET null
WORKDIR /tmp/
ENTRYPOINT python /tmp/gen.py $S3BUCKET


