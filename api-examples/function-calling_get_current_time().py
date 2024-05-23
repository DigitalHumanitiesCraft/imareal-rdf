import openai
import datetime
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_current_time():
    """
    Gets the current time in 'HH:MM AM/PM' format.
    """
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


functions = [
    {
        "name": "get_current_time",
        "description": "Gets the current time in 'HH:MM AM/PM' format.",
        "parameters": {
            "type": "object",
            "properties": {},  # No parameters needed
        },
        "required": [],
    }
]


def main():
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            break

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}],
            functions=functions,
            function_call="auto",  # Let the model decide if to call a function
        )

        response_message = response["choices"][0]["message"]

        if response_message.get("function_call"):
            function_name = response_message["function_call"]["name"]
            function_args = json.loads(response_message["function_call"]["arguments"])

            if function_name == "get_current_time":
                current_time = get_current_time()
                print("AI: I am using function calling to tell you that the current time is", current_time)
        else:
            print("AI:", response_message["content"])


if __name__ == "__main__":
    main()
