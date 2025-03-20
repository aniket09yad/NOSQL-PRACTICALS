import redis
import json
from flask import Flask, jsonify

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Preload user data into Redis
users = {
    "1": {"name": "John Doe", "age": 25, "email": "john@example.com"},
    "2": {"name": "Jane Smith", "age": 30, "email": "jane@example.com"},
    "3": {"name": "Alice Brown", "age": 28, "email": "alice@example.com"}
}

# Store users in Redis
for user_id, user_data in users.items():
    r.set(user_id, json.dumps(user_data))  # Convert dict to JSON string

# Flask API
app = Flask(__name__)

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Fetch user data from Redis
    user_data = r.get(user_id)
    
    if user_data is None:
        return jsonify({"error": "User not found"}), 404  # Return 404 if user not in Redis
    
    return jsonify(json.loads(user_data))  # Convert JSON string back to dictionary

if __name__ == '__main__':
    app.run(debug=True)

# Request url ex
# http://127.0.0.1:5000/api/users/1
# http://127.0.0.1:5000/api/users/2
