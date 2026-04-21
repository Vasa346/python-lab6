#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook
from recipes.wok import Wok
from recipes.burger import Burger
from recipes.pizza import Pizza

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчёт рецептов")
        self.root.geometry("500x500")
        
        # Выбор рецепта
        ttk.Label(root, text="Выберите рецепт:").pack(pady=5)
        self.recipe_var = tk.StringVar(value="wok")
        ttk.Radiobutton(root, text="Вок", variable=self.recipe_var, value="wok", command=self.update_ingredients).pack()
        ttk.Radiobutton(root, text="Бургер", variable=self.recipe_var, value="burger", command=self.update_ingredients).pack()
        ttk.Radiobutton(root, text="Пицца", variable=self.recipe_var, value="pizza", command=self.update_ingredients).pack()
        
        # Рамка для ингредиентов
        ttk.Label(root, text="\nИнгредиенты (граммы):").pack(pady=5)
        self.ingredients_frame = ttk.Frame(root)
        self.ingredients_frame.pack(pady=5)
        
        self.entries = {}
        self.update_ingredients()
        
        # Кнопка расчёта
        ttk.Button(root, text="Рассчитать", command=self.calculate).pack(pady=10)
        
        # Результаты
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=5)
        
        # Кнопка сохранения в Excel
        ttk.Button(root, text="Сохранить в Excel", command=self.save_to_excel).pack(pady=5)
    
    def update_ingredients(self):
        # Очищаем старые виджеты
        for widget in self.ingredients_frame.winfo_children():
            widget.destroy()
        self.entries.clear()
        
        recipe = self.recipe_var.get()
        if recipe == "wok":
            ingredients = Wok.INGREDIENTS
        elif recipe == "burger":
            ingredients = Burger.INGREDIENTS
        else:
            ingredients = Pizza.INGREDIENTS
        
        for name in ingredients:
            frame = ttk.Frame(self.ingredients_frame)
            frame.pack(pady=2, fill=tk.X)
            ttk.Label(frame, text=f"{name}:").pack(side=tk.LEFT, padx=5)
            entry = ttk.Entry(frame, width=10)
            entry.insert(0, "100")
            entry.pack(side=tk.LEFT)
            ttk.Label(frame, text="г").pack(side=tk.LEFT)
            self.entries[name] = entry
    
    def get_ingredients_dict(self):
        return {name: float(entry.get() or 0) for name, entry in self.entries.items()}
    
    def calculate(self):
        recipe = self.recipe_var.get()
        ingredients = self.get_ingredients_dict()
        
        if recipe == "wok":
            obj = Wok(ingredients)
        elif recipe == "burger":
            obj = Burger(ingredients)
        else:
            obj = Pizza(ingredients)
        
        cost = obj.calculate_cost()
        calories = obj.calculate_calories()
        
        self.last_result = (recipe, ingredients, cost, calories)
        self.result_label.config(text=f"Стоимость: {cost} руб.\nКалорийность: {calories} ккал")
    
    def save_to_excel(self):
        if not hasattr(self, 'last_result'):
            messagebox.showwarning("Нет данных", "Сначала выполните расчёт")
            return
        
        recipe, ingredients, cost, calories = self.last_result
        wb = Workbook()
        ws = wb.active
        ws.title = recipe.capitalize()
        ws.append(["Ингредиент", "Граммы"])
        for name, grams in ingredients.items():
            ws.append([name, grams])
        ws.append([])
        ws.append(["Стоимость", f"{cost} руб."])
        ws.append(["Калорийность", f"{calories} ккал"])
        
        filename = f"{recipe}_report.xlsx"
        wb.save(filename)
        messagebox.showinfo("Успех", f"Отчёт сохранён в {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()