FROM ubuntu:20.04

COPY . /EMI-Toolkit
COPY requirements.txt /

RUN \
  apt-get update && \
  apt-get install -y python3 python3-pip python3-dev
# RUN apt-get -y update
# RUN apt-get install python3.8 -y
# RUN apt-get install python3-pip -y
RUN pip install -r /requirements.txt
RUN apt-get install tk -y
RUN apt install python3-tk -y
# RUN apt-get install python3.8-tk -y

CMD [ "python3","/EMI-Toolkit/main.py" ]