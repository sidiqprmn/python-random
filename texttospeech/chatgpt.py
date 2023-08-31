import requests

def get_chatgpt_response(prompt):
    # Ganti YOUR_API_KEY dengan kunci API ChatGPT Anda
    api_key = "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"
    api_endpoint = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",  # Ganti dengan versi model yang sesuai
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": prompt}]
    }

    response = requests.post(api_endpoint, json=data, headers=headers)
    response_json = response.json()

    if "choices" in response_json and len(response_json["choices"]) > 0:
        chatgpt_reply = response_json["choices"][0]["message"]["content"]
        return chatgpt_reply
    else:
        return "Maaf, terjadi kesalahan dalam mendapatkan respons dari ChatGPT."

# Fungsi main untuk berkomunikasi dengan ChatGPT
def main():
    prompt = input("Anda: ")
    while prompt.lower() != "exit":
        reply = get_chatgpt_response(prompt)
        print("ChatGPT:", reply)
        prompt = input("Anda: ")

if __name__ == "__main__":
    main()
