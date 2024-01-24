import requests

url = 'https://example.com'  # Replace with the URL you want to access
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Process the response content here
    content = response.text
    print(content)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
