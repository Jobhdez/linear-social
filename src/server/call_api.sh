#!/bin/bash

#!/bin/bash

# Set the URL for the Django API
URL='http://127.0.0.1:8000/api/'

# Function to check if the Django server is running
check_server() {
    if curl -s --head $URL | grep "HTTP/1.1 200 OK" > /dev/null; then
        return 0
    else
        return 1
    fi
}

start_server() {
    echo "Starting Django server..."
    gnome-terminal -- bash -c "python manage.py runserver 0.0.0.0:8000; exec bash"
}

# Function to start RabbitMQ Docker container
start_rabbitmq() {
    echo "Starting RabbitMQ Docker container..."
    gnome-terminal -- bash -c "sudo docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management; exec bash"
}

# Function to start Celery worker
start_celery() {
    echo "Starting Celery worker..."
    gnome-terminal -- bash -c "celery -A server worker -l info; exec bash"
}

# Check if the Django server is running
if check_server; then
    echo "Django server is already running."
else
    start_server
fi

# Check if RabbitMQ Docker container is running
if sudo docker ps -a --format "{{.Names}}" | grep -q "rabbitmq"; then
    echo "RabbitMQ Docker container is already running."
else
    start_rabbitmq
fi

# Start Celery worker
start_celery


# Prompt for user credentials
read -p "Enter username for user 1: " user1_username
read -s -p "Enter password for user 1: " user1_password
echo

read -p "Enter email for user 1: " user1_email
echo

read -p "Enter first_name for user 1: " user1_first_name
echo

read -p "Enter linear algebra expression: " linear_algebra_expression

# Call the functions
register_result1=$(python -c "from src.python_client.client import register; print(register('$user1_password', '$user1_username', '$user1_first_name', '$user1_email'))")

login_result1=$(python -c "from src.python_client.client import login; print(login('$user1_username', '$user1_password'))")

request_friend_result=$(python -c "from src.python_client.client import request_friend; print(request_friend('$user1_username', 'jobpink', 'hello123'))")

accept_friend_result=$(python -c "from src.python_client.client import accept; print(accept('$user1_username', 'jobpink', 'hello123'))")

compute_result=$(python -c "from src.python_client.client import compute; print(compute('$linear_algebra_expression', 'jobpink', 'hello123'))")

dashboard_result=$(python -c "from src.python_client.client import dashboard; print(dashboard('jobpink', 'hello123'))")

# Print login results
echo "register result for user 1: $register_result1"
echo "Login result for user 1: $login_result1"
echo "friend request result for user 1: $request_friend_result"
echo "accept friend result: $accept_friend_result"
echo "compute algebra result: $compute_result"
echo "dashboard of jobpink: $dashboard_result"
