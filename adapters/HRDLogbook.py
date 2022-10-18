from WSJTXClass import WSJTX_Logged
from HRDLogbookClass import HRDLogbook
# INSERT INTO hrd_logbook.TABLE_HRD_CONTACTS_V01 (COL_PRIMARY_KEY, COL_ADDRESS, COL_AGE, COL_A_INDEX, COL_ANT_AZ,
#                                                 COL_ANT_EL, COL_ANT_PATH, COL_ARRL_SECT, COL_BAND, COL_BAND_RX,
#                                                 COL_BIOGRAPHY, COL_CALL, COL_CHECK, COL_CLASS, COL_CNTY, COL_COMMENT,
#                                                 COL_CONT, COL_CONTACTED_OP, COL_CONTEST_ID, COL_COUNTRY, COL_CQZ,
#                                                 COL_DISTANCE, COL_DXCC, COL_EMAIL, COL_EQ_CALL, COL_EQSL_QSLRDATE,
#                                                 COL_EQSL_QSLSDATE, COL_EQSL_QSL_RCVD, COL_EQSL_QSL_SENT,
#                                                 COL_EQSL_STATUS, COL_FORCE_INIT, COL_FREQ, COL_FREQ_RX, COL_GRIDSQUARE,
#                                                 COL_HEADING, COL_IOTA, COL_ITUZ, COL_K_INDEX, COL_LAT, COL_LON,
#                                                 COL_LOTW_QSLRDATE, COL_LOTW_QSLSDATE, COL_LOTW_QSL_RCVD,
#                                                 COL_LOTW_QSL_SENT, COL_LOTW_STATUS, COL_MAX_BURSTS, COL_MODE,
#                                                 COL_MS_SHOWER, COL_MY_CITY, COL_MY_CNTY, COL_MY_COUNTRY, COL_MY_CQ_ZONE,
#                                                 COL_MY_GRIDSQUARE, COL_MY_IOTA, COL_MY_ITU_ZONE, COL_MY_LAT, COL_MY_LON,
#                                                 COL_MY_NAME, COL_MY_POSTAL_CODE, COL_MY_RIG, COL_MY_SIG,
#                                                 COL_MY_SIG_INFO, COL_MY_STATE, COL_MY_STREET, COL_NAME, COL_NOTES,
#                                                 COL_NR_BURSTS, COL_NR_PINGS, COL_OPERATOR, COL_OWNER_CALLSIGN, COL_PFX,
#                                                 COL_PRECEDENCE, COL_PROP_MODE, COL_PUBLIC_KEY, COL_QSLMSG, COL_QSLRDATE,
#                                                 COL_QSLSDATE, COL_QSL_RCVD, COL_QSL_RCVD_VIA, COL_QSL_SENT,
#                                                 COL_QSL_SENT_VIA, COL_QSL_VIA, COL_QSO_COMPLETE, COL_QSO_RANDOM,
#                                                 COL_QTH, COL_RIG, COL_RST_RCVD, COL_RST_SENT, COL_RX_PWR, COL_SAT_MODE,
#                                                 COL_SAT_NAME, COL_SFI, COL_SIG, COL_SIG_INFO, COL_SRX, COL_SRX_STRING,
#                                                 COL_STATE, COL_STATION_CALLSIGN, COL_STX, COL_STX_STRING, COL_SWL,
#                                                 COL_TEN_TEN, COL_TIME_OFF, COL_TIME_ON, COL_TX_PWR, COL_WEB,
#                                                 COL_USER_DEFINED_0, COL_USER_DEFINED_1, COL_USER_DEFINED_2,
#                                                 COL_USER_DEFINED_3, COL_USER_DEFINED_4, COL_USER_DEFINED_5,
#                                                 COL_USER_DEFINED_6, COL_USER_DEFINED_7, COL_USER_DEFINED_8,
#                                                 COL_USER_DEFINED_9, COL_CREDIT_GRANTED, COL_CREDIT_SUBMITTED,
#                                                 COL_ISMULTIPLIER, COL_ROVERLOCATION, COL_HRDCOUNTRYNO, COL_SUBMODE)
# VALUES (11850, null, 0, 12, 0, 0, null, null, '15m', '15m', null, '9Z4A', null, null, null, 'FT8 Sent: -14 Rcvd: -15',
#         'SA', null, null, 'Trinidad & Tobago', 9, 8896.108832125496, '90', null, null, null, null, 'R', 'R', null, 0,
#         21075566, 21075566, 'FK91', 275.72573658460277, null, 11, 1, 0, 0, null, '2022-08-18 00:00:00', 'R', 'Y', null,
#         0, 'FT8', null, 'Minsk', 'Belarus', 'Belarus', 16, 'KO33TX', null, 0, 53.979167, 27.625, 'Alex', '220141',
#         'Yaesu FTDX-3000', null, null, null, null, 'Anthony', null, 0, 0, 'EW1MY', null, '9Z4', null, null, null, null,
#         null, null, 'N', null, 'N', null, null, 'Y', 0, 'Maloney Gardens', null, '-15', '-14', 0, null, null, 81, null,
#         null, 0, null, null, 'EW1MY', 0, null, 0, 0, '2022-08-17 18:17:00', '2022-08-17 18:13:30', 100, null, null,
#         null, null, null, null, null, null, null, '5/8', null, null, null, null, null, '90', null);

