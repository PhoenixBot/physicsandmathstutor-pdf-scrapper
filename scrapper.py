import requests

url = "https://www.physicsandmathstutor.com/past-papers/gcse-maths/aqa-paper-1/"

# url = "https://www.physicsandmathstutor.com/maths-revision/gcse-number/"


data = requests.request("GET", url).text


buffer = []

for element in data.split('<a href="')[1:]:
    element = element.split('">')[0]
    if "pdf" in element.lower():
        buffer.append(element)

i = 0

for element in buffer:
    name = str(i) + element.rsplit("/")[-1]

    with open(name, "wb") as f:
        f.write(requests.get(element).content)

    i += 1
