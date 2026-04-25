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

- `GET /upload-url` — Get presigned URL for upload
- `GET /documents` — Retrieve processed documents

## Security

This repo is configured to keep secrets out of source control.

- **Pre-commit hook:** [gitleaks](https://github.com/gitleaks/gitleaks) v8.21.2 runs on every commit and blocks anything containing detected secrets.
- **`.env.example` template** documents the required environment variables (`TABLE_NAME`, `BUCKET_NAME`, `AWS_SAM_STACK_NAME`). Actual `.env` files are gitignored and never committed.
- **Hardened `.gitignore`** covers credentials, `*.pem`, `*.key`, AWS config files, and `.aws-sam` build artifacts.

**Setup for new contributors:**

```bash
pip install pre-commit
python -m pre_commit install
```

Verify the hook is active:

```bash
python -m pre_commit run gitleaks --all-files
```

---

Built by **[Theo7Labs](https://github.com/Theo7Labs)**
