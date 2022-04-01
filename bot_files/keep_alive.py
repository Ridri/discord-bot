from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    print("I'm alive")

def run():
  app.run(host = '0.0.0.0', port = 4369)

def keep_alive():
    t = Thread(target = run)
    t.start()