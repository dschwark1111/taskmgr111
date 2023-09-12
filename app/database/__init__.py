from flask import g   #global context object 
import sqlite3

DATABASE_URL = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:  #if db is equal to none
        
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db