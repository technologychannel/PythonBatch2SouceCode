import requests

url = "https://api.x.ai/v1/chat/completions"
essay = input("Enter essay topic: ")
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xai-wEktZgVcOWloPY45ThNlyoy9iuAMQyFLdjod0HT3uxoLrqzEJebZQyePo0cl9kcBIhirn7huc8UdDX5c"
}
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are essay writer: "
        },
        {
            "role": "user",
            "content": f"Write essay on {essay} in 100 word."
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}
response = requests.post(url, headers=headers, json=data)

# Extract the 'essay' content from the response
essay = response.json().get('choices', [])[0].get('message', {}).get('content', '')

# Print the essay content
print(essay)