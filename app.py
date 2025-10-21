# app.py
from flask import Flask, request, jsonify
import requests
import os
import time
from dotenv import load_dotenv

# Load file .env
load_dotenv()

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN")

def ask_ai(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "version": "ibm-granite/granite-3.3-8b-instruct",  # model versi
        "input": {"prompt": prompt}
    }

    # 1. Kirim request awal (buat job)
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 201:
        return f"Error: {response.status_code} - {response.text}"

    data = response.json()
    prediction_id = data["id"]

    # 2. Polling sampai job selesai
    get_url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
    for _ in range(20):  # maksimal 20x cek
        result = requests.get(get_url, headers=headers).json()
        status = result["status"]

        if status == "succeeded":
            return result["output"][0]
        elif status == "failed":
            return "Generation failed."
        
        time.sleep(1)  # tunggu 1 detik sebelum cek lagi

    return "Timeout: model terlalu lama merespon."


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Missing question field'}), 400
    
    question = data['question']
    answer = ask_ai(question)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
