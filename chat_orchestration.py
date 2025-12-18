from openai import OpenAI, Anthropic

client = OpenAI(api_key="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")

client = OpenAI(api_key="sk-proj-V7rBn1nbrzzOF0mCAsEtt1p3LKGWWRI6bPPm1_A3g4Lzy8Zq8XFlzX_xfC3VHE5zpyaUKgMHaQT3BlbkFJFObs3ljCERoRsM4NlLQ-OZDldM5pvFYJuljU2tRafumuAIi7O7vroRY1bsoPey6Fr")

anthropic_client = Anthropic(api_key="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")
                        
response = client.chat.completions.create(
    model="gpt-4.1",   # or gpt-4.1-mini, gpt-4.1-preview
    messages=[
        {"role": "user", "content": "Hello, GPT-4! Explain transformers in 2 lines."}
    ]
)

print(response.choices[0].message["content"])
