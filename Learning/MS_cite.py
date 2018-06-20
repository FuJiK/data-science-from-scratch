import requests, bs4
url = 'https://portal.msrc.microsoft.com/ja-JP/security-guidance/advisory/ADV180012'
res = requests.get(url)
#res.raise_for_status()
print(res.status_code)
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('h2 class')
for elem in elems:
    print(elem)
