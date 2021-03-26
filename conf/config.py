'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.

This is already setup with sane values for solomining.
You NEED to set the parameters in BASIC SETTINGS
'''
# ******************** BASIC SETTINGS ***************
# These are the MUST BE SET parameters!

COINDAEMON_TRUSTED_HOST = 'localhost'
COINDAEMON_TRUSTED_PORT = 8778
COINDAEMON_TRUSTED_USER = 'bed666'
COINDAEMON_TRUSTED_PASSWORD = 'bedcoin123'

COINDAEMON_HAS_SEGWIT = True

# ******************** GENERAL SETTINGS ***************
# Set process name of twistd, much more comfortable if you run multiple processes on one machine
STRATUM_MINING_PROCESS_NAME= 'tsm'

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = 'bedpool.log'
LOGLEVEL = 'INFO'
# Logging Rotation can be enabled with the following settings
# It if not enabled here, you can set up logrotate to rotate the files.
# For built in log rotation set LOG_ROTATION = True and configure the variables
LOG_ROTATION = True
LOG_SIZE = 204857600 # Rotate every 10M
LOG_RETENTION = 10 # Keep 10 Logs

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 300

# ******************** TRANSPORTS *********************
# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Disable the example service
ENABLE_EXAMPLE_SERVICE = False

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333

# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None

# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None

# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None

# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None

#TCP_PROXY_PROTOCOL = True

# Salt used for Block Notify Password
PASSWORD_SALT = 'test_crazy_string'

# ******************** Database  *********************
DATABASE_DRIVER = 'mysql'       # Options: none, sqlite, postgresql or mysql
DATABASE_EXTEND = True         # SQLite and PGSQL Only!

# SQLite
DB_SQLITE_FILE = 'pooldb.sqlite'
# Postgresql
DB_PGSQL_HOST = 'localhost'
DB_PGSQL_DBNAME = 'pooldb'
DB_PGSQL_USER = 'pooldb'
DB_PGSQL_PASS = '**empty**'
DB_PGSQL_SCHEMA = 'public'
# MySQL
DB_MYSQL_HOST = 'localhost'
DB_MYSQL_DBNAME = 'pooldb'
DB_MYSQL_USER = 'debian-sys-maint'
DB_MYSQL_PASS = 'zHQKy9ZlFrD71QUx'
DB_MYSQL_PORT = 3306            # Default port for MySQL

# ******************** Pool Settings *********************

# User Auth Options
USERS_AUTOADD = False           # Automatically add users to database when they connect.
                                # This basically disables User Auth for the pool.
USERS_CHECK_PASSWORD = False    # Check the workers password? (Many pools don't)

# Transaction Settings
COINBASE_EXTRAS = '/stratumFun/'           # Extra Descriptive String to incorporate in solved blocks
ALLOW_NONLOCAL_WALLET = False               # Allow valid, but NON-Local wallet's

# Coin Daemon communication polling settings (In Seconds)
PREVHASH_REFRESH_INTERVAL = 15   # How often to check for new Blocks
                                #   If using the blocknotify script (recommended) set = to MERKLE_REFRESH_INTERVAL
                                #   (No reason to poll if we're getting pushed notifications)
MERKLE_REFRESH_INTERVAL = 60    # How often check memorypool
                                #   How often to check for new transactions to be added to the block
                                #   This effectively resets the template and incorporates new transactions.
                                #   This should be "slow"

INSTANCE_ID = 31                # Used for extranonce and needs to be 0-31


# Pool Target (Base Difficulty)
POOL_TARGET = 65500             # Pool-wide difficulty target int >= 1
VDIFF_MIN_TARGET = 65500        #  Minimum Target difficulty
VDIFF_MAX_TARGET = 100000000    # Maximum Target difficulty

# ******************** Worker Ban Options *********************
ENABLE_WORKER_BANNING = True    # Enable/disable temporary worker banning
WORKER_CACHE_TIME = 600         # How long the worker stats cache is good before we check and refresh
WORKER_BAN_TIME = 300           # How long we temporarily ban worker
INVALID_SHARES_PERCENT = 50     # Allow average invalid shares vary this % before we ban


######## IRC BOT ##################
BOT_ENABLED = False

ADMIN_PASSWORD_SHA256 = '67579321fe6c041e3815232b35eff4b856cc1173e395f9a68e878ffc47816aa2'
