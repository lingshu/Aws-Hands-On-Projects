# Aws-Hands-On-Projects
### 1. Run Flask App on EC2
    Run flask_server.py on AWS EC2 using
    FLASK_APP=flask_server.py flask run --host=0.0.0.0 --port=8080
    
    Then go to browser and go to the following URL:
    http://ec2-18-224-141-193.us-east-2.compute.amazonaws.com:8080/

### 2. Launch HTTP server on EC2, fetch and upload data with management of RDS database
    Run server.py on AWS EC2 using
    FLASK_APP=server.py flask run --host=0.0.0.0 --port=8080
    
    Then go to browser and go to the following URL:
    http://ec2-18-224-141-193.us-east-2.compute.amazonaws.com:8080/
    
### 3. Upload files using server on EC2 and store files in S3 buckets. Set up IAM users to get full access of S3 and configure credentials in .aws directory on EC2. Get files in S3 directly from browser
    Run server-s3.py on AWS EC2 using
    FLASK_APP=server-s3.py flask run --host=0.0.0.0 --port=8080
    
    Then go to browser and go to the following URL:
    http://ec2-18-224-141-193.us-east-2.compute.amazonaws.com:8080/
