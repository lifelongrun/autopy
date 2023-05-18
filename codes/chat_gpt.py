import requests

def call_chatgpt(prompt, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        response_json = response.json()
        message = response_json["choices"][0]["message"]["content"]
        return message.strip()
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    api_key = "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"  # 替换为你的API密钥
    prompt = "What is the capital of France?"  # 替换为你想要询问的问题

    response = call_chatgpt(prompt, api_key)
    if response:
        print(response)
