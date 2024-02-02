# producer_project

Cloning the project: git clone <url>

Creating Virtual Environments: python3 -m venv venv
    - Activate the environment: (Windows)
        venv\Scripts\activate
    

Installing Dependencies: pip install django celery django-rest-framework django-celery-results requests

Verifying Installations: pip list

Creating Django Project: django-admin startproject producerProject

Creating an App: python manage.py startapp producer_app

Running Migrations: python manage.py makemigrations python manage.py migrate

Creating a Superuser: python manage.py createsuperuser

Starting the Server: python manage.py runserver

Setting Up RabbitMQ: - To use Celery, we need to create a RabbitMQ user, a virtual host, and grant that user access to that virtual host:
Creating a new user via the web interface:
1. Access the users page in the RabbitMQ web interface.
2. Click on the "Create User" button.
3. Enter the username and password for the user.
4. Select the virtual hosts on which the user will have privileges.
5. Click on the "Create" button.
(Alternative Method) Creating a new user via the rabbitmqctl command:
- Execute the following command:
rabbitmqctl add_user <username> <password>
- Grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.
    rabbitmqctl set_user_tags username administrator
- To assign privileges to the user, execute the following command:
    rabbitmqctl set_permissions -p <vhost> <username> <configure> <write> <read>
    example: rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
- Execute this command in cmd:
    rabbitmq-plugins enable rabbitmq_management
- Open the browser and navigate to: http://localhost:15672/


- Creating a Celery Task Configuring Celery Running the Celery Worker:
    celery -A producerProject worker -l info

Installing Django REST Framework: 
    pip install djangorestframework

To create a webhook receiver view that accepts a POST request: 
    - First, install the djangorestframework-api-key package: 
        pip install djangorestframework-api-key

    TO TEST ON POSTMAN WEBHOOK the URL:   http://127.0.0.1:8000/api/webhook/
    - Create a New Request
    - Click on the "+ New" button and select "Request". 
    - Name your request and save it to a collection for easier access later.
    - In the request tab, select "POST" as the request method from the dropdown menu. 
    - Enter your API endpoint URL in the request URL field.
    - Go to the "Headers" tab and enter "Authorization" as the key and "Api-Key <your-api-key>" as the value. Replace "<your-api-key>" with the actual API key you created.
    - Send Request