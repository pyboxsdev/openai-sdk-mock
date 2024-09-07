# OpenAI SDK Mock

This is a mock version of the Python OpenAI SDK that allows you to test your application without actually making any API calls to OpenAI.

This library keeps the same interface as the official OpenAI SDK, so you can use it as a drop-in replacement for testing purposes.

## Installation

You can install the OpenAI SDK Mock directly from GitHub using pip:

```bash
pip install git+https://github.com
```

## Usage

```python
from openai_sdk_mock import openai


response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ]
)

print(response['choices'][0]['message']['content'])
```

## Classes

- `openai.ChatCompletion`: Mock class for ChatCompletion.   |  Implemented
- `openai.Completion`: Mock class for Completion.   |  Implemented
- `openai.Embedding`: Mock class for Embedding.   |  Implemented
- `openai.File`: Mock class for File.   |  Not implemented
- `openai.Image`: Mock class for Image.   |  Not implemented
- `openai.Moderation`: Mock class for Moderation.   |  Not implemented
- `openai.Model`: Mock class for Model.   |  Implemented
- `openai.Organization`: Mock class for Organization.   |  Not implemented
- `openai.Thread`: Mock class for Thread.   |  Not implemented

## Limitations

- This library is not intended to be a full replacement for the official OpenAI SDK. It only implements a subset of the functionality.
