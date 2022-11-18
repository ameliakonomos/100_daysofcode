import requests
data_response = requests.get(url="https://api.kanye.rest")

quote = data_response.json()["quote"]
print(f"Kanye says '{quote}' ")