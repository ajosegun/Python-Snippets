
import config

## URL Shortener

# pip3 install pyshorteners

import pyshorteners

url = input("Enter your url: ")
print("Your url: ", pyshorteners.Shortener().tinyurl.short(url))

# Bit.ly shortener Implementation
# Get API KEY from your bitly account

api_key = config.tinyurl_api_key

s = pyshorteners.Shortener(api_key=api_key)
print(s.bitly.short(url))

#follow insta/@codewithjoxia