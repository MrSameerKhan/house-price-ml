house-price-ml/
├── train.py
├── predict.py
├── model.pkl
└── requirements.txt


1.train.py
2.predict.py
3.requirements.txt
4.Test Locally


Move code to github
1. Intialize github
git init
git add .
git commit -m "Initial ML project"
2. Create github repo
3. Push to github
git branch -M main
git remote add origin https://github.com/<your-username>/house-price-ml.git
git push -u origin main



Dockerize the Project
1. Create Dockerfile

| Line      | Meaning                     |
| --------- | --------------------------- |
| `FROM`    | Base OS + Python            |
| `WORKDIR` | Container working directory |
| `COPY`    | Moves files into image      |
| `RUN`     | Executes at **build time**  |
| `CMD`     | Executes at **runtime**     |

2. Build Docker image
docker build -t house-price-ml .

3. Run training inside container
docker run house-price-ml

4. Persist Model
model.pkl lives inside container
Container exits → model is gone
docker run -v $(pwd):/app house-price-ml

5. Run Prediction via Docker
docker build -t house-price-ml .
docker run -v $(pwd):/app house-price-ml

Model You Just Built
| Layer      | You learned              |
| ---------- | ------------------------ |
| Python     | Core ML logic            |
| GitHub     | Source control           |
| Dockerfile | Reproducibility          |
| Image      | Immutable ML environment |
| Container  | Execution                |
| Volume     | Model persistence        |



STEP 1 — Create FastAPI App
Inside your project, create a new file: app.py
STEP 2 — Run FastAPI Locally (Without Docker)
pip install fastapi uvicorn #install dependencies
uvicorn app:app --reload. #Run server:
http://127.0.0.1:8000 #open browser
http://127.0.0.1:8000/docs #docs
This auto-generated Swagger UI is why FastAPI is loved in production.
STEP 3 — Update requirements.txt
STEP 4 — Dockerize FastAPI (Critical Step)
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
This turns your ML model into a deployable service.
STEP 5 — Build & Run Docker Image
Build: docker build -t house-price-api .
Run: docker run -p 8000:8000 house-price-api
http://localhost:8000/docs
You now have a containerized ML API.
STEP 6 — Test Like a Real System
curl -X POST "http://localhost:8000/predict?area=1000"
Or via Swagger UI:
Open /docs
Click POST /predict
Try it out
