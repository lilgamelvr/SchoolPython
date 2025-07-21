import re

websites = "Test URLs: http://www.example.com, https://www.valid-url.co.uk, http://www.hardcoregaming101.net, and http://invalid.ext."

pattern = r'http://www\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'

valid_urls = re.findall(pattern, websites)

for url in valid_urls:
    print(url)