# Signal Injection Attacks against CCD Image Sensors

<p align="center"><img src="https://via.placeholder.com/700X200" width="100%"><em style="color: grey">Fig. 1: Text injected into an otherwise empty frame.</em></p>

This repository contains the evaluation source code used in our paper [**Signal Injection Attacks against CCD Image Sensors**](https://arxiv.org/).

The paper presents a novel post-transducer signal injection attack against CCD image sensors using electromagnetic emanation.
We show that it is possible to manipulate the image information captured by a CCD image sensor with the granularity down to the brightness of individual pixels.
An example of the signal injection attack is given in Figure 1 above. 
The text "Welcome!" was injected into an otherwise empty frame.

<p align="center"><img src="https://via.placeholder.com/700X200" width="75%"><br><em style="color: grey">Fig. 2: Illustration of a readout of the generated signal charge from a CCD image sensor under the presence of an attack signal.</em></p>

## Structure of the Repository
This repository is organized as follows:

```
.                                         # root directory of the repository
├── code                                  # contains the evaluation source code
│   ├── data                              # persistent directory in which the evaluation results will be stored
│   ├── doc                               # different files used for the documentation
│   ├── lib                               # various Python classes required for the evaluation
│   │   │── AttackSetting.py              # Python class that defines the different attack settings
│   │   │── BarcodeScanResult.py          # Python class that represents the results of a barcode scan
│   │   │── EvaluationUtils.py            # Python class that implements various utils required for the evaluation
│   │   │── ImageMetrics.py               # Python class that represents the different various image metrics
│   │   │── SignalEmitter.py              # Python class that provides an abstracted API to control an ETTUS Research USRP
│   │   └── TIS                           # library to interact with cameras from the manufacturer The Imaging Source
│   ├── notebooks                         # all Jupyter Notebooks necessary to run the evaluation
│   │   │── Barcode Scanner.ipynb         # Jupyter Notebook implementing the Barcode Scanner Evaluation
│   │   │── Calculate Image Metrics.ipynb # Jupyter Notebook implementing the Image Metrics calculation
│   │   │── End-2-End Attack.ipynb        # Jupyter Notebook implementing the and end-2-end attack
│   │   └── Frequency Sweep.ipynb         # Jupyter Notebook implementing the Frequency Sweep to find the resonant frequency
│   ├── req                               # text file that contains all the Python requirements
│   └── scripts                           # directory that contains additional evaluation scripts
│       └── end-2-end_attack.py           # same code as in the notebook, just in the form of a script
├── docker-compose.yml                    # configuration file of the Docker container
├── Dockerfile                            # Build instructions for the Docker container
└── README.md                             # this README file
```

## Detailed Overview

As can be seen in the directory tree above, the source code is divided across four Jupyter Notebooks.
In the following, we give a brief overview of the different functionalities of each Notebook.

#### Barcode Scanner

This Jupyter Notebook defines all methods required to evaluate the performance of a Barcode Scanner under the presence of a signal injection attack.
First, a predefined number of frames from a *The Imaging Source* camera, such as the DFM25G445 used in our evaluation, for different exposure and gain settings are captured.
Second, the frames are analyzed for barcodes and the results are stored in a CSV file.


<table align="center"><tr>
<td> 
  <p align="center">
    <img alt="Forwarding" src="https://via.placeholder.com/700X200" width="300">
    <br>
    <em style="color: grey">a) Normal operation</em>
  </p> 
</td>
<td> 
  <p align="center">
    <img alt="Routing" src="https://via.placeholder.com/700X200" width="300">
    <br>
    <em style="color: grey">b) Under attack</em>
  </p> 

</td>
</tr></table>
 <p align="center"><em align="center">Fig. 3: Frames captured during normal operation of the barcode scanner and while an attack signal was emitted.</em></p>

#### Calculate Image Metrics

This Jupyter Notebook calculates different image quality metrics for frame pairs. It is used to analyze the frames captured during the frequency sweep to find the resontant frequency of a CCD image sensor.

#### End-2-End Attack

This Jupyter Notebook implements an End-2-End attack pipeline. It takes an input image, extracts the Luma Y for each pixel, interpolates the extracted symbols, and emits the signal at a predefined carrier frequency.

<p align="center"><img src="https://via.placeholder.com/700X200" width="90%"><br><em style="color: grey">Fig. 4: End-2-End representation of the signal injection attack.</em></p>

#### Frequency Sweep

This Jupyter Notebook executes a frequency sweep. It provides predefined methods that enable the collection of frames for the four tested cameras: DFM25G445, analog CCD board camera, Axis MV3045, and Logitech C922.

## Running the Evaluation Source Code
This repository contains all configuration and source code files necessary to run the attack presented in the paper.
To ensure a quick and easy deployment, we provide a Dockerfile to build a container with all the required dependencies.
<br>**Please note**, to use this repository, you will need `docker` and `docker-compose`.

The following steps outline how to build and run the Docker container:

 * `git clone https://github.com/ssloxford/ccd_signal_injection.git`
 * `cd ccd_signal_injection/`
 * `docker-compose build`
 * `docker-compose up -d`

Once the Docker container is up and running, `jupyter-lab` is listening on `localhost` and port `8888`.
You can now access the notebook via a browser at `localhost:8888`.

## Recommended Equipment

To ensure that the evaluation can be replicated without issues, we recommend the following equippment.

 * A software-defined radio with a maximum sample rate >= 25MSPS
 * A PC with the following minimum specifications:
    * Intel Core i7-7700K @ 4.20GHz or equivalent
    * 16GB RAM
    * 50GB free disk space
    * Ubuntu 18.04 or higher
 * An RF shielded box to prevent interference with and from other devices

## Contributors
 * [Sebastian Köhler](https://cs.ox.ac.uk/people/sebastian.kohler)
 * [Richard Baker](https://www.cs.ox.ac.uk/people/richard.baker/)
