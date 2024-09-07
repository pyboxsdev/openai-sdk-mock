from typing import Dict, Any, List

class Thread:
    @staticmethod
    def create(messages: List[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        response = {
            "id": "thread_mock123",
            "object": "thread",
            "created_at": 1677652288,
            "metadata": {}
        }
        return response

    @staticmethod
    def retrieve(thread_id: str, **kwargs) -> Dict[str, Any]:
        response = {
            "id": thread_id,
            "object": "thread",
            "created_at": 1677652288,
            "metadata": {}
        }
        return response

    @staticmethod
    def delete(thread_id: str, **kwargs) -> Dict[str, Any]:
        response = {
            "id": thread_id,
            "object": "thread.deleted",
            "deleted": True
        }
        return response