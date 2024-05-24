import tkinter as tk
from tkinter import scrolledtext
import itertools
import random

def generate_matches():
    try:
        n = int(entry_1.get()) 
        assert 3 < n
        days = int(entry_2.get())
        assert 1 < days
        matches = list(itertools.combinations(range(1, n+1), 2))
        output_text.delete(1.0, tk.END)
        
        availability = {}
        for i in range(1, n+1):
            availability[i] = set(random.sample(range(1, days + 1), k=random.randint(1, days)))
            
        filtered_matches = []
        for match in matches:
            if availability[match[0]] and availability[match[1]]: 
                filtered_matches.append(match)
            
        schedule = []
        used_days = set()
        for match in filtered_matches:
            common_days = availability[match[0]] and availability[match[1]]
            if common_days:
                day = min(common_days)
                schedule.append((match, day))
                used_days.add(day)
        sorted_schedule = list(sorted(schedule, key = lambda schedule: schedule[1]))
            
        if len(sorted_schedule) != 0:
            output_text.delete(1.0, tk.END)        
            output_text.insert(tk.END, f"Оптимальное расписание ((партия), день): {sorted_schedule}\n")
            output_text.insert(tk.END, f"Минимальное количество дней для проведения турнира: {len(used_days)}\n")
        else:
            output_text.delete(1.0, tk.END)        
            output_text.insert(tk.END, f"К сожалению игроки не могут играть вместе, т.к у них разные дни")
            
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Пожалуйста, введите целые числа.")
        
    except AssertionError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Пожалуйста, введите числа согласно условиям: Дней должно быть больше 1 и игроков больше 3 (Имеет хоть какой-то логический смысл).")

        
root = tk.Tk()
root.title("Генератор партий")
root.config(bg = 'orange')
root.geometry("500x600+560+150")

entry_label_1 = tk.Label(root, text="Введите количество шахматистов (N):",
                         bg = 'grey',
                         fg = 'white',
                         font = ('DaunPenh', 10, 'bold'),
                         bd = 20  
                         )
entry_label_1.pack()
entry_1 = tk.Entry(root)
entry_1.pack()

entry_label_2 = tk.Label(root, text="Введите количество дней:",
                         bg = 'grey',
                         fg = 'white',
                         font = ('DaunPenh', 10, 'bold'),
                         bd = 20
                         )
entry_label_2.pack()
entry_2 = tk.Entry(root)
entry_2.pack()

generate_button = tk.Button(root, text="Сгенерировать партии", command=generate_matches)
generate_button.pack()

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
