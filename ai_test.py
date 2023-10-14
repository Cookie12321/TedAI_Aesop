import openai


def test_openai():
    openai.api_key = ""
    print("open ai hehe")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Tell me about the Wright brothers.",
        max_tokens=60,
    )
    print(response)