from typing import Dict, Any, List

class Moderation:
    @staticmethod
    def create(input: str, **kwargs) -> Dict[str, Any]:
        response = {
            "id": "modr-mock123",
            "model": "text-moderation-001",
            "results": [
                {
                    "categories": {
                        "hate": False,
                        "hate/threatening": False,
                        "self-harm": False,
                        "sexual": False,
                        "sexual/minors": False,
                        "violence": False,
                        "violence/graphic": False
                    },
                    "category_scores": {
                        "hate": 0.01,
                        "hate/threatening": 0.01,
                        "self-harm": 0.01,
                        "sexual": 0.01,
                        "sexual/minors": 0.01,
                        "violence": 0.01,
                        "violence/graphic": 0.01
                    },
                    "flagged": False
                }
            ]
        }
        return response