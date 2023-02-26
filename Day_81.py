import  requests
import json
url1 = "https://newsapi.org/v2/everything?q=apple&from=2023-02-25&to=2023-02-25&sortBy=popularity&apiKey=038a605807664946a81dd2ff4efe9433"
url2 = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-26&sortBy=publishedAt&apiKey=038a605807664946a81dd2ff4efe9433"

r = requests.get(url2)
print(json.dumps(r.json(),indent=2))