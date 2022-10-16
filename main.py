import os
import socket
import WSJTXClass as WSJTXClass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository.repository_reg import RepositoriesRegistry
from repository import (WSJTX_DecodeRepository, WSJTX_LoggedRepository, WSJTX_StatusRepository)


session_maker = sessionmaker(bind=create_engine("sqlite:///wsjtx.db", echo=False))
session = session_maker()

repositories_registry = RepositoriesRegistry(
    decode=WSJTX_DecodeRepository,
    logged=WSJTX_LoggedRepository,
    status=WSJTX_StatusRepository
    )

UDP_IP = "127.0.0.1"
UDP_PORT = 2237

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.bind((UDP_IP, int(UDP_PORT)))
print("Do Ctrl+c to exit the program !!")

while True:
    # send_data = input("Type some text to send =>");
    # s.sendto(send_data.encode('utf-8'), (ip, port))
    # print("\n\n 1. Client Sent : ", send_data, "\n\n")
    fileContent, address = sock.recvfrom(4096)
    NewPacket = WSJTXClass.WSJTX_Packet(fileContent, 0)
    NewPacket.Decode()

    if NewPacket.PacketType == 0:
        HeartbeatPacket = WSJTXClass.WSJTX_Heartbeat(fileContent, NewPacket.index)
        HeartbeatPacket.Decode()
        # self.uiHeartbeatMsg.emit(HeartbeatPacket)

    elif NewPacket.PacketType == 1:
        StatusPacket = WSJTXClass.WSJTX_Status(fileContent, NewPacket.index)
        StatusPacket.Decode()
        # session.add(StatusPacket)
        # session.commit()
        print(f'StatusPacket {StatusPacket}')
        # self.uiStatusMsg.emit(StatusPacket)

    elif NewPacket.PacketType == 2:
        DecodePacket = WSJTXClass.WSJTX_Decode(fileContent, NewPacket.index)
        DecodePacket.Decode()
        # can use PyQt4.QtCore.QTime for this as well!
        s = int((DecodePacket.Time / 1000) % 60)
        m = int(((DecodePacket.Time / (1000 * 60)) % 60))
        h = int(((DecodePacket.Time / (1000 * 60 * 60)) % 24))
        dataDecode = (
            "{:02}:{:02}:{:02} {:>3} {:4.1f} {:>4} {} {}".format(h, m, s, DecodePacket.snr, DecodePacket.DeltaTime,
                                                                 DecodePacket.DeltaFrequency, DecodePacket.Mode,
                                                                 DecodePacket.Message))
        # self.emit(QtCore.SIGNAL('update(QString)'), dataDecode)
        # self.DecodeCount += 1
        # now we need to send it to the UI
        repo_decode = WSJTX_DecodeRepository(session)
        decode = repo_decode.add(DecodePacket)
        session.commit()
        print("Client received : ", dataDecode)
    elif NewPacket.PacketType == 3:
        pass
        # self.uiEraseMsg.emit()

    elif NewPacket.PacketType == 5:
        LoggedPacket = WSJTXClass.WSJTX_Logged(fileContent, NewPacket.index)
        LoggedPacket.Decode()
        # session.add(LoggedPacket)
        # session.commit()
        # self.uiLoggedMsg.emit(LoggedPacket)

s.close()
