import socket
from smartag.ClientHandler import CHandler

def setupConnection(numToConnect, port):
    print('Setting up the Connection...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    print('Created Socket...')

    s.listen(numToConnect)

    print("Made server... listening!");

    clients = []

    i = 0
    while i < 20:
        c, addr = s.accept()

        print('Addr is', addr)

        clients.append(CHandler(c))

        clients[len(clients) - 1].initConnection(i)

        # clients[len(clients) - 1].autoListener()

        i = i + 1

    return clients

'''
while 1:
    for c in clients:
        val = c.popQueue()
        if len(val) > 0:
            count = count + 1
            print(val)
            if count == 10:
                count = 0
                c.sendCommand(10)
                print("Watering...")
'''