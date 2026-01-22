# Serverless Task Management API

A cloud-native, serverless REST API for managing tasks, built using **AWS Lambda**, **API Gateway**, **DynamoDB**, and **GitHub Actions CI/CD**.

This project demonstrates modern backend and cloud engineering fundamentals, including serverless architecture, secure IAM usage, and automated deployment pipelines.

---

## 🚀 Features

- Create, read, update, and delete tasks (CRUD)  
- Fully serverless backend (no servers to manage)  
- Stateless API design  
- Persistent storage using DynamoDB  
- Automated CI/CD pipeline with GitHub Actions  
- Deployed and accessible via AWS API Gateway  

---

## 🏗 Architecture

Client (curl / Postman)
|
| HTTP (REST)
v
API Gateway
|
v
AWS Lambda (Python)
|
| IAM Role (least privilege)
v
DynamoDB (Tasks table)

yaml
Copy code

---

## 🧠 Key Design Decisions

### Why Serverless (Lambda)?
- No server management or scaling concerns  
- Pay only for execution time  
- Ideal for event-driven APIs and microservices  

### Why DynamoDB?
- Fully managed NoSQL database  
- Scales automatically  
- Low latency for key-value access  
- Simple data model fits task storage well  

### Why API Gateway?
- Native AWS integration with Lambda  
- Handles routing, HTTP methods, and request lifecycle  
- Public REST endpoint without custom servers  

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** to automatically deploy code on every push to `main`.

Pipeline steps:  
1. Checkout repository  
2. Package Lambda source code into a ZIP file  
3. Deploy ZIP to AWS Lambda using secure credentials  

Benefits:  
- No manual deployments  
- Consistent production builds  
- Faster iteration and safer changes  

---

## 📦 API Endpoints

**Create a Task**
```
curl -X POST https://<api-url>/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task"}'
```

**Get All Tasks**
```
curl https://<api-url>/tasks
```

**Update Tasks**
```
curl -X PUT https://<api-url>/tasks \
  -H "Content-Type: application/json" \
  -d '{"task_id": "<TASK_ID>", "completed": true}'
```

**Delete All Tasks**
```
curl -X DELETE https://<api-url>/tasks?task_id=<TASK_ID>
```
🔐 Security

Lambda executes using an IAM role with least-privilege permissions

No credentials are hardcoded

AWS credentials are securely stored as GitHub Secrets

Public API access controlled at the API Gateway level

🧪 Local Testing

Core logic can be tested locally by invoking the Lambda handler directly with simulated API Gateway events.
This enables fast iteration before deploying to the cloud.

📈 Future Improvements

Add authentication (Cognito / JWT)

Pagination for large task lists

Input validation and schema enforcement

Infrastructure as Code (Terraform or AWS CDK)

Rate limiting and monitoring enhancements

📌 What This Project Demonstrates

Cloud-native backend design

Serverless application development

REST API engineering

AWS IAM and security fundamentals

CI/CD automation

Production-style deployment workflows

🧑‍💻 Author

Sahil Nambiar
Computer Science @ Purdue University
