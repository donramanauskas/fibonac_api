FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /fibonaci_api

# Set /fibonaci_app as root directory
WORKDIR /fibonaci_api

# copy requirements.txt to container
COPY requirements.txt /fibonaci_api

# Install required packages
RUN pip install -r requirements.txt

# Copy direcory contents to container
COPY . /fibonaci_api