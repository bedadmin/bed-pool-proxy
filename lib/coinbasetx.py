import binascii
import halfnode
import struct
import util
import cStringIO
from lib.settings import s as settings
import lib.logger
log = lib.logger.get_logger('coinbasetx')

class CoinbaseTransaction(halfnode.CTransaction):
    '''Construct special transaction used for coinbase tx.
    It also implements quick serialization using pre-cached
    scriptSig template.'''

    extranonce_type = '>Q'
    extranonce_placeholder = struct.pack(extranonce_type, int('f000000ff111111f', 16))
    extranonce_size = struct.calcsize(extranonce_type)

    def __init__(self, raw_data, extra):
        super(CoinbaseTransaction, self).__init__()
        log.debug("Got to CoinBaseTX")

        if len(self.extranonce_placeholder) != self.extranonce_size:
            raise Exception("Extranonce placeholder don't match expected length!")

        self.deserialize(cStringIO.StringIO(raw_data))
        tx_in = self.vin[0]
        tx_in._scriptSig_template = (tx_in.scriptSig, util.ser_string(extra))
        tx_in.scriptSig = tx_in._scriptSig_template[0] + self.extranonce_placeholder + tx_in._scriptSig_template[1]

        self._serialized = super(CoinbaseTransaction, self).serialize().split(self.extranonce_placeholder)

    def set_extranonce(self, extranonce):
        (part1, part2) = self.vin[0]._scriptSig_template
        self.vin[0].scriptSig = part1 + extranonce + part2
