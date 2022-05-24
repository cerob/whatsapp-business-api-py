from typing import Dict, Union

import requests

from .endpoints import send_message_ep_uri
from .exceptions import SendingMessageFailedException
from .types import ApiRequestPayload, OutgoingTextPayload


class WhatsappAPI:

    def __init__(self, phone_number_id: Union[int, str], access_token: str) -> None:
        self.__phone_number_id: str = str(phone_number_id).replace(' ',
                                                                   '').replace('+', '')
        self.__access_token: str = access_token
        self.__headers: Dict[str, str] = {
            'Authorization':
                'Bearer {ACCESS_TOKEN}'.format(ACCESS_TOKEN=self.__access_token),
            'Content-Type':
                'application/json',
        }

    def send_text_message(self, to: str, message: str) -> None:
        payload = ApiRequestPayload(to=to,
                                    type='text',
                                    text=OutgoingTextPayload(preview_url=True,
                                                             body=message))

        r = requests.post(send_message_ep_uri(self.__phone_number_id),
                          headers=self.__headers,
                          data=payload.json())

        if r.status_code != 200:
            raise SendingMessageFailedException(r.status_code)
