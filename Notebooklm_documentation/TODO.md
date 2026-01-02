# 📋 AI Document Intelligence Pipeline - TODO List

**Last Updated:** January 1, 2025  
**Current Phase:** Phase 2 (In Progress)  

---

## ⏸️ IMMEDIATE NEXT STEPS (Resume Here!)

**You stopped at this question in PowerShell:**
```
Would you like to enable X-Ray tracing on the function(s) in your application? [y/N]:
```

**Answer:** Type `n` and press Enter

**Then complete the remaining sam init questions**

---

## ✅ Phase 2 Completion Checklist

- [ ] Answer X-Ray question (`n`)
- [ ] Complete sam init
- [ ] Navigate into project: `cd doc-intelligence-pipeline`
- [ ] Verify files created: `ls`
- [ ] View template.yaml: `cat template.yaml`
- [ ] Initialize Git: `git init`
- [ ] Create docs folder: `mkdir docs`
- [ ] Move Phase 1 markdown files into `docs/phase-1-planning/`

---

## ⚠️ CRITICAL REMINDER

### **BEFORE PHASE 3 DEPLOYMENT:**

**Enable X-Ray in template.yaml!**

Add this to the function properties:
```yaml
Tracing: Active
```

**Location in file:**
```yaml
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Tracing: Active  # ← ADD THIS LINE
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.13
      ...
```

**Why:** Professional monitoring, helps debug, portfolio looks better

---

## 📝 Phase 3 Tasks (After Phase 2 Complete)

- [ ] Rename `HelloWorldFunction` → `DocumentProcessorFunction`
- [ ] Rename `hello_world/` folder → `src/`
- [ ] Add S3 bucket resource to template.yaml
- [ ] Add S3 event trigger to Lambda
- [ ] Add DynamoDB table resource
- [ ] Update IAM permissions for Lambda
- [ ] Add Bedrock permissions
- [ ] Test template validation: `sam validate`
- [ ] Deploy to AWS: `sam deploy --guided`

---

## 📁 Files to Organize

**Currently in Downloads folder (need to move to project):**
1. Day-01-Session-Log.md
2. architecture-design.md
3. extraction-examples.md
4. ai-copilot-workflow.md
5. infrastructure-as-code-overview.md
6. PHASE-2-HANDOFF.md
7. TODO.md (this file)

**Move to:** `C:\Users\mcclu\ai-document-pipeline\docs\`

---

## 🧠 What Claude's Memory Knows

```
Building AI Document Intelligence Pipeline (S3→Lambda→Bedrock→DynamoDB).
Remember to enable X-Ray tracing in template.yaml before final deployment.
```

This persists to all future chats!

---

## 🎯 Project Overview (Quick Reminder)

**What we're building:**
- Upload PDF to S3
- Lambda triggered automatically
- Lambda calls Bedrock AI (Claude)
- AI extracts structured data (summary, steps, PPE, warnings)
- Store results in DynamoDB
- Query via API Gateway

**Tech Stack:**
- AWS SAM (Infrastructure as Code)
- Python 3.13
- AWS Lambda
- AWS Bedrock (Claude 3 Haiku)
- DynamoDB
- API Gateway
- S3

**Test Documents:**
- __SAFETY_SOP.pdf (main SOP)
- Simplified_Safety_Guide.pdf
- Technician_Quick_Sheet.pdf

---

## 📞 Start Next Chat With:

```
Hey Claude, continuing my AI Document Intelligence Pipeline project.
We stopped during Phase 2 (sam init) at the X-Ray question.
Check your memory and I'm uploading PHASE-2-HANDOFF.md for context.
What should I do next?
```

---

*Keep this file handy - it's your quick reference guide!*
