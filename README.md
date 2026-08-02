# Azure DevOps Data Science Project

## Project Overview

This project demonstrates an end-to-end deployment of a Machine Learning application on Microsoft Azure using modern DevOps practices.

The application performs customer segmentation using the K-Means clustering algorithm, stores the prediction results in Azure SQL Database, and is deployed on Azure Kubernetes Service (AKS) using Docker containers stored in Azure Container Registry (ACR).

---

## Architecture

```
GitHub
   │
   ▼
Docker Build
   │
   ▼
Azure Container Registry (ACR)
   │
   ▼
Azure Kubernetes Service (AKS)
   │
   ▼
Flask Application
   │
   ▼
Azure SQL Database
```

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- Docker
- Kubernetes
- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Azure SQL Database
- Azure CLI
- Git & GitHub

---

## Features

- Customer segmentation using K-Means
- Stores prediction results in Azure SQL Database
- Dockerized Python application
- Deployed on AKS
- Kubernetes Deployment and LoadBalancer Service
- Version controlled using GitHub

---

## Project Structure

```
azure-devops-datascience/
│
├── Dockerfile
├── README.md
├── hello.py
├── kmeans.py
├── requirements.txt
├── config.py.example
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── .gitignore
```

---

## Docker

Build image

```bash
docker build -t retail-ml-app .
```

Run container

```bash
docker run -p 5000:5000 retail-ml-app
```

---

## Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check pods

```bash
kubectl get pods
```

Check services

```bash
kubectl get svc
```

---

## Azure Services Used

- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Azure SQL Database

---

## Security

Sensitive credentials are excluded from version control.

Create a `config.py` file using the provided `config.py.example` template before running the application.

---

## Future Enhancements

- Azure DevOps CI/CD Pipeline
- GitHub Actions
- Azure Key Vault integration
- Monitoring using Azure Monitor
- Horizontal Pod Autoscaling

---

## Author

**Anushka Suryawanshi**

Azure DevOps | Azure | Docker | Kubernetes | Terraform | Jenkins