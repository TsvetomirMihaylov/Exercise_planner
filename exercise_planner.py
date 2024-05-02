import tkinter as tk
from tkinter import scrolledtext
import webbrowser






exercise_dict = {
    'Biceps':['Hefesto pullup progression','Pull up','One arm pull up dynamic progression','One arm pull up static progression','Back lever','Front lever pull up','Muscle up'],
    "Chest": ['Muscle up',"Back lever", "Dip",'Push up','Handstand pushup'],
    "Lats": ['Pull up',"Front lever static progression", "Front lever dynamic progression", 'One arm pull up dynamic progression','One arm pull up static progression', 'Muscle up','Front lever pull up'],
    'Abs':['Muscle up','Pull up',"Front lever static progression", "Front lever dynamic progression", 'One arm pull up dynamic progression','One arm pull up static progression','Front lever pull up'],
    'Shoulders':['Planche progression','Muscle up','Push up','Dip','Handstand holds','Handstand pushups','Back lever','Korean dip','Hefesto pull up progression'],
    'Triceps':['Handstand pushup','Push up','L-sit progression','Dip'],
    'Forearm':['Handstand holds','Dead hang'],
    'Quadriceps':['Running','Pistol squat'],
    'Calf':['Running','One-legged calf raises'],
    'Glute':['Pistol squat','Side leg hold'],
    'Hip flexor':['Front lever pull up',"Front lever static progression", "Front lever dynamic progression",'Front leg hold','L-sit progression',"Front lever dynamic progression"],
    'Cardio':['Running'],
    'Flexibility':['Touch toes','Splits','Bridge'],
}

exercise_links = {
    'Hefesto pullup progression': 'https://www.youtube.com/watch?v=kLz2S_magwY',
    'Pull up': 'https://www.youtube.com/watch?v=eGo4IYlbE5g',
    'One arm pull up dynamic progression': 'https://www.youtube.com/watch?v=mTJHClMQPM8',
    'One arm pull up static progression': 'https://www.youtube.com/watch?v=zZfrf5G9OdE',
    'Back lever': 'https://www.youtube.com/watch?v=HXaG8mJmSnU&t',
    'Front lever pull up': 'https://www.youtube.com/watch?v=owXfTSkJqr4',
    'Muscle up': 'https://www.youtube.com/watch?v=8kq-1QfgI7I',
    'Dip': 'https://www.youtube.com/watch?v=jyxDvqqdttk',
    'Push up': 'https://www.youtube.com/watch?v=_l3ySVKYVJ8',
    'Handstand pushup': 'https://www.youtube.com/watch?v=JZkpJzX_6BQ',
    'Front lever static progression': 'https://www.youtube.com/watch?v=B3_iF6mxSXY',
    'Front lever dynamic progression': 'https://www.youtube.com/watch?v=B3_iF6mxSXY',
    'Planche progression': 'https://www.youtube.com/watch?v=ghNIgUG8_ZY',
    'Handstand holds': 'https://www.youtube.com/watch?v=dT6DmCcPNYc',
    'Handstand pushups': 'https://www.youtube.com/watch?v=JZkpJzX_6BQ',
    'Korean dip': 'https://www.youtube.com/watch?v=42-lPrG7dkU',
    'Dead hang': 'https://www.youtube.com/watch?v=Rf8Yrml4SpI',
    'L-sit progression': 'https://www.youtube.com/watch?v=cu0fHp8HCDo',
    'Front leg hold': 'https://www.youtube.com/watch?v=oztV03rrgvM',
    'Running': 'https://www.youtube.com/watch?v=sScNDZu2MWk',
    'Pistol squat': 'https://www.youtube.com/watch?v=QOVaHwm-Q6U',
    'Side leg hold': 'https://www.youtube.com/watch?v=o0KsIcDL0dg',
    'Touch toes': 'https://www.youtube.com/watch?v=6XM-Jzq-pOA',
    'Splits': 'https://www.youtube.com/watch?v=E9mM2StxkCo',
    'Bridge': 'https://www.youtube.com/watch?v=fZoASuW8gK8'
}


