from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, Float

Base = declarative_base()


class WSJTX_Logged(Base):
    __tablename__ = 'WSJTX_Logged'
    id = Column(Integer, primary_key=True)
    DateOff = Column(Integer, default=0)
    TimeOff = Column(Integer, default=0)
    TimeOffSpec = Column(Integer, default=0)
    TimeOffOffset = Column(Integer, default=0)
    DXcall = Column(String, default="")
    DXgrid = Column(String, default="")
    DialFrequency = Column(Integer, default=0)
    Mode = Column(String, default="")
    ReportSent = Column(String, default="")
    ReportReceived = Column(String, default="")
    TxPower = Column(String, default="")
    Comments = Column(String, default="")
    Name = Column(String, default="")
    DateOn = Column(Integer, default=0)
    TimeOn = Column(Integer, default=0)
    TimeOnSpec = Column(Integer, default=0)
    TimeOnOffset = Column(Integer, default=0)


class WSJTX_Status(Base):
    __tablename__ = 'WSJTX_Status'
    id = Column(Integer, primary_key=True)
    Frequency = Column(Integer, default=0)
    Mode = Column(String, default="")
    DXCall = Column(String, default="")
    Report = Column(String, default="")
    TxMode = Column(String, default="")
    TxEnabled = Column(Boolean, default=False)
    Transmitting = Column(Boolean, default=False)
    Decoding = Column(Boolean, default=False)
    RxDF = Column(Integer, default=0)
    TxDF = Column(Integer, default=0)
    DECall = Column(String, default="")
    DEgrid = Column(String, default="")
    DXgrid = Column(String, default="")
    TxWatchdog = Column(Boolean, default=False)
    Submode = Column(String, default="")
    Fastmode = Column(Boolean, default=False)


class WSJTX_Decode(Base):
    __tablename__ = 'WSJTX_Decode'
    id = Column(Integer, primary_key=True)
    New = Column(Boolean, default=False)
    Time = Column(Integer, default=0)
    snr = Column(Integer, default=0)
    DeltaTime = Column(Float, default=0.0)
    DeltaFrequency = Column(Integer, default=0)
    Mode = Column(String, default="")
    Message = Column(String, default="")
    LowConfidence = Column(Boolean, default=False)
    OffAir = Column(Boolean, default=False)
