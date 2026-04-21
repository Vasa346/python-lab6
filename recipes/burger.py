#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Burger:
    """Расчёт стоимости и калорийности Бургера."""
    
    INGREDIENTS = {
        "булочка": {"price": 40, "calories": 150},
        "котлета": {"price": 100, "calories": 300},
        "сыр": {"price": 60, "calories": 120},
        "салат": {"price": 20, "calories": 15},
        "соус": {"price": 15, "calories": 50},
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