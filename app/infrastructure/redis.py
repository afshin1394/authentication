
from typing import Optional

import aioredis




class RedisClient:
    _instance: Optional['RedisClient'] = None

    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.redis = None

    @classmethod
    async def get_instance(cls, redis_url: str = 'redis://localhost:6379/0') -> 'RedisClient':
        if cls._instance is None:
            cls._instance = RedisClient(redis_url)
            cls._instance.redis = await aioredis.from_url(redis_url, decode_responses=True)
        return cls._instance

    async def invalidate_keys(self, keys: list):
        if not keys:
            return
        await self.redis.delete(*keys)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value, expire: int = 3600):
        await self.redis.set(key, value, ex=expire)
