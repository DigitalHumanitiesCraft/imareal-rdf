# Import prerequisite libraries
import os
import openai

# Setting the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Perform tasks using OpenAI API
models = openai.Model.list()  # List all OpenAI models

# Print the list of models
print(models)
