# AI Document Intelligence Pipeline - Final Project Documentation

**Project Completed:** February 1, 2026  
**Developer:** Theo  
**Stack:** AWS Serverless (S3, Lambda, Bedrock, DynamoDB)  
**Status:** ✅ Fully Deployed and Working

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI DOCUMENT INTELLIGENCE PIPELINE                        │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌──────────┐         ┌──────────┐         ┌──────────┐         ┌──────────┐
     │          │         │          │         │          │         │          │
     │    S3    │────────▶│  LAMBDA  │────────▶│ BEDROCK  │────────▶│ DYNAMODB │
     │  BUCKET  │ trigger │ FUNCTION │  call   │ (Claude) │  store  │  TABLE   │
     │          │         │          │         │          │         │          │
     └──────────┘         └──────────┘         └──────────┘         └──────────┘
          │                    │                    │                    │
          │                    │                    │                    │
     Upload PDF          Process &            AI Analyzes          Results
     (.pdf files)        Orchestrate          Document             Stored
```

---

## Data Flow - What Happens When You Upload a PDF

```
STEP 1: UPLOAD
────────────────
User uploads PDF to S3 bucket
    │
    ▼
┌─────────────────────────────────────┐
│  S3 Bucket                          │
│  doc-intelligence-pipeline-documents│
│  ┌─────────────────┐                │
│  │ document.pdf    │                │
│  └─────────────────┘                │
└─────────────────────────────────────┘
    │
    │ S3 Event Notification (automatic trigger)
    ▼

STEP 2: TRIGGER
────────────────
Lambda function automatically invoked
    │
    ▼
┌─────────────────────────────────────┐
│  Lambda Function                    │
│  - Downloads PDF from S3            │
│  - Extracts text content            │
│  - Prepares prompt for AI           │
└─────────────────────────────────────┘
    │
    │ API Call to Bedrock
    ▼

STEP 3: AI PROCESSING
────────────────────────
Bedrock (Claude) analyzes the document
    │
    ▼
┌─────────────────────────────────────┐
│  Amazon Bedrock                     │
│  - Receives document text           │
│  - Claude AI processes content      │
│  - Returns structured analysis:     │
│    • Summary                        │
│    • Key points                     │
│    • Extracted data                 │
└─────────────────────────────────────┘
    │
    │ AI Response
    ▼

STEP 4: STORAGE
────────────────
Results saved to DynamoDB
    │
    ▼
┌─────────────────────────────────────┐
│  DynamoDB Table                     │
│  ┌────────────────────────────────┐ │
│  │ document_id: "doc_123"         │ │
│  │ file_name: "contract.pdf"      │ │
│  │ file_size: 1048576             │ │
│  │ extracted_data: {              │ │
│  │   "summary": "...",            │ │
│  │   "key_points": [...],         │ │
│  │   "entities": [...]            │ │
│  │ }                              │ │
│  │ processed_at: "2026-02-01..."  │ │
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘

