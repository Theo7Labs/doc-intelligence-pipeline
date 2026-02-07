# Theo7 Doc Intelligence

🔗 **Live Demo:** [theo7-docai.lovable.app](https://theo7-docai.lovable.app)

AI-powered document analysis platform that automatically extracts insights from PDFs using generative AI.

## Features
- Upload PDFs via drag-and-drop
- AI-generated summaries and key points
- Serverless architecture (scales automatically)
- Real-time document processing

## Tech Stack
- **Frontend:** React (Lovable)
- **Backend:** AWS Lambda, API Gateway
- **AI:** Amazon Bedrock (Claude)
- **Storage:** S3, DynamoDB
- **Infrastructure:** AWS SAM / CloudFormation

## Architecture
```
PDF Upload → S3 → Lambda → Bedrock AI → DynamoDB → API → Frontend
```

## API Endpoints
- `GET /upload-url` - Get presigned URL for upload
- `GET /documents` - Retrieve processed documents

---
Built by [Theo7Labs](https://github.com/Theo7Labs)
