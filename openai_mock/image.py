from typing import Dict, Any, List

class Image:
    @staticmethod
    def create(prompt: str, n: int = 1, size: str = "1024x1024", **kwargs) -> Dict[str, Any]:
        response = {
            "created": 1677652288,
            "data": [
                {
                    "url": f"https://mock-image-url.com/image{i}.jpg"
                } for i in range(n)
            ]
        }
        return response

    @staticmethod
    def create_edit(image: Any, prompt: str, n: int = 1, size: str = "1024x1024", **kwargs) -> Dict[str, Any]:
        response = {
            "created": 1677652288,
            "data": [
                {
                    "url": f"https://mock-image-edit-url.com/image{i}.jpg"
                } for i in range(n)
            ]
        }
        return response

    @staticmethod
    def create_variation(image: Any, n: int = 1, size: str = "1024x1024", **kwargs) -> Dict[str, Any]:
        response = {
            "created": 1677652288,
            "data": [
                {
                    "url": f"https://mock-image-variation-url.com/image{i}.jpg"
                } for i in range(n)
            ]
        }
        return response