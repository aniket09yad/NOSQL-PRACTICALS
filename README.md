# Flask College Practicals

This repository contains Flask APIs for college practical exams.

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