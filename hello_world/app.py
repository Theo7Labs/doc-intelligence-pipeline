import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    """
    Triggered when PDF uploaded to S3.
    Reads PDF, sends to Bedrock for analysis, stores results in DynamoDB.
    """
    
    print("Lambda function started")
    
    # Extract S3 bucket and object key from event
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        print(f"Processing file: {object_key} from bucket: {bucket_name}")
    except KeyError as e:
        print(f"Error extracting S3 info: {e}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid S3 event format"})
        }
    
    # Initialize AWS clients
    s3_client = boto3.client('s3')
    bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
    dynamodb = boto3.resource('dynamodb')
    
    # Download PDF from S3
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        pdf_content = response['Body'].read()
        print(f"Successfully downloaded PDF, size: {len(pdf_content)} bytes")
    except Exception as e:
        print(f"Error downloading from S3: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to download PDF: {str(e)}"})
        }
    
    # For now, we'll use a placeholder for PDF text extraction
    # In production, you'd use PyPDF2 or pdfplumber
    pdf_text = f"[PDF Content from {object_key}]"
    print(f"PDF text extracted (placeholder)")
    
    # Create prompt for Bedrock
    prompt = f"""Analyze this document and extract key information in JSON format.

Document: {pdf_text}

Extract the following information:
- summary: A brief summary of the document
- key_points: List of main points
- document_type: Type of document (report, manual, letter, etc.)

Respond ONLY with valid JSON, no other text."""

    # Call Bedrock (Claude)
    try:
        bedrock_request = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        bedrock_response = bedrock_client.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            body=json.dumps(bedrock_request)
        )
        
        response_body = json.loads(bedrock_response['body'].read())
        extracted_data = response_body['content'][0]['text']
        print(f"Bedrock response received")
        
    except Exception as e:
        print(f"Error calling Bedrock: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to process with Bedrock: {str(e)}"})
        }
    
    # Store results in DynamoDB
    try:
        table_name = os.environ.get('TABLE_NAME', 'ProcessedDocumentsTable')
        table = dynamodb.Table(table_name)
        
        # Generate document ID from filename
        document_id = object_key.replace('/', '_').replace('.pdf', '')
        
        item = {
            'document_id': document_id,
            'bucket_name': bucket_name,
            'object_key': object_key,
            'processed_at': datetime.now().isoformat(),
            'extracted_data': extracted_data,
            'file_size': len(pdf_content)
        }
        
        table.put_item(Item=item)
        print(f"Successfully stored results in DynamoDB")
        
    except Exception as e:
        print(f"Error storing in DynamoDB: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to store in DynamoDB: {str(e)}"})
        }
    
    # Success!
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Document processed successfully",
            "document_id": document_id,
            "processed_at": datetime.now().isoformat()
        })
    }