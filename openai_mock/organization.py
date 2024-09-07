from typing import Dict, Any, List

class Organization:
    @staticmethod
    def list(**kwargs) -> Dict[str, Any]:
        response = {
            "object": "list",
            "data": [
                {
                    "id": "org-mock123",
                    "object": "organization",
                    "name": "Mock Organization",
                    "personal": False,
                    "created": 1677652288
                }
            ]
        }
        return response