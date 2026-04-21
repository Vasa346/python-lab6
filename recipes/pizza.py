#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pizza:
    """Расчёт стоимости и калорийности Пиццы."""
    
    INGREDIENTS = {
        "тесто": {"price": 60, "calories": 200},
        "сыр": {"price": 80, "calories": 150},
        "колбаса": {"price": 120, "calories": 280},
        "соус": {"price": 25, "calories": 60},
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