def get_excluded_exercises():
    undesired_muscles = []
    for i, var in enumerate(muscle_undesired_vars):
        if var.get():
            undesired_muscles.extend(exercise_dict[list(exercise_dict.keys())[i]])

    excluded_exercises = []
    for exercise in exercise_dict.values():
        for ex in exercise:
            if ex in undesired_muscles:
                excluded_exercises.append(ex)
    return excluded_exercises

def get_included_exercises():
    desired_muscles = []
    for i, var in enumerate(muscle_desired_vars):
        if var.get():
            desired_muscles.extend(exercise_dict[list(exercise_dict.keys())[i]])

    included_exercises = []
    for exercise in exercise_dict.values():
        for ex in exercise:
            if ex in desired_muscles:
                included_exercises.append(ex)
    return included_exercises

opened_links = set()

def open_link(event):
    widget = event.widget
    index = widget.index(tk.CURRENT)
    line, column = index.split('.')
    line_text = widget.get(f"{line}.0", f"{line}.end")
    exercise_name = line_text.strip()
    if exercise_name in exercise_links:
        link = exercise_links[exercise_name]
        if link and link not in opened_links:
            webbrowser.open(link)
            opened_links.add(link)

def set_cursor_hand(event):
    event.widget.config(cursor="hand2")

def set_cursor_arrow(event):
    event.widget.config(cursor="")

def show_exercises():
    excluded_exercises = get_excluded_exercises()
    included_exercises = get_included_exercises()

    if len(included_exercises) == 0:
        included_exercises = [item for sublist in exercise_dict.values() for item in sublist]

    set1 = set(included_exercises)
    set2 = set(excluded_exercises)
    result = list(set1 - set2)
    if len(result) == 0:
        result = ['No available exercises.']
    exercise_text.delete(1.0, tk.END)
    for exercise in result:
        if exercise in exercise_links:
            exercise_text.insert(tk.END, exercise + "\n", "link")
        else:
            exercise_text.insert(tk.END, exercise + "\n")
    exercise_text.tag_config("link", foreground="blue", underline=True)
    exercise_text.bind("<Button-1>", open_link)

# GUI setup
root = tk.Tk()
root.title("Fitness Helper")


root.configure(bg="#add8e6")  
font_style = ("Helvetica", 10)  

muscles_frame = tk.Frame(root, bg="#add8e6")
muscles_frame.pack(side=tk.LEFT)

muscle_desired_vars=[]
muscle_undesired_vars = []
for i, muscle in enumerate(exercise_dict):
    var_desired = tk.BooleanVar()
    var_desired.set(False)
    chk_desired = tk.Checkbutton(muscles_frame, text=muscle+" (want)", variable=var_desired, bg="#add8e6", font=font_style)
    chk_desired.grid(row=i, column=0, sticky=tk.W)
    muscle_desired_vars.append(var_desired)
    
    var_undesired = tk.BooleanVar()
    var_undesired.set(False)
    chk_undesired = tk.Checkbutton(muscles_frame, text=muscle+" (can't)", variable=var_undesired, bg="#add8e6", font=font_style)
    chk_undesired.grid(row=i, column=1, sticky=tk.W)
    muscle_undesired_vars.append(var_undesired)

show_button = tk.Button(root, text="Show Exercises", command=show_exercises, bg="#4CAF50", fg="black", font=font_style)
show_button.pack(pady=10)

exercise_text = scrolledtext.ScrolledText(root, width=40, height=10, font=font_style, bg="#4CAF50")
exercise_text.pack()

for muscle, exercises in exercise_dict.items():
    exercise_text.insert(tk.END, f"{muscle}:\n", "heading")
    exercise_text.tag_config("heading", font=("Helvetica", 10, "bold"))
    for exercise in exercises:
        exercise_text.insert(tk.END, f"{exercise}\n", "link")
        exercise_text.tag_bind("link", "<Button-1>", open_link)
        exercise_text.tag_bind("link", "<Enter>", set_cursor_hand)
        exercise_text.tag_bind("link", "<Leave>", set_cursor_arrow)
    exercise_text.insert(tk.END, "\n")

exercise_text.tag_config("link", foreground="blue", underline=True)


root.mainloop()
