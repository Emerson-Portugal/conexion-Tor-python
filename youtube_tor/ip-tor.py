from torpy.http.requests import TorRequests

with TorRequests() as tor_requests:
    print("conexion 1")
    with tor_requests.get_session() as sess:
        # print(sess.get("http://httpbin.org/ip").json())
        print(sess.get("http://ip-api.com/json").json())
