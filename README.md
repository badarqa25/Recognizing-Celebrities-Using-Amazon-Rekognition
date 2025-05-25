# Celebrity Image Recognition using AWS Lambda & S3

This project uses AWS Lambda and Amazon Rekognition to detect celebrities in images uploaded to an S3 bucket named `celebrityuploadsbybadarqa`.

## 🧠 Overview

Whenever a new image is uploaded to the `celebrityuploadsbybadarqa` S3 bucket, a Lambda function is triggered to:
- Analyze the image using AWS Rekognition.
- Detect if any known celebrities are in the image.
- Log the result to CloudWatch or send the data to another service (e.g., DynamoDB, SNS, etc.).

## 🗂️ Bucket: `celebrityuploadsbybadarqa`

### Purpose:
Stores uploaded images for celebrity recognition processing.

### Requirements:
- The bucket must have the correct event trigger configuration to invoke the Lambda function on `ObjectCreated` events.

## ⚙️ Lambda Function

### Trigger:
- **S3 Event:** On image upload (ObjectCreated).

### Actions:
1. Retrieve the image from S3.
2. Use `Rekognition.detect_celebrities()` to identify any celebrities.
3. Log results or send to another AWS service for storage/display.

### Required IAM Permissions:
- `s3:GetObject`
- `rekognition:RecognizeCelebrities`
- `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents`

## 📦 Project Structure

celebrity-recognition/
│
├── lambda_function.py # Main handler for processing uploaded images
├── requirements.txt # Python dependencies (e.g., boto3)
└── README.md # Project documentation