COL_BAND = ['10m', '15m', '30m']
#
def col_band(frequency):
    return None

def col_cont(dxcall):
    return None

def col_country(dxcall):
    return None

def mapping(obj: WSJTX_Logged) -> HRDLogbook:
    hdr = {
        'COL_ADDRESS': "",
        'COL_AGE': 0,
        'COL_A_INDEX': 0,
        'COL_ANT_AZ': 0,
        'COL_ANT_EL': 0,
        'COL_ANT_PATH': "",
        'COL_ARRL_SECT': "",
        'COL_BAND': col_band(obj.DialFrequency),
        'COL_BAND_RX': col_band(obj.DialFrequency),
        'COL_BIOGRAPHY': "",
        'COL_CALL': obj.DXcall,
        'COL_CHECK': "",
        'COL_CLASS': "",
        'COL_CNTY': "",
        'COL_COMMENT': "",
        'COL_CONT': col_cont(obj.DXcall),
        'COL_CONTACTED_OP': "",
        'COL_CONTEST_ID': "",
        'COL_COUNTRY': col_country(obj.DXcall),
        'COL_CQZ': col_cqz(obj.DXcall),
        'COL_DISTANCE': col_distance(obj.DXcall),
        'COL_DXCC': col_dxcc((obj.DXcall),
        'COL_EMAIL': col_email((obj.DXcall),
        'COL_EQ_CALL': "",
        'COL_EQSL_QSLRDATE': "",
        'COL_EQSL_QSLSDATE': "",
        'COL_EQSL_QSL_RCVD': "N",
        'COL_EQSL_QSL_SENT': "N",
        'COL_EQSL_STATUS': "",
        'COL_FORCE_INIT': 0,
        'COL_FREQ': Column(INTEGER(11))
        'COL_FREQ_RX': Column(INTEGER(11))
        'COL_GRIDSQUARE': Column(String(12))
        'COL_HEADING': Column(Float(asdecimal=True))
        'COL_IOTA': Column(String(10), index=True)
        'COL_ITUZ': Column(INTEGER(11))
        'COL_K_INDEX': Column(Float(asdecimal=True))
        'COL_LAT': Column(Float(asdecimal=True))
        'COL_LON': Column(Float(asdecimal=True))
        'COL_LOTW_QSLRDATE': Column(DateTime)
        'COL_LOTW_QSLSDATE': Column(DateTime)
        'COL_LOTW_QSL_RCVD': Column(String(2))
        'COL_LOTW_QSL_SENT': Column(String(2))
        'COL_LOTW_STATUS': Column(String(255))
        'COL_MAX_BURSTS': Column(INTEGER(11))
        'COL_MODE': Column(String(10), index=True)
        'COL_MS_SHOWER': Column(String(32))
        'COL_MY_CITY': Column(VARCHAR(32))
        'COL_MY_CNTY': Column(String(32))
        'COL_MY_COUNTRY': Column(String(64))
        'COL_MY_CQ_ZONE': Column(INTEGER(11))
        'COL_MY_GRIDSQUARE': Column(String(12))
        'COL_MY_IOTA': Column(String(10))
        'COL_MY_ITU_ZONE': Column(INTEGER(11))
        'COL_MY_LAT': Column(Float(asdecimal=True))
        'COL_MY_LON': Column(Float(asdecimal=True))
        'COL_MY_NAME': Column(VARCHAR(64))
        'COL_MY_POSTAL_CODE': Column(String(24))
        'COL_MY_RIG': Column(VARCHAR(255))
        'COL_MY_SIG': Column(String(32))
        'COL_MY_SIG_INFO': Column(String(64))
        'COL_MY_STATE': Column(String(32))
        'COL_MY_STREET': Column(VARCHAR(64))
        'COL_NAME': Column(VARCHAR(128))
        'COL_NOTES': Column(LONGTEXT)
        'COL_NR_BURSTS': Column(INTEGER(11))
        'COL_NR_PINGS': Column(INTEGER(11))
        'COL_OPERATOR': Column(String(32))
        'COL_OWNER_CALLSIGN': Column(String(32))
        'COL_PFX': Column(String(32), index=True)
        'COL_PRECEDENCE': Column(String(32))
        'COL_PROP_MODE': Column(String(8))
        'COL_PUBLIC_KEY': Column(String(255))
        'COL_QSLMSG': Column(VARCHAR(255))
        'COL_QSLRDATE': Column(DateTime)
        'COL_QSLSDATE': Column(DateTime)
        'COL_QSL_RCVD': Column(String(2))
        'COL_QSL_RCVD_VIA': Column(String(2))
        'COL_QSL_SENT': Column(String(2))
        'COL_QSL_SENT_VIA': Column(String(2))
        'COL_QSL_VIA': Column(String(64))
        'COL_QSO_COMPLETE': Column(String(6))
        'COL_QSO_RANDOM': Column(INTEGER(11))
        'COL_QTH': Column(VARCHAR(64))
        'COL_RIG': Column(String(255))
        'COL_RST_RCVD': Column(String(32))
        'COL_RST_SENT': Column(String(32))
        'COL_RX_PWR': Column(Float(asdecimal=True))
        'COL_SAT_MODE': Column(String(32))
        'COL_SAT_NAME': Column(String(32))
        'COL_SFI': Column(Float(asdecimal=True))
        'COL_SIG': Column(String(32))
        'COL_SIG_INFO': Column(String(64))
        'COL_SRX': Column(INTEGER(11))
        'COL_SRX_STRING': Column(String(32))
        'COL_STATE': Column(String(32))
        'COL_STATION_CALLSIGN': Column(String(32))
        'COL_STX': Column(INTEGER(11))
        'COL_STX_STRING': Column(String(32))
        'COL_SWL': Column(INTEGER(11))
        'COL_TEN_TEN': Column(INTEGER(11))
        'COL_TIME_OFF': Column(DateTime)
        'COL_TIME_ON': Column(DateTime, index=True)
        'COL_TX_PWR': Column(Float(asdecimal=True))
        'COL_WEB': Column(String(128))
        'COL_USER_DEFINED_0': Column(String(64))
        'COL_USER_DEFINED_1': Column(String(64))
        'COL_USER_DEFINED_2': Column(String(64))
        'COL_USER_DEFINED_3': Column(String(64))
        'COL_USER_DEFINED_4': Column(String(64))
        'COL_USER_DEFINED_5': Column(String(64))
        'COL_USER_DEFINED_6': Column(String(64))
        'COL_USER_DEFINED_7': "",
        'COL_USER_DEFINED_8': "",
        'COL_USER_DEFINED_9': "",
        'COL_CREDIT_GRANTED': "",
        'COL_CREDIT_SUBMITTED': "",
        'COL_ISMULTIPLIER': "",
        'COL_ROVERLOCATION': "",
        'COL_HRDCOUNTRYNO': col_hrdcountryno(obj.DXcall),
        'COL_SUBMODE': ""
    }