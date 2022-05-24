def send_message_ep_uri(phone_number_id: str) -> str:
    return 'https://graph.facebook.com/v13.0/{FROM_PHONE_NUMBER_ID}/messages'.format(
        FROM_PHONE_NUMBER_ID=phone_number_id)
