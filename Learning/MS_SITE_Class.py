import requests, bs4
res = requests.get('https://portal.msrc.microsoft.com/ja-JP/security-guidance/advisory/CVE-2018-1040')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('.form-control-static.flat-bottom.ng-binding')
for elem in elems:
    print(elem)