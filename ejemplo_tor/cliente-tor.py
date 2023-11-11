from multiprocessing.pool import ThreadPool
from torpy.http.requests import tor_requests_session

with tor_requests_session() as s:  # returns requests.Session() object
    links = ['http://nzxj65x32vh2fkhk.onion', 'http://facebookcorewwwi.onion'] * 2

    with ThreadPool(3) as pool:
        pool.map(s.get, links)
