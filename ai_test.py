import openai


def test_openai():
    openai.api_key = "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"
    print("open ai hehe")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What dinosaurs lived in the cretaceous period?",
        max_tokens=60
    )
    print(response)