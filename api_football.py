import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "5a951dd93dea6c3d26870a9624f004d9"
    }

cruzeiro_id = str(135)
brasil_id = str(6)

conn.request("GET", "/fixtures?status=NS&next=3&season=2024&team=" + brasil_id , headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

### Doesnt work for current games in the free plan, only for games in 2021-2022