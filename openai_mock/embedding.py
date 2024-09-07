from typing import Dict, Any, List
import hashlib

class Embedding:
    @staticmethod
    def create(model: str, input: str, **kwargs) -> Dict[str, Any]:
        # Generate a deterministic mock embedding based on the input
        hash_object = hashlib.md5(input.encode())
        hash_hex = hash_object.hexdigest()
        mock_embedding = [int(hash_hex[i:i+2], 16) / 255 for i in range(0, 32, 2)]

        response = {
            "object": "list",
            "data": [
                {
                    "object": "embedding",
                    "embedding": mock_embedding,
                    "index": 0
                }
            ],
            "model": model,
            "usage": {
                "prompt_tokens": len(input.split()),
                "total_tokens": len(input.split())
            }
        }
        return response