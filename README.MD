# Project Setup and Deployment Guide

This guide will help you set up the project locally and push it to the Snowflake Container Service.

## Prerequisites

- Docker installed on your machine.
- Access to Snowflake Container Service.

## Steps to Run the Project Locally and Deploy

### Step 1: Set Up Environment

1. Copy the `env.example` file in the root directory.
2. Rename it to `.env`.
3. Fill in all your credentials in the `.env` file.

### Step 2: Build the Docker Image

Run the following command to build your Docker image without using cache:

```bash
docker build --no-cache -t <APP_NAME> .
```

### Step 3: Login to Snowflake Container Service

```bash
docker login <SNOWFLAKE_IMAGE_REPO> -u <SNOWFLAKE_USERNAME>
```
example: docker login vdbyyxh-ly00649.registry.snowflakecomputing.com/snowflake/public/my_repo -u Virakpech

### Step 4: Tag the Docker Image
After a successful login, tag your image:

```bash
docker tag <APP_NAME>:latest <SNOWFLAKE_IMAGE_REPO>/<APP_NAME>:latest
```

### Step 5: Push the Docker Image
Push the tagged image to the Snowflake Container Service:
```bash
docker push <SNOWFLAKE_IMAGE_REPO>/<APP_NAME>:latest
```

### Running Locally
If you want to run the application locally, use this command:
```bash
docker run -p 8501:8501 <APP_NAME>
```