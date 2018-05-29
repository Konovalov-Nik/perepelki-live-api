from gevent.pywsgi import WSGIServer

from perepelki_api.api.app import APP


def main():
    http_server = WSGIServer(('', 5000), APP)
    http_server.serve_forever()


if __name__ == "__main__":
    main()
