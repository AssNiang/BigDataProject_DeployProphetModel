# ML model Deployment with FastAPI, and Docker

### 1. Develop and save the model with this Colab

[Open Colab -- Prophet_Model](https://colab.research.google.com/drive/11QbRxPFI6g0KTQNbwmSIIilQ0HwELWCT?usp=sharing)

### 2. Create Docker container

```bash
docker build -t predict-temp .

docker run -d --name predict-temp-container -p 80:80 predict-temp
```

### 3. Save the Docker image in Dockerhub

```bash
docker tag predict-temp sas792/predict-temp

docker push sas792/predict-temp
```

### 4. Download and Run the Docker image from Dockerhub

```bash
docker pull sas792/predict-temp

docker run -d --name predict-temp-container -p 80:80 sas792/predict-temp
```

### 5. Access the API

[API / home](http://localhost:80)

[API / docs](http://localhost:80/docs)

[API / predict next 3 hours temperature](http://localhost:80/predict-next-3-hours-temp)


### 6. Save the project in Github

If you clone this repo this step is not needed. Or you can delete this git repo with `rm -rf .git` and start with a new one:

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/AssNiang/BigDataProject_DeployProphetModel.git
git push -u origin main
```

[Open Github](https://github.com/AssNiang/BigDataProject_DeployProphetModel.git)

### 7. Clone the project from Github

```bash
git clone https://github.com/AssNiang/BigDataProject_DeployProphetModel.git
```

### 8. Sources

[https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/]

[https://fastapi.tiangolo.com/deployment/docker/]

[https://www.youtube.com/watch?v=h5wLuVDr0oc]

[https://dev.meteostat.net/]