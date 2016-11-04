# import SocketServer
# import json
# import rethinkdb as r
# import TCPSocket
#
# import WebsocketServer
#
#
# def dbConnection():
#     db_connection = r.connect("localhost", 28015)
#         # r.db_create("Siyara2D").run(db_connection)
#         # r.db("Siyara2D").table_create("Vessels").run
#     vessel=json.loads(TCPSocket.jdata)
#
#         # r.db("Siyara2D").table("Vessels").delete().run(db_connection)
#         #--------------------- cursor1 = r.db("Siyara2D").table("Vessels").changes().run(db_connection)
#
#     if (r.db("Siyara2D").table("Vessels").get(vessel["Ship_name"]).run(db_connection)):
#         print "in the if"
#         r.db("Siyara2D").table("Vessels").get(vessel["Ship_name"]).update({
#                 "latitude": vessel["latitude"],
#                 "longitute": vessel["longitute"],
#
#             }).run(db_connection)
#
#     else:
#         r.db("Siyara2D").table("Vessels").insert(json.loads(jdata)).run(db_connection)
#
#
#     cursor = r.db("Siyara2D").table("Vessels").run(db_connection)
#     for document in cursor:
#         print document