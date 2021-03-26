''' A simple wrapper for pylibmc. It can be overwritten with simple hashing if necessary '''
from lib.settings import s as settings
import lib.logger
log = lib.logger.get_logger('Cache')

#import pylibmc

class Cache():
    def __init__(self):
        # Open a new connection
        #self.mc = pylibmc.Client([settings.MEMCACHE_HOST + ":" + str(settings.MEMCACHE_PORT)], binary=True)
        log.info("Caching initialized")

    def set(self, key, value, time):
        pass
        #return self.mc.set(settings.MEMCACHE_PREFIX + str(key), value, time)

    def get(self, key):
        pass
        #return self.mc.get(settings.MEMCACHE_PREFIX + str(key))

    def delete(self, key):
        pass
        #return self.mc.delete(settings.MEMCACHE_PREFIX + str(key))

    def exists(self, key):
        pass
        #return str(key) in self.mc.get(settings.MEMCACHE_PREFIX + str(key))
