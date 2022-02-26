import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_questions(role: str):
    prompt = f'''Create a list of 5 questions for my interview with a {role}:\n'''
    print(prompt)
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["text"]



if __name__ == "__main__":
    result = get_questions("software engineer")
    print(result)