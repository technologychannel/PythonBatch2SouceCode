import requests

url = "https://api.x.ai/v1/chat/completions"

husband_name = input("Enter husband's name: ")
wife_name = input("Enter wife's name: ")

headers = {
    "Content-Type": "application/json",
      "Authorization": "Bearer xai-UeY2DHVlLSSaZObWTEPMRuyKMbRNjWBlmwVOO6l2dzInrozNp4kcgfSK47iNQVgqwp6VYvuMuZAnpvSW"
}
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are a user. Please provide the following information."
        },
        {
            "role": "user",
            "content": f"Generate 5 Asian Baby Names for husband {husband_name} and wife {wife_name}. Provide direct in point.`"
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Extract and print only the essay content from the response JSON
if response.status_code == 200:
    response_json = response.json()
    essay_content = response_json['choices'][0]['message']['content']
    print(essay_content)
else:
    print(f"Error: {response.status_code}, {response.text}")

## Create Essay Writer Web App Using Django.