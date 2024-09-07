from typing import Dict, Any

class Completion:
    @staticmethod
    def create(model: str, prompt: str, **kwargs) -> Dict[str, Any]:
        # Generate a mock response based on the input
        response_text = f"This is a mock completion response to: '{prompt}'. The model {model} was used for this text completion."

        response = {
            "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
            "object": "text_completion",
            "created": 1589478378,
            "model": model,
            "choices": [
                {
                    "text": response_text,
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": "length"
                }
            ],
            "usage": {
                "prompt_tokens": len(prompt.split()),
                "completion_tokens": len(response_text.split()),
                "total_tokens": len(prompt.split()) + len(response_text.split())
            }
        }
        return response