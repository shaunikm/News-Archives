from flask import render_template
import newsarchives

def index():
    return(render_template('index.html'))

def day_search(day):
    return(render_template('search.html', news=newsarchives.day(day)['data'][0]['articles']))