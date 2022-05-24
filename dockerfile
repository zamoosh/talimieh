FROM python:3
# RUN apt-get update
# RUN apt-get install -y build-essential cmake zlib1g-dev libcppunit-dev git subversion wget python3 python3-pip && rm -rf /var/lib/apt/lists/*
# RUN wget https://ftp.openssl.org/source/old/1.0.2/openssl-1.0.2k.tar.gz -O - | tar -xz
# WORKDIR /openssl-1.0.2k
# RUN ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl && make && make install

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# fa_IR UTF-8/fa_IR UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG fa_IR.UTF-8
ENV LC_ALL fa_IR.UTF-8

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN rm -rf /app/cicd
RUN rm -rf /app/dockerfile
RUN rm -rf /app/.gitignore
RUN rm -rf /app/.gitlab-ci.yml
#RUN rm -rf /app/static
#RUN python manage.py migrate
#CMD python manage.py runserver 0.0.0.0:80
