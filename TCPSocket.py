import SocketServer
import json
import rethinkdb as r


import WebsocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):


    def handle(self):

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv\
            (1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print type(self.data)

        jdata = json.dumps(json.loads(self.data))
        print jdata, " data recieved from client"

        # def connect_db(self):--------------------------------------------------------------------------------------------

        db_connection = r.connect("localhost", 28015)
        # r.db_create("Siyara2D").run(db_connection)
        # r.db("Siyara2D").table_create("Vessels").run
        vessel=json.loads(jdata)

        # r.db("Siyara2D").table("Vessels").delete().run(db_connection)
        #--------------------- cursor1 = r.db("Siyara2D").table("Vessels").changes().run(db_connection)

        if (r.db("Siyara2D").table("Vessels").get(vessel["Ship_name"]).run(db_connection)):
            print "in the if"
            r.db("Siyara2D").table("Vessels").get(vessel["Ship_name"]).update({
                "latitude": vessel["latitude"],
                "longitute": vessel["longitute"],

            }).run(db_connection)

        else:
            r.db("Siyara2D").table("Vessels").insert(json.loads(jdata)).run(db_connection)


        cursor = r.db("Siyara2D").table("Vessels").run(db_connection)
        for document in cursor:
            print document

            # WebsocketServer.subscribers[0].sendMessage(document)

                # subscriber.sendMessage(new_user_alert)

        # ------------------------------------------------------------------------------------------------------------------

        self.request.sendall(self.data)









    # for cid,cobj in WebsocketServer.subscribers.items():
        #     cobj.sendMessage(jdata)


def funcTCP():
# if __name__ == "__main__":


    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

