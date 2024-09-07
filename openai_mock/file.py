from typing import Dict, Any, List

class File:
    @staticmethod
    def create(file: Any, purpose: str, **kwargs) -> Dict[str, Any]:
        response = {
            "id": "file-mock123",
            "object": "file",
            "bytes": 1234,
            "created_at": 1677652288,
            "filename": "mockfile.jsonl",
            "purpose": purpose,
        }
        return response

    @staticmethod
    def list(**kwargs) -> Dict[str, Any]:
        response = {
            "data": [
                {
                    "id": "file-mock123",
                    "object": "file",
                    "bytes": 1234,
                    "created_at": 1677652288,
                    "filename": "mockfile.jsonl",
                    "purpose": "fine-tune",
                }
            ],
            "object": "list"
        }
        return response

    @staticmethod
    def delete(file_id: str, **kwargs) -> Dict[str, Any]:
        response = {
            "id": file_id,
            "object": "file",
            "deleted": True
        }
        return response