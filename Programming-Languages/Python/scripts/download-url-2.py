import wget
import pandas as pd
import os
import requests

import pandas as pd
how_many = 0
inner_counter = 0

def counters(name):
    counter = 0
    df = pd.read_excel(name)
    counter = len(df)
    print(name, counter, sep=" : ")

        
        
def downloader(dir_name, names, urls):
    global how_many
    global inner_counter
    left = len(names)
    for name, url in zip(names, urls):
        print("\n", how_many)
        name_save = f"{dir_name}{name}.pdf"
        how_many += 1
        
        
        try:
            url = url.rstrip()
            wget.download(url, out=name_save)
        except:
            print("first")
            inner_counter += 1
            
        ##second option
        try:
            r = requests.get(url, allow_redirects=True)

            open(name_save, 'wb').write(r.content) 
        except:
            print("second")
            inner_counter += 1

def start(dir_name, name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    df = pd.read_excel(name.strip("\n"))
    downloader(dir_name, df[df.columns[0]], df[df.columns[-1]])
 
    
with open("files.txt", "r") as files:
    
    for i, file in enumerate(files.readlines()):
        print("Is now in process: ", file)
        dir_name = file[:-6] + "/"
        
        if i != len(files.readlines())-1:
            file = file[:-1]
        start(dir_name, file)
    