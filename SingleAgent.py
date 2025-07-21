# ✅ ChatGPT Agent with Memory using GPT-4.1 nano (New SDK - One Cell)
!pip install openai

from openai import OpenAI
client = OpenAI(api_key="yourkeyhere")  # Replace with your OpenAI API key

conversation_history = []

def chat_with_memory(prompt):
    context = "\n".join(conversation_history[-5:])
    full_prompt = f"{context}\nUser: {prompt}\nAssistant:"

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt}
        ]
    )

    reply = response.choices[0].message.content
    conversation_history.append(f"User: {prompt}")
    conversation_history.append(f"Assistant: {reply}")
    return reply

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    reply = chat_with_memory(user_input)
    print("AIUN Agent:", reply)
