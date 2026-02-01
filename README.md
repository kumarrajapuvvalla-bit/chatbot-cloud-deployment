# Cloud Chatbot Deployment

This project demonstrates how to design, containerise, and deploy a simple
chatbot application to a cloud‑native environment.  It provides a
baseline that you can extend with additional natural language
processing capabilities or integrate with platform services such as
Amazon Lex or Azure Cognitive Services.  The repository contains:

- A Python Flask application (`app/main.py`) implementing a basic
  chatbot API.
- A `Dockerfile` to build a container image.
- Kubernetes manifests for deploying the chatbot to a cluster.
- Terraform configuration for provisioning an Amazon ECR repository and
  an Amazon EKS cluster.
- An architecture diagram illustrating the overall solution.

## Architecture

The chatbot runs as a container within a Kubernetes cluster.  A load
balancer routes external HTTP requests to the service, which forwards
traffic to the underlying pods.  The container image is stored in
Amazon ECR, and the infrastructure is provisioned using Terraform.

![Architecture](diagrams/architecture.png)

## Features

* **Lightweight chatbot** – responds to basic greetings and help
  requests; the logic can be extended to call a pre‑trained model or
  third‑party API.
* **Containerised deployment** – the application is packaged into a
  Docker image for portability across environments.
* **Infrastructure as Code** – Terraform scripts provision an ECR
  repository and an EKS cluster using the official AWS modules.
* **Kubernetes manifests** – includes a `Deployment` for running
  replicas and a `Service` exposing the chatbot through a load
  balancer.
* **Extensible pipeline** – you can add a GitHub Actions or Jenkins
  workflow to build and push the container image automatically to
  ECR/EKS.

## Getting Started

### Prerequisites

* **Docker** – to build and run the container locally.
* **Python 3.9+** – if you want to run the application without
  containerisation.
* **kubectl** and a Kubernetes cluster – to deploy the manifests.  You
  can create a cluster using EKS, AKS, or Minikube for local
  development.
* **Terraform** – if you plan to provision AWS resources.

### Running Locally

To test the chatbot without deploying it to the cloud:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py

# In another terminal, send a request:
curl -X POST -H "Content-Type: application/json" \
     -d '{"message": "hello"}' http://localhost:8080/chat
```

### Building the Docker Image

```bash
docker build -t chatbot:latest .
docker run -p 8080:8080 chatbot:latest
```

### Deploying to Kubernetes

1. Push the built image to a container registry (for example, Amazon
   ECR) and update the `image` field in `k8s/deployment.yaml`.
2. Apply the manifests:

   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

3. Retrieve the service’s external IP and test the endpoint.

### Provisioning AWS Resources with Terraform

The `terraform` directory contains a sample configuration that
provisions an ECR repository and an EKS cluster using the
`terraform-aws-modules/eks` module.  Before running Terraform you
should customise the variables (VPC ID, subnets, cluster name) in
`terraform/variables.tf` or by providing a `terraform.tfvars` file.

```bash
cd terraform
terraform init
terraform plan -out plan.tfplan
terraform apply plan.tfplan
```

Outputs will display the repository URL and cluster ID.  You can use
`aws eks update-kubeconfig --name <cluster-name>` to configure
`kubectl` to communicate with the new cluster.

## Extending This Project

The current implementation is intentionally simple.  To showcase your
DevOps skills you might:

* Integrate a pre‑trained language model from Hugging Face or Azure
  OpenAI and store weights in a secure location (for example, S3 or
  Azure Blob Storage).
* Build a CI/CD pipeline using Jenkins or GitHub Actions that
  automatically builds the Docker image, scans for vulnerabilities,
  pushes it to ECR, and deploys to EKS via `kubectl` or Helm.
* Replace the Kubernetes manifests with Helm charts and implement
  GitOps deployment using Argo CD.
* Add monitoring and logging using Prometheus and Grafana or Amazon
  CloudWatch.

By following these practices you demonstrate proficiency in cloud
infrastructure, container orchestration, and automation.
