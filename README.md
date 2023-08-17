# A basic linear algebra interpreter web service
A small social media back-end whose functionality includes:

- a friend request system;

- an activity stream application, i.e., news feed;

- an Asynchronous email notification system whereby a user recieves an email aynchronously when the user receives a friend request;

- a basic linear algebra interpeter whereby a user can make lineara algebra computations over the network;

- a way for users to create book studies; and

- a way for users to chat within a book study group.


## Running the program

### Dependencies
#### docker
```
sudo pacman -S docker
```

#### RabbitMQ
```
docker pull rabbitmq
```

#### Celery
```
sudo pacman -S python-celery
```
#### Redis
```
$ docker pull redis
$ pip install redis ;; or
$ sudo pacman -S python-redis
```

#### Memcache
```
$ docker pull memcached
$ sudo pacman -S python-pymemcache ;; or
$ pip install pymemcache
```

### Required servers

#### Django
```
python manage.py runserver
```

#### RabbitMQ
```
sudo docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

#### Celery
```
celery -A server worker -l info
```

#### Redis
```
docker run -it --rm --name redis -p 6379:6379 redis
```

#### Memcached
```
docker run -it --rm --name memcached -p 11211:11211 memcached -m 64
```
### Usage
You can use the python client in `src/python_client/client.py` to call the api.

Once you have at least a user or two you can use the bash script in `src/server/call_api.sh` but you will need to replace the user `jobpink` and the password with a new user of your choice.

To run the bash script:

```
$ chmod +x call_api.sh
$ ./call_api.sh
```

## Architecture
The architecture consists of a server that gets data in a cache if the data is in the cache otherwise it gets data from a database; moreover, it consists of a message broker, and a worker server that gets the messages from the message queue that the broker manages. By using the cache, in theory, we improve the performance and by using the message broker and worker we process asynchronous tasks such as sending an email notification to a given user who has received a friend request; this setup can also be used to send notifications to the user whose post has been liked.

```mermaid
graph TD;
    Client-->Server;
    Server-->Cache;
    Server-->Database;
    Server-->Message-Broker;
    Message-Broker-->Worker;
    Worker-->Message-Broker;
```

Specifically, the architecture consists of this:

```mermaid
graph TD;
    Client-->Django;
    Django-->Memcache;
    Django-->RabbitMQ;
    RabbitMQ-->Celery;
    Celery-->RabbitMQ;
    
```
