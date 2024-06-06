# hello-redis
Like a `hello-world`, but for Redis.

## Install Redis  
We will run Redis in a Docker container. If you need more help to get started, please follow instructions available in Docker Hub: https://hub.docker.com/_/redis

```bash
# Pull image
docker pull redis

# Create container
docker run -d -p 6379:6379 --name my-redis redis:latest

# Enter the container in interactive mode
docker exec -it my-redis redis-cli

# https://redis.io/docs/management/security/
CONFIG SET protected-mode no
```

To start the container again:

```bash
# Start the container already created
docker start my-redis

# Enter into the redis CLI
docker exec -it my-redis redis-cli
```

## Redis CLI

```bash
# Create examples
SET color "blue"
RPUSH animals "dog" "cat" "bird"

# List the available databases
# https://stackoverflow.com/questions/12802726/how-to-list-all-redis-databases
CONFIG GET databases

# Move between databases
SELECT 0 
SELECT 1

# Show what is in each database
INFO keyspace

# List the keys
KEYS *

# Print the contents of the list on index x
LINDEX animals 0
LINDEX animals 1

# Print data type of key
TYPE color
TYPE animals

# Get the value of specific key
GET color

# Delete all keys from one database
SELECT ...
FLUSHDB

# Delete all keys from all databases
FLUSHALL
```
