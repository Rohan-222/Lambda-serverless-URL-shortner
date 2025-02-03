# Serverless URL Shortener
![SERVERLESS URL SHORTNER](https://github.com/user-attachments/assets/f8c9a468-2f36-4b7f-9b09-231aad6280e7)

NOTE: 
1. You can Find the **Amazon Blog** for Build a Serverless, Private URL Shortener - [Here](https://aws.amazon.com/blogs/compute/build-a-serverless-private-url-shortener)
2. If You Like to **Build a serverless URL shortener app without AWS Lambda** Go to - [Amazon Blog Link](https://aws.amazon.com/blogs/compute/building-a-serverless-url-shortener-app-without-lambda-part-1)

This project demonstrates how to build a serverless URL shortener using AWS Lambda, API Gateway, and DynamoDB. It is designed to be beginner-friendly and includes step-by-step instructions for Windows users.

## Features
- Generate short codes for long URLs.
- Redirect users to the original URL using the short code.
- Fully serverless and scalable.

---

## Prerequisites
Before starting, ensure you have the following:
1. **AWS Account**: Sign up at [AWS Free Tier](https://aws.amazon.com/free/).
2. **AWS CLI**: Install and configure the AWS CLI on your Windows machine.
   - Download the AWS CLI installer from [here](https://aws.amazon.com/cli/).
   - Run the installer and follow the prompts.
   - Open **Command Prompt** or **PowerShell** and configure the AWS CLI:
     ```bash
     aws configure
     ```
     Enter your AWS Access Key, Secret Key, region, and output format when prompted.
3. **Python 3.x**: Install Python 3.x from [python.org](https://www.python.org/downloads/).
   - During installation, ensure you check the box to **Add Python to PATH**.
4. **Postman** (optional): Download and install Postman from [here](https://www.postman.com/downloads/) for testing the API.

---

## Step-by-Step Guide

### Step 1: Set Up DynamoDB Table
1. Open the **AWS Management Console** and navigate to **DynamoDB**.
2. Click **Create Table**.
   - **Table name**: `URLShortener`
   - **Partition key**: `short_code` (String)
3. Click **Create**.

---

### Step 2: Create the Lambda Function
1. Navigate to **AWS Lambda** in the AWS Management Console.
2. Click **Create Function**.
   - **Function name**: `URLShortenerFunction`
   - **Runtime**: Python 3.x
   - **Permissions**: Create a new role with basic Lambda permissions (AWS will automatically create a role).
3. Click **Create Function**.

---

### Step 3: Add Code to the Lambda Function
1. In the Lambda function editor, replace the default code with the provided Python code (see the `lambda_function.py` file in this repository).
2. **Deploy the function**.

---

### Step 4: Set Up API Gateway
1. Navigate to **API Gateway** in the AWS Management Console.
2. Click **Create API**.
   - Choose **HTTP API**.
   - Click **Build**.
3. **Add Routes**:
   - `POST /shorten` (for creating short URLs).
   - `GET /redirect` (for redirecting to the original URL).
4. **Integrate with Lambda**:
   - For each route, select the `URLShortenerFunction` Lambda function.
5. **Deploy the API**:
   - Click **Deploy**.
   - Create a new stage (e.g., `prod`).
6. **Note the API endpoint URL** (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod`).

---

### Step 5: Test the URL Shortener
#### Using Postman (Recommended for Windows)
1. **Create a Short URL**:
   - Open Postman.
   - Set the request type to `POST`.
   - Enter the URL: `https://<api-id>.execute-api.<region>.amazonaws.com/prod/shorten`.
   - Go to the **Body** tab, select **raw**, and choose **JSON**.
   - Add the following JSON payload:
     ```json
     {
       "long_url": "https://www.example.com"
     }
     ```
   - Click **Send**. You should receive a response with a `short_code`.

2. **Redirect to the Original URL**:
   - Set the request type to `GET`.
   - Enter the URL: `https://<api-id>.execute-api.<region>.amazonaws.com/prod/redirect?short_code=<short_code>`.
   - Click **Send**. You should be redirected to the original URL.

#### Using Command Prompt or PowerShell
1. **Create a Short URL**:
   ```bash
      Invoke-RestMethod -Uri "https://<api-id>.execute-api.<region>.amazonaws.com/prod/shorten" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"long_url": "https://www.example.com"}'

(Note: Use backticks ` for line continuation in PowerShell.)

2. **Redirect to the Original URL:**
   ```bash
   Invoke-RestMethod -Uri "https://<api-id>.execute-api.<region>.amazonaws.com/prod/redirect?short_code=<short_code>"
---

### Step 6: Clean Up
  1. Delete the DynamoDB table.
  2. Delete the Lambda function.
  3. Delete the API Gateway.
---

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Here’s how you can help:

- Add new features or improve existing ones.
- Write documentation or tutorials.
- Fix bugs or optimize the code.

## Support
If you have any questions or need help, feel free to open an issue in this repository. or If you found some errors you can give the updates.
