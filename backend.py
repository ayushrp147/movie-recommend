import csv
import random
import tkinter as tk
from tkinter import messagebox

filename = "IMDB-Movie-Data.csv"
fields = []
rows = []

with open(filename , 'r',encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)  
    for row in csvreader:
        rows.append(row)

def recommend(genre,imdb,run,year,n):
    action=[]
    for i in range(len(rows)):
        l1=[]
        if 'Action' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            action.append(l1)
        
    adventure=[]
    for i in range(len(rows)):
        l1=[]
        if 'Adventure' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            adventure.append(l1)
    sciFi=[]
    for i in range(len(rows)):
        l1=[]
        if 'Sci-Fi' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            sciFi.append(l1)
    mystery=[]
    for i in range(len(rows)):
        l1=[]
        if 'Mystery' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            mystery.append(l1)
    horror=[]
    for i in range(len(rows)):
        l1=[]
        if 'Horror' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            horror.append(l1)
    biography=[]
    for i in range(len(rows)):
        l1=[]
        if 'Biography' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            biography.append(l1)
    drama=[]
    for i in range(len(rows)):
        l1=[]
        if 'Drama' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            drama.append(l1)
    romance=[]
    for i in range(len(rows)):
        l1=[]
        if 'Romance' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            romance.append(l1)
    fantasy=[]
    for i in range(len(rows)):
        l1=[]
        if 'Fantasy' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            fantasy.append(l1)
    animation=[]
    for i in range(len(rows)):
        l1=[]
        if 'Animation' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            animation.append(l1)
    comedy=[]
    for i in range(len(rows)):
        l1=[]
        if 'Comedy' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            comedy.append(l1)
    
    history=[]
    for i in range(len(rows)):
        l1=[]
        if 'History' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            history.append(l1)
    western=[]
    for i in range(len(rows)):
        l1=[]
        if 'Western' in rows[i][6]:
            l1=[rows[i][1],rows[i][3],rows[i][5],rows[i][4],rows[i][2],rows[i][6]]
            western.append(l1)
    
    if genre=='Action':
        l1=[]
        for i in range(len(action)):
            l2=[]
            if float(action[i][2])>=imdb and float(action[i][1])>=year and float(action[i][3])>=run:
                l2=[action[i][0],action[i][4],action[i][1],action[i][2],action[i][3],action[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Drama':
        l1=[]
        for i in range(len(drama)):
            l2=[]
            if float(drama[i][2])>=imdb and float(drama[i][1])>=year and float(drama[i][3])>=run:
                l2=[drama[i][0],drama[i][4],drama[i][1],drama[i][2],drama[i][3],drama[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Romance':
        l1=[]
        for i in range(len(romance)):
            l2=[]
            if float(romance[i][2])>=imdb and float(romance[i][1])>=year and float(romance[i][3])>=run:
                l2=[romance[i][0],romance[i][4],romance[i][1],romance[i][2],romance[i][3],romance[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Fantasy':
        l1=[]
        for i in range(len(fantasy)):
            l2=[]
            if float(fantasy[i][2])>=imdb and float(fantasy[i][1])>=year and float(fantasy[i][3])>=run:
                l2=[fantasy[i][0],fantasy[i][4],fantasy[i][1],fantasy[i][2],fantasy[i][3],fantasy[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Animation':
        l1=[]
        for i in range(len(animation)):
            l2=[]
            if float(animation[i][2])>=imdb and float(animation[i][1])>=year and float(animation[i][3])>=run:
                l2=[animation[i][0],animation[i][4],animation[i][1],animation[i][2],animation[i][3],animation[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Comedy':
        l1=[]
        for i in range(len(comedy)):
            l2=[]
            if float(comedy[i][2])>=imdb and float(comedy[i][1])>=year and float(comedy[i][3])>=run:
                l2=[comedy[i][0],comedy[i][4],comedy[i][1],comedy[i][2],comedy[i][3],comedy[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='History':
        l1=[]
        for i in range(len(history)):
            l2=[]
            if float(history[i][2])>=imdb and float(history[i][1])>=year and float(history[i][3])>=run:
                l2=[history[i][0],history[i][4],history[i][1],history[i][2],history[i][3],history[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Western':
        l1=[]
        for i in range(len(western)):
            l2=[]
            if float(western[i][2])>=imdb and float(western[i][1])>=year and float(western[i][3])>=run:
                l2=[western[i][0],western[i][4],western[i][1],western[i][2],western[i][3],western[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected       
    if genre=='Biography':
        ll1=[]
        for i in range(len(biography)):
            l2=[]
            if float(biography[i][2])>=imdb and float(biography[i][1])>=year and float(biography[i][3])>=run:
                l2=[biography[i][0],biography[i][4],biography[i][1],biography[i][2],biography[i][3],biography[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Horror':
        l1=[]
        for i in range(len(horror)):
            l2=[]
            if float(horror[i][2])>=imdb and float(horror[i][1])>=year and float(horror[i][3])>=run:
                l2=[horror[i][0],horror[i][4],horror[i][1],horror[i][2],horror[i][3],horror[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Mystery':
        l1=[]
        for i in range(len(mystery)):
            l2=[]
            if float(mystery[i][2])>=imdb and float(mystery[i][1])>=year and float(mystery[i][3])>=run:
                l2=[mystery[i][0],mystery[i][4],mystery[i][1],mystery[i][2],mystery[i][3],mystery[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Sci-Fi':
        l1=[]
        for i in range(len(sciFi)):
            l2=[]
            if float(sciFi[i][2])>=imdb and float(sciFi[i][1])>=year and float(sciFi[i][3])>=run:
                l2=[sciFi[i][0],sciFi[i][4],sciFi[i][1],sciFi[i][2],sciFi[i][3],sciFi[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected
    if genre=='Adventure':
        l1=[]
        for i in range(len(adventure)):
            l2=[]
            if float(adventure[i][2])>=imdb and float(adventure[i][1])>=year and float(adventure[i][3])>=run:
                l2=[adventure[i][0],adventure[i][4],adventure[i][1],adventure[i][2],adventure[i][3],adventure[i][5]]
                l1.append(l2)
        selected=[]
        if(n>len(l1)):
            for i in range(len(l1)):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        elif(len(l1)==0):
            messagebox.showerror("Sorry","No Movies to Recommend")
        else:
            for i in range(n):
                chosen_item=random.choice(l1)
                selected.append(chosen_item)
                l1.remove(chosen_item)
        return selected