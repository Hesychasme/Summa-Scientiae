#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 21:02:14 2025

@author: thomas
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solar-system')
def solar_system():
    return render_template('solar-system.html')

if __name__ == '__main__':
    app.run(debug=True)