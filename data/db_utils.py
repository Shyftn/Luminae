# db_utils.py

import sqlite3
from sqlite3 import Error

def add_asked_question(conn, question_id, category):
    """
    Adds asked question to database
    """
    query = "INSERT INTO asked_questions(question_id, category) VALUES(?,?)"
    cur = conn.cursor()
    cur.execute(query, (question_id, category))
    conn.commit()
    return cur.lastrowid

def fetch_asked_questions(conn, category):
    """
    Fetch all asked questions for the category
    """
    query = "SELECT question_id FROM asked_questions WHERE category = ?"
    cur = conn.cursor()
    cur.execute(query, (category,))
    return cur.fetchall()

def update_user_score(conn, username, category):
    """
    Update user score in database
    """
    query = "UPDATE scores SET score = score + 1 WHERE username = ? AND category = ?"
    cur = conn.cursor()
    cur.execute(query, (username, category))
    conn.commit()

def fetch_user_score(conn, username, category):
    """
    Fetch user score from database
    """
    query = "SELECT score FROM scores WHERE username = ? AND category = ?"
    cur = conn.cursor()
    cur.execute(query, (username, category))
    return cur.fetchone()

def add_user(conn, username, category):
    """
    Add a new user to the score table
    """
    query = "INSERT INTO scores(username, score, category) VALUES(?,?,0)"
    cur = conn.cursor()
    cur.execute(query, (username, category))
    conn.commit()
    return cur.lastrowid
