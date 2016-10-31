import json
import rethinkdb as r
import WebsocketServer

def changeFeed():
    print "running realtime db........"

    db_connection = r.connect("localhost", 28015)

    feed = r.db("Siyara2D").table("Vessels").changes().run(db_connection)

    for document in feed:
        print document,"lenght of subscribers.... ",len(WebsocketServer.subscribers)

        for cid, cobj in WebsocketServer.subscribers.items():
            cobj.sendMessage(json.dumps(document["new_val"]))
