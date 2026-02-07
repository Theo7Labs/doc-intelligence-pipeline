import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    """
    Generate a presigned URL for uploading a PDF to S3.
    Frontend calls this to get a secure upload link.
    """
    print("Generate upload URL request received")
    
    # Get filename from query parameters
    query_params = event.get('queryStringParameters') or {}
    filename = query_params.get('filename', f'{uuid.uuid4()}.pdf')
    
    # Ensure .pdf extension
    if not filename.lower().endswith('.pdf'):
        filename += '.pdf'
    
    # Sanitize filename
    safe_filename = filename.replace(' ', '_')
    
    bucket_name = os.environ['BUCKET_NAME']
    
    try:
        s3_client = boto3.client('s3')
        
        # Generate presigned URL (valid for 5 minutes)
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': bucket_name,
                'Key': safe_filename,
                'ContentType': 'application/pdf'
            },
            ExpiresIn=300
        )
        
        print(f"Generated presigned URL for: {safe_filename}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,OPTIONS'
            },
            'body': json.dumps({
                'uploadUrl': presigned_url,
                'filename': safe_filename,
                'bucket': bucket_name
            })
        }
        
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,OPTIONS'
            },
            'body': json.dumps({'error': str(e)})
        }
