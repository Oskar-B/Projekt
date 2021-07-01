import psycopg2
import config
import pandas as pd
import matplotlib.pyplot as plt
import csv
import tkinter as tk

# Verlgiecht zwei Attribute von einem Land (Grafische-Visualisierung)
def vergleich_att(country, col1, col2):
    conn = None
    try:
        params = config.config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #Hole die zwei Attribute aus der Datenbank
        cur.execute("SELECT year, "+col1+", "+col2+" FROM country c WHERE name = ""'"+country+"'""")
        db = cur.fetchall()
        #Attributnamen noch einfügen
        db.insert(0,('year', col1, col2))
        #Daten als CSV Datei speichern
        with open('somefile.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            for row in db:
                writer.writerow(row)
        #Erstellte CSV Datei (somefile.csv(oder anderer Name) muss dabei im Ordner sein)
        data = pd.read_csv("somefile.csv",';')

        #Die Erste Achse mit Attribut 1
        fig, grow = plt.subplots()
        color = 'tab:red'
        grow.set_xlabel('Jahre')
        grow.set_ylabel(col1, color=color)

        if col1 == 'pop_growth':
            grow.plot(data.year, data.pop_growth, color=color)
        elif col1 == 'total_pop':
            grow.plot(data.year, data.total_pop, color=color)
        elif col1 == 'gdp':
            grow.plot(data.year, data.gdp, color=color)
        elif col1 == 'co2_emm':
            grow.plot(data.year, data.co2_emm, color=color)
        elif col1 == 'generosity':
            grow.plot(data.year, data.generosity, color=color)
        elif col1 == 'corruption':
            grow.plot(data.year, data.corruption, color=color)
        elif col1 == 'freedom':
            grow.plot(data.year, data.freedom, color=color)
        grow.tick_params(axis='y', labelcolor=color)

        #Zweite Achse mit Attribut 2
        popu = grow.twinx()
        color = 'tab:blue'
        popu.set_ylabel(col2, color = color)

        if col2 == 'pop_growth':
            popu.plot(data.year, data.pop_growth, color=color)
        elif col2 == 'total_pop':
            popu.plot(data.year, data.total_pop, color=color)
        elif col2 == 'gdp':
            popu.plot(data.year, data.gdp, color=color)
        elif col2 == 'co2_emm':
            popu.plot(data.year, data.co2_emm, color=color)
        elif col2 == 'generosity':
            popu.plot(data.year, data.generosity, color=color)
        elif col2 == 'corruption':
            popu.plot(data.year, data.corruption, color=color)
        elif col2 == 'freedom':
            popu.plot(data.year, data.freedom, color=color)
        popu.tick_params(axis='y', labelcolor=color)
        #Visualisierung anzeigen
        fig.tight_layout()
        plt.xticks(data.year[::2])
        plt.show()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#GUI für die Bedienung
root = tk.Tk()
root.title("DBS Uebungsblatt 10 - Projekt")
root.geometry("500x220")
options_list = ['pop_growth', 'total_pop', 'gdp', 'co2_emm', 'generosity', 'corruption', 'freedom']

value_inside = tk.StringVar(root)
value_inside.set("Attribut 1")

value_inside2 = tk.StringVar(root)
value_inside2.set("Attribut 2")

def getTextInput():
    Country=Land.get(1.0, tk.END+"-1c")
    Collm1=value_inside.get()
    Collm2=value_inside2.get()
    vergleich_att(Country,Collm1,Collm2)

w = tk.Label(root, text="Land")
w.pack()

Land=tk.Text(root, height=1, width=20)
Land.pack()

spacer = tk.Label(root, text=" ")
spacer.pack()

question_menu = tk.OptionMenu(root, value_inside, *options_list)
question_menu.pack()

spacer1 = tk.Label(root, text=" ")
spacer1.pack()

question_menu2 = tk.OptionMenu(root, value_inside2, *options_list)
question_menu2.pack()

spacer2 = tk.Label(root, text=" ")
spacer2.pack()

btnRead=tk.Button(root, height=1, width=10, text="Show", 
                    command=getTextInput)
btnRead.pack()

root.mainloop()

btnRead=tk.Button(root, height=1, width=10, text="Show", 
                    command=getTextInput)
btnRead.pack()

root.mainloop()
