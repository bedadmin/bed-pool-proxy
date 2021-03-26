import time
import hashlib
from lib.settings import s as settings
import lib.logger
log = lib.logger.get_logger('DB_Mysql')

import pymysql
import DB_Mysql

class DB_Mysql_Extended(DB_Mysql.DB_Mysql):
    def __init__(self):
        DB_Mysql.DB_Mysql.__init__(self)

    def import_shares(self, data):
        # Data layout
        # 0: worker_name,
        # 1: block_header,
        # 2: block_hash,
        # 3: difficulty,
        # 4: timestamp,
        # 5: is_valid,
        # 6: ip,
        # 7: self.block_height,
        # 8: self.prev_hash,
        # 9: invalid_reason,
        # 10: share_diff

        for v in data:
            d = {'time':v[4]*1000,'host':v[6],'worker':v[0],'is_valid':v[5],'is_accepted':0,'reason':v[9],'solution':v[2],
                                'block_height':v[7],'prev_block_hash':v[8],'ua':'','diff':v[3]}

            self.execute_nb("insert into shares2 " +\
                "(submit_at,host,worker,is_valid,is_accepted,reason,solution,block_height,prev_block_hash,difficulty) " +\
                "VALUES (%(time)s,%(host)s,%(worker)s,%(is_valid)s,%(is_accepted)s,%(reason)s,%(solution)s,%(block_height)s,%(prev_block_hash)s,%(diff)s)", d)

    def found_block(self, v):
        data = {'time':v[4]*1000,'host':v[6],'worker':v[0],'is_valid':True,'is_accepted':v[5],'reason':'','solution':v[2],
                                'block_height':v[7],'prev_block_hash':v[8],'ua':'','diff':v[3]}
        self.execute_nb("insert into shares2 " +\
                "(submit_at,host,worker,is_valid,is_accepted,reason,solution,block_height,prev_block_hash,difficulty) " +\
                "VALUES (%(time)s,%(host)s,%(worker)s,%(is_valid)s,%(is_accepted)s,%(reason)s,%(solution)s,%(block_height)s,%(prev_block_hash)s,%(diff)s)", data)

    def check_tables(self):
        log.debug("Checking Tables")
        if settings.DATABASE_EXTEND == True :
                self.execute_nb("create table if not exists shares2" +\
                        "(id bigint AUTO_INCREMENT, host varchar(255), worker varchar(255), is_valid TINYINT, is_accepted TINYINT, reason TEXT, " +\
                        "block_height INTEGER, prev_block_hash varchar(255), difficulty Decimal(10,2), solution varchar(64), submit_at BIGINT, PRIMARY KEY (id))")
                
                #self.execute_nb("CREATE INDEX if not exists shares_time_worker ON shares(submit_at,worker)")
                #self.execute_nb("CREATE INDEX if not exists shares_upstreamresult ON shares(is_accepted)")
        else :
                self.execute_nb("create table if not exists shares2" + \
                        "(submit_at DATETIME,host TEXT, worker TEXT, is_valid INTEGER, is_accepted INTEGER, reason TEXT, solution TEXT)")
