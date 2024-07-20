# line-mapping

## Installation

**Install the dependencies as follows:**
* CMake >= 3.17
* COLMAP 3.8 [[the official guide](https://colmap.github.io/install.html)] _make sure to use the tag 3.8_
* PoseLib [[Guide](misc/install/poselib.md)]
* HDF5
```bash
sudo apt-get install libhdf5-dev
```
* Python 3.9 + required packages
```bash
git submodule update --init --recursive

# Refer to https://pytorch.org/get-started/previous-versions/ to install pytorch compatible with your CUDA
python -m pip install torch==1.12.0 torchvision==0.13.0 
python -m pip install -r requirements.txt
```

To install:
```
python -m pip install -Ive . 
```
To double check if the package is successfully installed:
```
python -c "import limap"
```
