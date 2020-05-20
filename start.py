import psycopg2

import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)




@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)


@ask.intent("YesIntent")

def next_round():

    round_msg = render_template('round1')

    return question(round_msg)


@ask.intent("AnswerIntent", convert={'text': str})

def answer(text):
    msg = str(text)
    print(msg)


    try:
        conn = psycopg2.connect("dbname='python' user='postgres' host='localhost' password='root'")
        print("I m connected")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()

    try:
        sql = "INSERT INTO test values('%s')" %(msg)
        cur.execute(sql)
        print("inserted")
    except:
        print("I can't Insert")


    conn.commit()
    print("Records created successfully")
    conn.close()
    return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)