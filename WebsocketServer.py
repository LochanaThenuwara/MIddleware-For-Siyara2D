from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
import json
import TCPSocket

subscribers={}
index=0
class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):

        print("Client connecting: {0}".format(request.peer))
        print (request.peer)

        subscribers[request.peer]=self

        #print TCPSocket.vessel_list[0]


    def onOpen(self):
        print("WebSocket connection open.")

        m = [{"latitude": "6.97037", "Ship_name": "Y101", "longitute": "79.839915"},
             {"latitude": "6.96490333", "Ship_name": "R16", "longitute": "79.853065"},
             {"latitude": "6.95782667", "Ship_name": "R14", "longitute": "79.847035"}]
        n = json.dumps(m)
        o = json.loads(n)

        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))

        # echo back message verbatim
        payload = json.dumps(o, ensure_ascii=False).encode('utf8')





    def onMessage(self, payload, isBinary):

        # m = [{"latitude":"6.97037","Ship_name":"Y101","longitute":"79.839915"},{"latitude":"6.96490333","Ship_name":"R16","longitute":"79.853065"},{"latitude":"6.95782667","Ship_name":"R14","longitute":"79.847035"}]
        # n = json.dumps(m)
        # o = json.loads(n)


        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))

        # # echo back message verbatim
        # payload=json.dumps(o, ensure_ascii = False).encode('utf8')
        # self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


#if __name__ == '__main__':

def funcWS():
    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9003")
    factory.protocol = MyServerProtocol


    reactor.listenTCP(9003, factory)
    reactor.run()
