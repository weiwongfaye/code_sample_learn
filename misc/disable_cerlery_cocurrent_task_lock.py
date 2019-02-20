import redis
import logging
from functools import wraps
REDIS_CLIENT = redis.Redis()
logger = logging.getLogger(__name__)

def single_instance_task(timeout=60*30):
    def task_exc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            have_lock = False
            key = "key"
            lock = REDIS_CLIENT.lock(key, timeout=timeout)
            try:
                have_lock = lock.acquire(blocking=False)
                if have_lock:
                    logger.info("accquire lock")
                    # return is needed otherwise it will return None by default
                    return func(*args, **kwargs)
            finally:
                if have_lock:
                    lock.release()
                    logger.info("release lock")

        return wrapper
    return task_exc

# example: @single_instance_task()
