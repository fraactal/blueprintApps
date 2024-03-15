FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get install -y python3-pip 
    #python-dev

WORKDIR /app

#copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

#prepare environment for flask mysql connector
RUN apt-get install -y libmysqlclient-dev

#install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

#RUN pip install flask 
#RUN pip install virtualenv 
#RUN pip install flask-mysqldb

##Asi funciona hasta antes del test
COPY src /app/src
COPY templates /app/templates

#configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["/app/src/app.py" ]
