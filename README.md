## Train with Lambda AWS

#### Prepare
1 - Before further actions, you need to install:
* [Python](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/get-docker/)
* [Serverless Application Model (sam)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

2 - Do the next commands:
 1. Add to root folder .env
 2. Copy from _env to .env.
 3. Set all environment variables

NOTE: When you want to add a new environment variable follow the next principle:
 1. Add new variable to _env and .env files
 2. Go to template.yaml Globals->Function->Environment->Variables
    add variable with !Ref to Parameters. Name of parameter must
    follow by the next pattern:
    * starts with lower symbol
    * contains only alphabet symbols
    * first symbol after under "_" symbol must be upper     
    Examples: DB_NAME -> dbName; DB_USERNAME -> dbUsername; SOME_SPEC_VAR -> someSpecVar

#### Create python virtualenv(optional)
```bash
cd PROJECT_FOLDER
python3.8 -m venv ./venv
. venv/bin/activate
```

#### Build application:
```bash
sam build --use-container
```

#### Start local ApiGateWay(for testing purposes)
```bash
sam local start-api --parameter-overrides $(python3 environ.py)
```

#### Deploy project to AWS CloudFormation
```bash
sam build -g --parameter-overrides $(python3 environ.py) 
```
NOTE: key -g needs only for the first deploy

#### Delete CloudFormation stack
```bash
aws cloudformation delete-stack --stack-name STACK_NAME
```