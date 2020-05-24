FROM ubuntu
# RUN groupadd -g 999 appuser && \
#     useradd -r -u 999 -g appuser appuser

RUN apt update
RUN apt-get install fish sudo -y


RUN adduser --disabled-password --gecos "" somedudeuser
RUN adduser somedudeuser sudo

RUN echo 'root:rootpass' | chpasswd
RUN echo 'somedudeuser:mypass' | chpasswd

USER somedudeuser
CMD echo $HOME