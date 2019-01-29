# Machine learning model deployment as web app with Flask and Docker

This repo serves as an accompaniment to the Pivigo S2DS blog post on how to deploy a machine learning model using a web app using Flask and Docker.

The code in this repo is kept at minimum in interests of brevity, as well as to aid readability for people new to Flask and Docker. Do not consider the project and code layout as an exemplerary example, but rather as a simple starting point to learn the tools. 

## Usage
The repo is intended to be run as a Docker container using the provided `Dockerfile`.  To build the container, run:

```bash
docker build . -t <<container_name>>
```

Once built, the container can be launched as follows:

```bash
docker run -it -p 5000:5000 <<container_name>>
```