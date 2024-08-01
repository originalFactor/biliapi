import httpx, bs4, json

res = httpx.get("https://socialsisteryi.github.io/bilibili-API-collect/docs/misc/sign/APPKey.html")

soup = bs4.BeautifulSoup(res.text)

table = soup.table

dataKeys = []

data = []

for head in table.find_all("th"):
    dataKeys.append(head.text)
    
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    dataItem = {}
    for i in range(len(cols)):
        dataItem[dataKeys[i]] = cols[i].text
    data.append(dataItem)

with open('./docs/assets/sign/app/appkeys.json','w') as f:
    json.dump(data, f)
