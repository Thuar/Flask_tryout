from flask import Flask

@app.route('/')
def home():
        return "<p>Dit is een test</p>"