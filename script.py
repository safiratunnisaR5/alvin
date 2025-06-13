import time
import sys
import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday</title>
    <style>
        body {
            background-color: #0c0c2d;
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h1 {
            font-size: 3em;
            color: #64a3ff;
        }
        .cake {
            position: relative;
            margin: 30px auto;
            width: 200px;
        }
        .tier {
            background-color: #f3f3f3;
            border: 4px solid #64a3ff;
            border-radius: 10px;
            margin: 10px auto;
            height: 40px;
        }
        .tier:nth-child(1) { width: 140px; }
        .tier:nth-child(2) { width: 180px; }
        .tier:nth-child(3) { width: 200px; }
        .candle {
            width: 10px;
            height: 30px;
            background-color: orange;
            margin: 0 auto;
            animation: flicker 1s infinite;
        }
        @keyframes flicker {
            0% {opacity: 1;}
            50% {opacity: 0.5;}
            100% {opacity: 1;}
        }
        .message {
            margin-top: 20px;
            font-size: 1.1em;
            color: #cccccc;
        }
    </style>
</head>
<body>
    <h1>🎉 Happy Birthday 🎉</h1>
    <div class="cake">
        <div class="candle"></div>
        <div class="tier"></div>
        <div class="tier"></div>
        <div class="tier"></div>
    </div>
    <div class="message">
        <p>Semoga setiap langkah kamu ke depan selalu dibarengi hal-hal baik.</p>
        <p>Makasih udah jadi kamu — dengan segala hal kecil yang bikin aku senyum diam-diam.</p>
        <p>Aku harap, apapun yang kamu cari, kamu temui.</p>
        <p>Kalau kamu lagi nyanyi lagu Naff - Akhirnya ku Menemukanmu...</p>
        <p>Mungkin kamu bakal inget pernah ada seseorang yang inget kamu sesimpel itu. 😌</p>
        <p>Have a good life, Mr. Gemini. 🖤</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
