from openai import OpenAI
client = OpenAI(api_key='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')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex English language concepts with creative flair."},
    {"role": "user", "content": "Explain what is the hardest part for ESL when preparing in TOEFL test."}
  ]
)

print(completion.choices[0].message)
# 将print中返回得到的文本结果输出到文件
with open("test.txt", 'w', encoding='utf-8') as file:
    file.write(completion.choices[0].message)