DONE! Document processed automatically.
```

---

## Component Breakdown

### 1. Amazon S3 (Simple Storage Service)
**What it does:** Stores the uploaded PDF files  
**Why we use it:** Scalable, cheap storage that can trigger events  
**Key feature:** Event notifications automatically trigger Lambda when files are uploaded

### 2. AWS Lambda
**What it does:** Runs our Python code without managing servers  
**Why we use it:** Pay only when code runs, scales automatically  
**Key feature:** Serverless - no EC2 instances to manage

### 3. Amazon Bedrock (Claude AI)
**What it does:** AI that reads and understands the document  
**Why we use it:** Managed AI service, no ML expertise needed  
**Key feature:** Access to Claude and other foundation models via API

### 4. Amazon DynamoDB
**What it does:** Stores the processed results  
**Why we use it:** Fast, scalable NoSQL database, serverless  
**Key feature:** Pay-per-request pricing, no capacity planning

---

## What Makes This Different From Using ChatGPT Manually

| Manual AI (ChatGPT/Claude) | Automated Pipeline |
|---------------------------|-------------------|
| Upload one document at a time | Drop 1000 PDFs, walk away |
| Copy/paste results manually | Results auto-saved to database |
| You have to be there | Runs 24/7 without you |
| No searchable history | All results queryable |
| Consumer tool | Engineering solution |

**The key insight:** Anyone can use ChatGPT. Building an automated pipeline that processes documents at scale is a cloud engineering skill.

---

## Technical Specifications

### Infrastructure (template.yaml)
- **Runtime:** Python 3.11
- **Timeout:** 60 seconds
- **Memory:** Default (128MB)
- **Architecture:** x86_64
- **Tracing:** AWS X-Ray enabled

### IAM Permissions
- S3: Read access to documents bucket
- DynamoDB: Full CRUD on processed-documents table
- Bedrock: InvokeModel permission

### Event Trigger
- Type: S3 ObjectCreated
- Filter: `.pdf` suffix only

---

## Project Structure

```
doc-intelligence-pipeline/
├── hello_world/
│   └── app.py                    # Lambda function (124 lines)
├── template.yaml                 # Infrastructure as Code
├── samconfig.toml               # Deployment configuration
├── Notebooklm_documentation/    # Project documentation
│   ├── PHASE-2-HANDOFF.md
│   ├── Phase-4-Lambda-Function-Development.md
│   ├── Phase-5-YAML-Indentation-Fix.md
│   └── Phase-6-Python-Runtime-Mismatch.md
└── .git/                        # Version control
```

---

## Git Commit History

```
Commit 8: Phase 6 complete - Pipeline tested and working
Commit 7: Add environment variables and IAM permissions to Lambda function
Commit 6: Add Lambda function with Bedrock and DynamoDB integration
Commit 5: Complete Phase 3 infrastructure
Commit 4: Add DynamoDB table
Commit 3: Add S3 bucket
Commit 2: Enable X-Ray tracing
Commit 1: Initial project setup
```

---

## Challenges Overcome

### 1. YAML Indentation (Phase 5)
**Problem:** `Environment` and `Policies` were outside `Properties` block  
**Error:** "property Variables not defined for resource"  
**Root cause:** YAML indentation determines structure - wrong spaces = wrong meaning  
**Solution:** Claude generated corrected file with proper nesting  
**Lesson:** YAML is syntactically valid but semantically wrong - VS Code won't catch it, `sam validate` will

### 2. Python Version Mismatch (Phase 6)
**Problem:** Template specified Python 3.13, local machine had 3.11  
**Error:** "Binary validation failed for python"  
**Root cause:** `sam build` needs matching Python version locally  
**Solution:** Changed `Runtime: python3.13` to `Runtime: python3.11`  
**Lesson:** `sam validate` checks YAML structure, `sam build` actually uses Python

### 3. Double File Extension (Phase 6)
**Problem:** File was named `template.yaml.yaml`  
**Error:** "Template file not found"  
**Root cause:** Windows hides extensions, so saving as "template.yaml" added another .yaml  
**Solution:** `Rename-Item "template.yaml.yaml" "template.yaml"`  
**Lesson:** Use `dir` command to see actual filenames

### 4. S3 Trigger Not Connecting (Phase 6)
**Problem:** Uploading PDF didn't trigger Lambda  
**Root cause:** S3 event notification wasn't configured despite being in template  
**Solution:** Manually added trigger via AWS Console  
**Lesson:** Always verify triggers are connected after deployment

### 5. Wrong File Type Uploaded (Phase 6)
**Problem:** Uploaded PNG instead of PDF  
**Root cause:** Trigger filtered for `.pdf` suffix only  
**Solution:** Upload actual PDF file  
**Lesson:** Triggers can filter by file type - check your filter settings

---

## Interview Talking Points

### "Tell me about a project you've built"

> "I built an AI document intelligence pipeline on AWS. When you upload a PDF to an S3 bucket, it automatically triggers a Lambda function that sends the document to Amazon Bedrock - which uses Claude AI - to analyze the content. The extracted insights are then stored in DynamoDB. The entire thing is serverless and event-driven, so it scales automatically and I only pay when documents are processed."

### "What challenges did you face?"

> "The trickiest part was YAML configuration. I had an indentation error that passed syntax validation but failed semantically - the properties were at the wrong nesting level. It taught me that infrastructure-as-code requires precision, and that validation tools check different things. I also hit a Python version mismatch between my local environment and the Lambda runtime, which taught me the difference between template validation and actual builds."

### "Why serverless instead of EC2?"

> "For this use case, serverless makes more sense. The workload is event-driven and bursty - documents come in unpredictably. With Lambda, I pay per invocation instead of keeping a server running 24/7. It also scales automatically - if someone uploads 100 PDFs at once, Lambda handles it without me configuring auto-scaling groups."

### "How would you improve this?"

> "Three things: First, add a frontend so users can upload documents through a web interface instead of the AWS Console. Second, add search functionality so you can query across all processed documents. Third, implement multi-region deployment for high availability - right now it's single-region, so if us-east-1 goes down, the service goes down."

### "What's the difference between this and just using ChatGPT?"

> "ChatGPT is manual - you upload one document, wait for a response, copy the results. My pipeline is automated - drop a thousand PDFs in a bucket, walk away, and the results appear in a searchable database. It's the difference between using a tool and building infrastructure. Anyone can use ChatGPT, but building automated AI pipelines is an engineering skill."

---

## Cost Estimate (Minimal Usage)

| Service | Free Tier | After Free Tier |
|---------|-----------|-----------------|
| S3 | 5GB storage | ~$0.023/GB |
| Lambda | 1M requests/month | ~$0.20/1M requests |
| DynamoDB | 25GB + 25 RCU/WCU | Pay per request |
| Bedrock | Varies by model | ~$0.003/1K input tokens |

**For portfolio/testing:** Likely under $1/month with minimal usage.

---

## Business Value

### For Personal Use
- Auto-process brand deal contracts
- Extract payment terms, deadlines, usage rights
- Log expenses from invoices automatically
- Summarize research documents

### For Businesses
- Invoice processing at scale
- Contract analysis and extraction
- Compliance document review
- Customer document intake automation

### The Math
- Virtual assistant: $500-2000/month
- This pipeline: Pennies per document
- Scales infinitely without hiring

---

## What I Learned

### Technical Skills
- AWS Lambda development
- Amazon Bedrock AI integration
- DynamoDB NoSQL database
- S3 event-driven architecture
- SAM/CloudFormation Infrastructure as Code
- Git version control workflow

### Problem-Solving Skills
- Reading error messages carefully
- Understanding the difference between syntax and semantic validation
- Debugging deployment issues
- Iterative troubleshooting

### AI-Native Development
- Upload files to AI for direct fixes (faster than manual debugging)
- Get working code first, understand later
- Use AI to generate boilerplate and configuration
- Compare broken vs fixed versions to learn

---

## Future Enhancements (If Continuing)

### Phase 7: Frontend (2-3 sessions)
- API Gateway for REST endpoints
- Static website hosted on S3
- Upload interface
- Results display page

### Phase 8: Search & Query
- DynamoDB secondary indexes
- Search across all documents
- Filter by date, type, content

### Phase 9: Production Hardening
- Multi-region deployment
- CI/CD pipeline (auto-deploy on git push)
- Monitoring and alerting
- Cost controls and budgets

---

## Quick Reference Commands

```powershell
# Navigate to project
cd C:\Users\mcclu\ai-document-pipeline\doc-intelligence-pipeline

# Validate template
sam validate

# Build project
sam build

# Deploy (first time)
sam deploy --guided

# Deploy (subsequent)
sam deploy

# Git workflow
git add .
git commit -m "Your message"

# Check Python version
python --version

# List files (see actual names)
dir
```

---

## Conclusion

This project demonstrates real cloud engineering skills:
- **Serverless architecture** using AWS managed services
- **Event-driven design** with automatic triggers
- **AI integration** via Amazon Bedrock
- **Infrastructure as Code** with SAM/CloudFormation
- **Professional workflow** with Git version control

It's not just a tutorial project - it's a working system that can process real documents, solve real problems, and scale without manual intervention.

**Total development time:** ~6 sessions over 2 weeks  
**Lines of code:** 124 (Lambda function) + 56 (template.yaml)  
**AWS services used:** S3, Lambda, Bedrock, DynamoDB, IAM, CloudWatch, X-Ray

---

**Project Status: COMPLETE ✅**

*Documentation created: February 1, 2026*
