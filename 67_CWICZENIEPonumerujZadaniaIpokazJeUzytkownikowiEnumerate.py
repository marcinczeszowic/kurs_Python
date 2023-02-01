# tworzymy liste
colors = ["red", "green", "blue"]

# wybieramy elementy z krotki i je wyświetlamy:
for i, color in enumerate(colors):
    print(i, color)

tasks = ["clean the kitchen", "do laundry", "pay bills"]
"""
1 Clean the kitchen
2 Do laundry
3 Pay bills
"""
for i, tasks in enumerate(tasks, start=1):
    task = tasks.capitalize()
    print(i, task)