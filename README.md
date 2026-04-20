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
Add a "Security" section to README.md documenting our secret scanning setup. Include:

- Pre-commit hook with gitleaks v8.21.2 that blocks any commit containing secrets
- .env.example template showing required environment variables (TABLE_NAME, BUCKET_NAME, AWS_SAM_STACK_NAME) — actual .env files are gitignored
- Hardened .gitignore covering credentials, *.pem, *.key, AWS config files, and .aws-sam build artifacts
- Setup instructions for new contributors:
  1. pip install pre-commit
  2. python -m pre_commit install
  3. Verify with: python -m pre_commit run gitleaks --all-files

Keep it concise — under a ## Security header. Place it after any existing setup/installation sections.
