import openai
from rdflib import Graph
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def query_knowledge_base(question: str) -> str:
    """Queries the RDF knowledge base and returns an answer."""
    g = Graph()
    g.parse("knowledge_base.ttl", format="ttl")

    depictions = []
    for subject, predicate, obj in g:
        if str(subject).endswith("God") and str(predicate).endswith("depiction"):
            depictions.append(obj.toPython())

            """ Example Turtle:
            <God> <depiction> "An old man with a white beard".
            <God> <depiction> "A burning bush".
            <God> <depiction> "An omnipresent spirit". """

    if depictions:
        return "The depictions of God include: " + ", ".join(depictions)
    return "I don't have information about that."


functions = [
    {
        "name": "query_knowledge_base",
        "description": "Queries the knowledge base about facts.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The question to ask the knowledge base.",
                }
            },
            "required": ["question"],
        },
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
            function_call="auto",
        )

        response_message = response["choices"][0]["message"]

        if response_message.get("function_call"):
            function_name = response_message["function_call"]["name"]
            function_args = json.loads(response_message["function_call"]["arguments"])

            if function_name == "query_knowledge_base":
                question = function_args["question"]
                answer = query_knowledge_base(question)
                print("AI:", answer)
        else:
            print("AI:", response_message["content"])


if __name__ == "__main__":
    main()
