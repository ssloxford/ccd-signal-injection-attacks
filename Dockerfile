FROM ubuntu:18.04

RUN apt -y update && apt -y install python3-pip wget locales libxrender-dev libsm6 git sudo libboost-all-dev libusb-1.0-0-dev python-mako doxygen python-docutils cmake build-essential ffmpeg v4l-utils
ENV LANG C.UTF-8

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

WORKDIR /home

#### Install TIS ####
RUN git clone https://github.com/TheImagingSource/tiscamera.git && cd tiscamera && ./scripts/install-dependencies.sh --compilation --runtime --yes
RUN cd tiscamera && mkdir build && cd build && cmake -DBUILD_ARAVIS=ON .. && make && make install

ADD ./code /home/code
WORKDIR /home/code

### Install Pyhton Requirements and Jupyter ###
RUN pip3 install -r req
RUN pip3 install --upgrade jupyter
RUN pip3 install jupyterlab

#### Install UHD ####
RUN git clone https://github.com/EttusResearch/uhd.git && cd uhd/host && mkdir build && cd build && cmake -DENABLE_PYTHON_API=ON ../ && make && make test && make install && ldconfig
ENV PYTHONPATH "$PYTHONPATH:/usr/local/lib/python3/dist-packages"

### Patch USRP Python Library ###
RUN sed -i 's/sc16/sc8/g' /usr/local/lib/python3/dist-packages/uhd/usrp/multi_usrp.py

### Start Jupyter-lab 
CMD ["jupyter-lab", "--allow-root", "--ip=0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.password=''"]
