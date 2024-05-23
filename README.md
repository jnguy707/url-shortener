# url-shortener

## Architecture Changes 
- Configuration of Variables
    - Host Name
    - Port
    - DB Connection Information
- Three Layer Architecture
    - Controller-Service-Repo
- Containerization + Cloud Hosting
    - Docker
    - AWS
- Add User Services
    - User owns shorten urls 
    - User has login information    
        - Login info
            - Hashed passwords
        
## Steps to Run Local DynamoDB
1. Create `.env` file with content
`
AWS_ACCESS_KEY_ID=dummy
AWS_SECRET_ACCESS_KEY=dummy
AWS_REGION=us-west-2
DYNAMODB_ENDPOINT_URL = http://localhost:8000
`
We do this because we use local_dotenv() to get local credentials.