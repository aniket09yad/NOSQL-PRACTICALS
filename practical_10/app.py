from flask import Flask, request, jsonify

app = Flask(__name__)

def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(digit) ** order for digit in str(num))

@app.route('/armstrong', methods=['GET'])
def armstrong():
    try:
        num = int(request.args.get('number'))
        return jsonify({
            "practical": 10,
            "number": num,
            "is_armstrong": is_armstrong(num)
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input, provide an integer"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)

# Request url: http://127.0.0.1:5002/armstrong?number=153