from queue import Queue
from threading import Thread
import math
import struct

class CHandler:

    def __init__(self, socket):
        self.socket = socket
        self.dataQueue = Queue()
        self.readThread = Thread()
        self.running = True

    def initConnection(self, id):
        # get plant type
        self.type = int.from_bytes(self.socket.recv(4), byteorder='little')
        self.plant_id = id
        print("Plant id:", self.plant_id, "type:", self.type)
        self.socket.send(self.plant_id.to_bytes(4, 'little'))
        self.readThread = Thread(target=self.autoListener)
        self.readThread.start()

    def autoListener(self):
        while (self.running):
            data = self.socket.recv(4)
            id = struct.unpack("i", data)
            data = self.socket.recv(8)
            waterLevel = struct.unpack("d", data)
            data = self.socket.recv(8)
            chemA = struct.unpack("d", data)
            data = self.socket.recv(8)
            chemB = struct.unpack("d", data)
            data = self.socket.recv(8)
            growthLevel = struct.unpack("d", data)
            data = self.socket.recv(1)
            state = struct.unpack("?", data)
            data = self.socket.recv(4)
            timeStamp = struct.unpack("i", data)
            data = self.socket.recv(4)
            checkSum = struct.unpack("i", data)

            if checkSum[0] == math.floor(float(id[0]) + float(waterLevel[0]) + float(chemA[0]) + float(chemB[0]) + float(growthLevel[0]) + float(timeStamp[0]) + float(state[0])):
                vals = [id[0], waterLevel[0], chemA[0], chemB[0], growthLevel[0], timeStamp[0], int(state[0])]
                self.dataQueue.put(vals)

    def popQueue(self):
        if self.dataQueue.empty():
            return []
        return self.dataQueue.get()

    def sendCommand(self, waterAmt):
        self.socket.send(waterAmt.to_bytes(4, "little"))

    def stop(self):
        self.running = 0

    def closeConnection(self):
        self.socket.close()

