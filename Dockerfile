FROM ubuntu

RUN apt update
RUN apt-get install fish sudo curl -y


RUN adduser --disabled-password --gecos "" somedudeuser
RUN adduser somedudeuser sudo

RUN echo 'root:rootpass' | chpasswd
RUN echo 'somedudeuser:mypass' | chpasswd

USER somedudeuser

WORKDIR /home/somedudeuser

CMD echo $HOME