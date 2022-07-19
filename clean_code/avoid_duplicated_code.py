
"""
Example of using decorators to avoid code duplication.
"""


def log_message_delivery(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Failed to deliver message to: {e}")
        else:
            logger.info("Message was delivered successfully")
        return wrapper


@log_message_delivery
def send_email(email_address):
    # Logic related to email delivery
    print(email_address)


@log_message_delivery
def send_sms(phone_number):
    # Logic related to sms delivery
    print(phone_number)
