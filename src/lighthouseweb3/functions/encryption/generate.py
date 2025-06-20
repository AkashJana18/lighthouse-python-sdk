import secrets
from typing import Any, Dict, List

from secretsharing import SecretSharer


def _generate_master_key() -> str:
    # Generate a 32-byte secure random key and return it as a hex string
    return secrets.token_hex(32)


def _split_key(master_key: str, threshold: int, key_count: int) -> List[Dict[str, str]]:
    # Split the master key into key shards
    shares = SecretSharer.split_secret(master_key, threshold, key_count)

    # Convert to desired format: { key: <shard>, index: <index> }
    key_shards = []
    for share in shares:
        parts = share.split('-')
        index = parts[0]
        key = '-'.join(parts[1:])
        key_shards.append({"key": key, "index": index})

    return key_shards


async def generate(threshold: int = 3, keyCount: int = 5) -> Dict[str, Any]:
    if keyCount < threshold:
        raise ValueError("keyCount must be greater than or equal to threshold")

    master_key = _generate_master_key()
    key_shards = _split_key(master_key, threshold, keyCount)

    return {
        "masterKey": master_key,
        "keyShards": key_shards
    }
