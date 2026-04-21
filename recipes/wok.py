#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wok:
    """Расчёт стоимости и калорийности Вока."""
    
    INGREDIENTS = {
        "лапша": {"price": 50, "calories": 200},
        "курица": {"price": 120, "calories": 250},
        "овощи": {"price": 80, "calories": 100},
        "соус": {"price": 30, "calories": 80},
    }
    
    def __init__(self, ingredients=None):
        self.ingredients = ingredients or {}
    
    def calculate_cost(self):
        total = 0
        for name, grams in self.ingredients.items():
            if name in self.INGREDIENTS:
                total += self.INGREDIENTS[name]["price"] * grams / 100
        return round(total, 2)
    
    def calculate_calories(self):
        total = 0
        for name, grams in self.ingredients.items():
            if name in self.INGREDIENTS:
                total += self.INGREDIENTS[name]["calories"] * grams / 100
        return round(total, 2)