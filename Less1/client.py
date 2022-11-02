import redis


with redis.Redis() as redis_client:
    value = redis_client.rpop("Queue")


print(int(value))