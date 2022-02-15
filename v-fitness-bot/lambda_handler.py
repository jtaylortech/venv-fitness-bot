import json
import random
import re
import boto3
import datetime
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse


SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)


def write_workout_to_dynamo(user_name, workout_obj):
    """
    Writes the workout object to the DynamoDB workout log.
    :param phone_num: Phone number to use as the partition key.
    :param workout_obj: Workout object to be written.
    :return:
    """
    dynamo = boto3.resource("dynamodb")

    tbl = dynamo.Table("twilio-fit-log")

    tbl.put_item(
        Item={
            'workout-user': str(user_name),
            'exercise_time': str(datetime.datetime.now()),
            'workout': workout_obj,
        }
    )


def buildworkout():
    """
    Builds the workout for the day.
    :return: A workout dictionary with the workout details and a string representation of the workout.
    """
    with open("exercise_inventory.json", "r") as f:
        exercises = json.load(f)
        f.close()

    workout = {k: random.choice(v) for k, v in exercises.items()}

    msg_intro = "Today's workout: \n ... what do you think?"
    exercise_msg = "\n".join([k + ": " + v for k, v in workout.items()])
    workout_msg = "\n".join([msg_intro, exercise_msg])

    return workout, workout_msg


    @app.route("/", methods=["POST"])
    def main():
        # makes the message lowercase removes punctuation to ease readability
        msg=re.sub(r'[^\w\s]', '', requests.values.get("Body".lower()))

        # is there an on going conversation
        context = session.get("context", "hello")

        # test for the wake phrase if this is the first entry
        if context == "hello":
            if msg == "whats todays workout":
                # this is the workout builder
                workout_obj, workout_msg = build_workout()
                session["context"] = "build_workout"
                session["response"] = workout_msg
                session["workout_obj"] = workout_obj
            else:
                session["response"] = "I don't understand what you're asking."

        # acknowledges the workout 
        elif context == "build_workout":
            if msg == "lets get it":
                session["response"] = "Bet! Make sure you tell JT how it went."
                session["cleanup"] = True

                # logs the workout in the log -> DynamoDB
                write_workout_to_dynamo("fitness-bot", session["workout_obj"])
            elif msg == "lets do something else":
                # build another workout
                workout_obj, workout_msg = build_network()
                session["response"] = workout_msg
                session["workout_obj"] = workout_obj
            else:
                session["response"] = "I don't understand ...?"

        # cleans up the session
        if session.get("cleanup", False):
            session.pop("context")
            session.pop("cleanup")

        # sends the text response
        resp = MessagingResponse()
        resp.message(session.get("response"))

        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)