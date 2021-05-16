import requests

def gen_for_urls(urls: tuple) -> tuple: 
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


urls = ('http://bbc.co.uk','http://google.com','http://www.lidl.co.uk')

for resp_len, status, url in gen_for_urls(urls):
    print(resp_len, status,url)