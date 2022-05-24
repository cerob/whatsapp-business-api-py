# Whatsapp Business Cloud API

This repository is a wrapper for Meta's Whatsapp Business Cloud API.

## Use

```python
from whatsapp_business_api import WhatsappAPI

phone_number_id = 'YOUR_SENDER_ID'
access_token = 'YOUR_ACCESS_TOKEN'

w = WhatsappAPI(phone_number_id=phone_number_id,
                access_token=access_token)

w.send_text_message(to='49xxxxxxxxxxx', message='This is a test!')
```
