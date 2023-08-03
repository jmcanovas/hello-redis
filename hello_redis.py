import redis

# This is a "hello-world" example for Redis

# --- Connect to redis in local container
client = redis.Redis(host='localhost', port=6379, db=5, charset="utf-8", decode_responses=True)

# https://stackoverflow.com/a/25745110/10152848


# --- Example 1
# Set a key-value pair
client.set('key_fruit', 'value_apple')

# Get a value
value_1 = client.get('key_fruit')

# Print the value to the console
print('This is example 1')
print(f'Print value: {value_1}')
print(f'Type of the value is: {type(value_1)}')
print(' ')

# --- Example 2: Redis lists
# Append to a Redis list
# https://redis.io/commands/rpush/
client.rpush('letters', 'a', 'b', 'c')

# Get a value
value_2 = client.lrange('letters', 0, -1)

# Print the value to the console
print('This is example 2')
print(f'Print value: {value_2}')
print(f'Type of the value is: {type(value_2)}')

