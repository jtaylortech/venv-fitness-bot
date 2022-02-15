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
    - see requirements.txt file

- Activate the Environment  </br>
    - ``` source environment-name/bin/activate ```
- Install the Dependencies </br>
    - ``` pip3 install -r requirements.txt ```

- Create __send_sms.py__ file for Twilio implementation
    - this file will be in accordance with the twilio walk though mentioned above
    - do not forget to run ``` pip install twilio ``` at the end 

- Write the AWS Lambda Function 
    - refer to __lambda_handler.py__ file
    - this will handle the messages
    - Flask is used to maintain the context of the conversation throughout the interaction
        - messages received -> Flask identifies the context -> proper response is kicked back
