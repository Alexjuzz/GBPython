import redis

with redis.Redis() as redis_server:
    redis_server.lpush("Queue", 4)
