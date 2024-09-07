from .chat_completion import ChatCompletion
from .completion import Completion
from .embedding import Embedding
from .file import File
from .image import Image
from .moderation import Moderation
from .model import Model
from .organization import Organization
from .thread import Thread

class OpenAI:
    ChatCompletion = ChatCompletion
    Completion = Completion
    Embedding = Embedding
    File = File
    Image = Image
    Moderation = Moderation
    Model = Model
    Organization = Organization
    Thread = Thread

openai = OpenAI()