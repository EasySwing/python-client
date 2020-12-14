__version__ = "2.2.1"

try:
    from rfid.rfid import RFID
    from rfid.util import RFIDUtil
except RuntimeError:
    print("Must be used on Raspberry Pi")
