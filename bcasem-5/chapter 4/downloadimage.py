import urllib.request

# Image URL
url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# Create a request object with a User-Agent header
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

# Open the URL and save the image
with urllib.request.urlopen(req) as response:
    with open("myimage1.jpg", "wb") as out_file:
        out_file.write(response.read())
