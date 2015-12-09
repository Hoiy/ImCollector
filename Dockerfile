#FROM ubuntu:precise
FROM centos:7

# Install Scrapy and dependencies
RUN yum install -y epel-release
RUN yum install -y \
    gcc \
    pyOpenSSL \
    python-devel \
    python-lxml \
    python-pip 
RUN pip install --upgrade \
    pip \
    setuptools
RUN pip install scrapy
##

# Install ImCollector and dependencies
RUN yum install -y \
    libjpeg-devel \
    zlib-devel
RUN pip install image

RUN mkdir -p /scrapy
WORKDIR /scrapy
COPY ./src/ .
##

