# Personal Fitness Bot

# Quick Summary
- I am building a fitness bot using python, aws, and twilio SMS that I will be able to text on any given day and will receive a response with a random workout to complete 

- This is a serverless environment so AWS will be in use

## Steps To Run
### Early Steps
- set up your twilio account </br>
    - https://www.twilio.com/docs/sms/quickstart/python
- make sure you have an AWS account </br>
    - https://aws.amazon.com/getting-started/
- enable your AWS CLI </br> 
    - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

### Python
- Initialize the Virtual Environment </br>
    - ``` python3 -m venv environment-name ```

- Implement the Required Packages
    - see `requirements.txt` file

- Activate the Environment  </br>
    - ``` source environment-name/bin/activate ```
- Install the Dependencies </br>
    - ``` pip3 install -r requirements.txt ```

- Create `__send_sms.py__` file for Twilio implementation
    - this file will be in accordance with the twilio walk though mentioned above
    - do not forget to run ``` pip install twilio ``` at the end 

- Write the AWS Lambda Function 
    - refer to `__lambda_handler.py__` file
    - this will handle the messages
    - Flask is used to maintain the context of the conversation throughout the interaction
        - messages received -> Flask identifies the context -> proper response is kicked back

- Create `__exercise_inventory.json__` as your nonrelational database
    - this is used to hold your variety of categorical workouts to construct a full workout upon request
    - this is needed to carry out the `build_workout` function in the `__lambda.handler.py__` file 
    - the history of the workouts will be stored in AWS's DynamoDB

- Set up the AWS Environment
    - setup the AWS serverless infrastructure
        - a DynamoDB database is required to carry out the `write_workout_to_dynamo` function
            - name the table whatever you desire
            - the primary key will be a partition key named "workout_user"
            - the sort key will be named "exercise_time"
    - since the code with be deployed to AWS as a Lambda function, Zappa is used to assist in this
        - Zappa will setup the leftover serverless infrastructure
            - includes: IAM roles, Lambda function, & API Gateway
        - refer to `__twilio-fit-iam-policy.json__` file
            - relevant documentation is located here: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html
        -  create `__zappa_settings.json__`
            - this is the setup for the deployment configuration for Zappa
            - update zappa as necessary

- Deploy to the Cloud
    - from the CLI
        - enter `zappa deploy fitness-bot`
            - "fitness-bot" is used here because that's the name given to the deployment in __zappa_settings.json__
        

