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

@app.route('/quantum-computing')
def quantum():
    return render_template('quantum-computing.html')

@app.route('/climate-change')
def climate():
    return render_template('climate-change.html')

@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

if __name__ == '__main__':
    app.run(debug=True)