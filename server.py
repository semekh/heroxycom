from twisted.internet import reactor
from twisted.web import proxy, http
import urlparse
import os
import config


class ServerProxyRequest(proxy.ProxyRequest):
    def process(self):
        upstream_headers = self.getAllHeaders().copy()
        uri = upstream_headers['uri']

        parsed = urlparse.urlparse(uri)
        protocol = parsed[0]
        host = parsed[1]
        port = self.ports[protocol]
        if ':' in host:
            host, port = host.split(':')
            port = int(port)
        rest = urlparse.urlunparse(('', '') + parsed[2:])
        if not rest:
            rest += '/'
        class_ = self.protocols[protocol]
        headers = {}
        for x in upstream_headers:
            if x.startswith(config.HEADER_PREFIX):
                headers[x[len(config.HEADER_PREFIX):]] = upstream_headers[x]
        self.content.seek(0, 0)
        s = self.content.read()
        clientFactory = class_(self.method, rest, self.clientproto, headers, s, self)
        self.reactor.connectTCP(host, port, clientFactory)


class ServerProxy(proxy.Proxy):
    requestFactory = ServerProxyRequest


class ServerProxyFactory(http.HTTPFactory):
    protocol = ServerProxy


if __name__ == "__main__":
    reactor.listenTCP(int(os.getenv('PORT', config.DEFAULT_SERVER_PORT)), ServerProxyFactory())
    reactor.run()
