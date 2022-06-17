# big-fiubrother-camera

Big Fiubrother camera application for surveillance.
This application is meant to run on a Raspberry PI but it can also run on any computer with a webcam.

### Prerequisites

- python3
- Raspberry PI with PiCamera


### Install

In order to install big-fiubrother-camera, a virtual environment is recommended. This can be achieved executing:

```bash
python3 -m venv big-fiubrother-camera-venv
source big-fiubrother-camera-venv/bin/activate

# Install opencv dependencies for Raspberry PI
sudo apt install -y libqtgui4 libqt4-test libjasper
```
Now, to install all the dependencies, execute the following script: 

```bash
python3 -m pip install -r requirements.txt
```

### Configuration

Before running, proper configuration should be considered. Default parameters for development are stored in *config/development.yml*.

### Run

```bash
./run.py
```

### Development

The Big Fiubrother camera consists of three tasks that are running concurrently in separate threads:

```
+--------------+     +--------------------+     +--------------------------------+
| Record video | --> | Upload video chunk | --> | Publish Video Processing Event |
+--------------+     +--------------------+     +--------------------------------+
```

1) First task records a short video into a local file.
2) Second task uploads the video chunk into a file storage (e.g. S3).
3) Third task publish an event to start the video processing pipeline.