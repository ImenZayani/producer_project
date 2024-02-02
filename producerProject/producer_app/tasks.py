from celery import shared_task, app
from .models import Message


#When a message needs to be processed, the producer app will publish a message to RabbitMQ
@shared_task
def process_data(text):
    """
    Processes the text data and creates a Message instance.

    Args:
        text: The text content of the message.

    Returns:
        The ID of the created Message instance.
    """
    message = Message.objects.create(text=text)
    # Publish the message to RabbitMQ
    publish_message.delay({'text': message.text})
    return message.id

@shared_task
def publish_message(celery_tasks):
    """
    Publishes a message to RabbitMQ for consumption by the consumer app.

    Args:
        message_data: A dictionary containing the message data.
    """
    app.send_task('consumer_app.tasks.consume_message', args=[celery_tasks])