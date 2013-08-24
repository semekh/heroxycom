#!/bin/env python2
import base64
from twisted.internet import reactor
from twisted.web import proxy, http
import urlparse
import config


class ClientProxyRequest(proxy.ProxyRequest):
    def process(self):
        parsed = urlparse.urlparse(self.uri)
        protocol = parsed[0]
        host = parsed[1]
        if ':' in host:
            host, port = host.split(':')
        class_ = self.protocols[protocol]
        upstream_headers = self.getAllHeaders().copy()
        if 'host' not in upstream_headers:
            upstream_headers['host'] = host
        headers = {'host': config.SERVER_HOST, 'uri': self.uri}
        if 'content-length' in upstream_headers:
            headers['content-length'] = upstream_headers['content-length']
        for x in upstream_headers:
            headers[config.HEADER_PREFIX + x] = upstream_headers[x]
        self.content.seek(0, 0)
        s = self.content.read()
        clientFactory = class_(self.method, '/' + base64.urlsafe_b64encode(self.uri), self.clientproto, headers, s,
                               self)
        self.reactor.connectTCP(config.SERVER_HOST, int(config.DEFAULT_SERVER_PORT), clientFactory)


class ClientProxy(proxy.Proxy):
    requestFactory = ClientProxyRequest


class ClientProxyFactory(http.HTTPFactory):
    protocol = ClientProxy


if __name__ == "__main__":
    reactor.listenTCP(int(config.DEFAULT_CLIENT_PORT), ClientProxyFactory())
    reactor.run()
