import requests

# r= requests.get('https://www.google.com')
# print(r.status_code)
# print("="*100)
# print(r.text)
# print("="*100)



# r= requests.get("https://xkcd.com/353/")
# print(r.headers)
# print("="*100)
# print(r.status_code)
# print(r.text)
# print(r.content)
# print("="*100)


# r= requests.get("https://imgs.xkcd.com/comics/python.png")
# print(r.content)
# print(r.headers)
# with open("python.png", "wb") as f:
#     f.write(r.content)

#=========================================
payload={
    "name": "John Doe",
    "email": "jon@gmail.com",
}
r= requests.get("https://httpbin.org/delay/3", timeout=2)

print(r.status_code)
# print(r.json())

# print(r.json().get("form"))