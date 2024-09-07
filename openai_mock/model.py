from typing import Dict, Any, List

class Model:
    _models = [
        "gpt-4", "gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314",
        "gpt-3.5-turbo", "gpt-3.5-turbo-0301",
        "text-davinci-003", "text-davinci-002", "text-curie-001",
        "text-babbage-001", "text-ada-001",
        "davinci", "curie", "babbage", "ada",
        "code-davinci-002", "code-cushman-001",
        "text-davinci-edit-001", "code-davinci-edit-001",
        "whisper-1",
        "text-embedding-ada-002",
        "text-search-ada-doc-001",
        "text-moderation-stable", "text-moderation-latest"
    ]

    @staticmethod
    def list(**kwargs) -> Dict[str, Any]:
        response = {
            "object": "list",
            "data": [
                {
                    "id": model,
                    "object": "model",
                    "created": 1686935002,
                    "owned_by": "openai" if "gpt" in model or "text-" in model or "code-" in model else "openai-internal",
                    "permission": [],
                    "root": model,
                    "parent": None,
                }
                for model in Model._models
            ]
        }
        return response

    @staticmethod
    def retrieve(model: str, **kwargs) -> Dict[str, Any]:
        if model not in Model._models:
            raise ValueError(f"Model '{model}' not found")
        
        response = {
            "id": model,
            "object": "model",
            "created": 1686935002,
            "owned_by": "openai" if "gpt" in model or "text-" in model or "code-" in model else "openai-internal",
            "permission": [],
            "root": model,
            "parent": None,
        }
        return response