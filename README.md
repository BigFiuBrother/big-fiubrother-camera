# big-fiubrother-camera

Big fiubrother camera application for surveillance. This application is meant to run on a Raspberry PI.

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

```
python3 -m pip install -r requirements.txt
```

### Configuration

Before running, proper configuration should be considered. Default parameters for development are stored in *config/development.yml*.

### Run

```
./run.py
```