from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def square():
    try:
        num = int(request.args.get('number'))
        return jsonify({
            "practical": 9,
            "number": num,
            "square": num ** 2
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input, provide an integer"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# Request url: http://127.0.0.1:5001/square?number=5