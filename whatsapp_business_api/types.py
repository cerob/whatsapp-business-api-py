from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MessageTypes(Enum):
    text = 'text'
    image = 'image'
    location = 'location'
    contacts = 'contacts'
    interactive = 'interactive'


class OutgoingTextPayload(BaseModel):
    preview_url: bool
    body: str


class ApiRequestPayload(BaseModel):
    messaging_product: str = 'whatsapp'
    recipient_type: str = 'individual'
    to: str
    type: MessageTypes
    text: Optional[OutgoingTextPayload]
