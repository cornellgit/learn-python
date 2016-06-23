from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


def worker(url, timeout):
    with urlopen(url, timeout=timeout) as conn:
        return conn.read()


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(worker, url, 60): url for url in URLS}
    for future, url in futures.items():
        try:
            page = future.result()
        except Exception as e:
            print(url, e)
        else:
            print(url, len(page))
