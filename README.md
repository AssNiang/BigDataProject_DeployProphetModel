# ML model Deployment with FastAPI, and Docker

### 1. Develop and save the model with this Colab

[Open Colab -- Prophet_Model](https://colab.research.google.com/drive/11QbRxPFI6g0KTQNbwmSIIilQ0HwELWCT?usp=sharing)

### 2. Create Docker container

```bash
docker build -t predict-temp .

docker run -d --name predict-temp-container -p 80:80 predict-temp
```

### 3. Save the project in a Git repo

If you clone this repo this step is not needed. Or you can delete this git repo with `rm -rf .git` and start with a new one:

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/AssNiang/BigDataProject_DeployProphetModel.git
git push -u origin main
```

