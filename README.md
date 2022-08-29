# Diffusion Test

This project is a proof of concept to use diffusers to generate images from text recognition.

The diffuser used on this test can be found at https://huggingface.co/CompVis/stable-diffusion-v1-4

## Requirements

- Python 3.x installed
- Unix system or Windows with admin privileges
- Account in HuggingFaces
- Accept the License requirements.
- ~10 GB of free space in HDD

## How to prepare environment

The following steps are designed for an UNIX environment, may differ from the steps required on a windows OS

In order to use this, it is recommended to use virtualenv and generate a virtual env for this application

```bash
pip install virtualenv
virtualenv local 
sources local/Scripts/activate
```

Once this is done, you need to install the dependencies of the project, a `requirements.txt` has been built to ease this task.

NOTE: this will install the Cuda 11.3 version of the library

```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu113
```

## How to use

Simply run the main script with the command

```bash
python main.py
```
