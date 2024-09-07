import json
from typing import List, Dict, Any

class ChatCompletion:
    @staticmethod
    def create(model: str, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        # Generate a mock response based on the input
        last_message = messages[-1]["content"]
        response_content = f"This is a mock response to: '{last_message}'. The model {model} was used for this chat completion."

        response = {
            "id": "chatcmpl-123",
            "object": "chat.completion",
            "created": 1677652288,
            "model": model,
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response_content
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": len(" ".join([m["content"] for m in messages]).split()),
                "completion_tokens": len(response_content.split()),
                "total_tokens": len(" ".join([m["content"] for m in messages]).split()) + len(response_content.split())
            }
        }
        return response