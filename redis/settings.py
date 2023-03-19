# initialize Redis connection settings
REDIS_HOST = 'redis-14315.c302.asia-northeast1-1.gce.cloud.redislabs.com'
REDIS_PORT = 14315
REDIS_PASSWORD = "AW0fELxdUcjvpT41DL2RxC968OTnqaVr"
REDIS_DB = 0

# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"

# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25
