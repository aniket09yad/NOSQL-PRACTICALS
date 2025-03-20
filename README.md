# Flask College Practicals

This repository contains Flask APIs for college practical exams.

## Practical 7: Redis Cache API

This API demonstrates using Redis as a cache for user data, accessed via a Flask API.

### Redis Configuration
This practical uses Redis as a data store:
- The main Redis server runs on the default port 6379
- A slave Redis instance can be configured on port 6380 for redundancy
- User data is preloaded into Redis at application startup

### Redis Server Setup
To set up the Redis server in slave mode for redundancy (optional):
```bash
redis-server --port 6380 --slaveof 127.0.0.1 6379
```

This command:
- Starts a Redis server on port 6380
- Configures it as a slave (replica) of the master Redis instance running on localhost (127.0.0.1) port 6379
- Automatically synchronizes data from the master to this slave instance

### Application Logic
The application works as follows:
1. Connects to Redis on localhost:6379
2. Preloads sample user data into Redis (converting Python dictionaries to JSON strings)
3. Creates a Flask API with a route to fetch user data by ID
4. When a request is made, retrieves the JSON data from Redis and returns it

### Running the API
To run the Redis Cache API:
```bash
cd practical_7
python app.py
```
API will be available at: http://127.0.0.1:5000/api/users/1

### API Details
- **Endpoint:** `/api/users/<user_id>`
- **Method:** `GET`
- **Description:** Retrieves user data from Redis cache based on the provided user ID

### Example Usage
To retrieve user data for user with ID 1:
```
http://127.0.0.1:5000/api/users/1
```

### Example Response
```json
{
    "name": "John Doe",
    "age": 25,
    "email": "john@example.com"
}
```

### Error Response
If the user is not found:
```json
{
    "error": "User not found"
}
```
(with 404 status code)

### Key Implementation Details
- User data is stored in Redis as JSON strings
- When retrieved, the JSON strings are converted back to Python dictionaries
- The implementation demonstrates a common pattern in modern web applications:
  using Redis as a fast in-memory cache for frequently accessed data

This API demonstrates using Redis as a cache for user data, accessed via a Flask API.

### Redis Configuration
This practical uses Redis as a data store:
- The main Redis server runs on the default port 6379
- A slave Redis instance can be configured on port 6380 for redundancy
- User data is preloaded into Redis at application startup

### Redis Server Setup
To set up the Redis server in slave mode for redundancy (optional):
```bash
redis-server --port 6380 --slaveof 127.0.0.1 6379
```

This command:
- Starts a Redis server on port 6380
- Configures it as a slave (replica) of the master Redis instance running on localhost (127.0.0.1) port 6379
- Automatically synchronizes data from the master to this slave instance

### Application Logic
The application works as follows:
1. Connects to Redis on localhost:6379
2. Preloads sample user data into Redis (converting Python dictionaries to JSON strings)
3. Creates a Flask API with a route to fetch user data by ID
4. When a request is made, retrieves the JSON data from Redis and returns it

### API Details
- **Endpoint:** `/api/users/<user_id>`
- **Method:** `GET`
- **Description:** Retrieves user data from Redis cache based on the provided user ID

### Example Usage
To retrieve user data for user with ID 1:
```
http://127.0.0.1:5000/api/users/1
```

### Example Response
```json
{
    "name": "John Doe",
    "age": 25,
    "email": "john@example.com"
}
```

### Error Response
If the user is not found:
```json
{
    "error": "User not found"
}
```
(with 404 status code)

### Key Implementation Details
- User data is stored in Redis as JSON strings
- When retrieved, the JSON strings are converted back to Python dictionaries
- The implementation demonstrates a common pattern in modern web applications:
  using Redis as a fast in-memory cache for frequently accessed data

## Practical 9: Square API

This API calculates the square of a given number.
- **Endpoint:** `/square`
- **Method:** `GET`
- **Example Usage:**
```
http://127.0.0.1:5001/square?number=5
```
- **Response:**
```json
{
    "practical": 9,
    "number": 5,
    "square": 25
}
```

## Practical 10: Armstrong Number API

This API checks whether a given number is an Armstrong number.
- **Endpoint:** `/armstrong`
- **Method:** `GET`
- **Example Usage:**
```
http://127.0.0.1:5002/armstrong?number=153
```
- **Response:**
```json
{
    "practical": 10,
    "number": 153,
    "is_armstrong": true
}
```

## Installation and Setup

Follow these steps to set up and run the project:

1. Clone the Repository
```bash
git clone https://github.com/hrisabhy/flask-college-practicals.git
cd flask-college-practicals
```

2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Running the APIs
   
   Run Practical 9 (Square API)
   ```bash
   cd practical_9
   python app.py
   ```
   API will be available at: http://127.0.0.1:5001/square?number=5

   You can exit the script with Ctrl+C

   Run Practical 10 (Armstrong API)
   ```bash
   cd ../practical_10
   python app.py
   ```
   API will be available at: http://127.0.0.1:5002/armstrong?number=153