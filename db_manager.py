#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
from psycopg2 import sql

DB_NAME = "recipes"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

class DBManager:
    def __init__(self):
        self.conn = None
        self.create_table()
    
    def connect(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
    
    def create_table(self):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS calculations (
                    id SERIAL PRIMARY KEY,
                    recipe VARCHAR(50),
                    ingredients TEXT,
                    cost DECIMAL(10, 2),
                    calories DECIMAL(10, 2),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.commit()
        self.close()
    
    def save_calculation(self, recipe, ingredients, cost, calories):
        self.connect()
        with self.conn.cursor() as cur:
            ingredients_str = ", ".join([f"{k}: {v}г" for k, v in ingredients.items()])
            cur.execute(
                "INSERT INTO calculations (recipe, ingredients, cost, calories) VALUES (%s, %s, %s, %s)",
                (recipe, ingredients_str, cost, calories)
            )
            self.conn.commit()
        self.close()
    
    def get_all_calculations(self):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM calculations ORDER BY created_at DESC")
            rows = cur.fetchall()
        self.close()
        return rows
    
    def close(self):
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    db = DBManager()
    print("Таблица calculations создана.")