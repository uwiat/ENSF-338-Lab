import json
import numpy as np
import matplotlib.pyplot as plt

def below_10k_countries(below_10k_data):
    fig, axs = plt.subplots(figsize=(15, 5))

    axs.hist(below_10k_data, fc='none', edgecolor='blue', label='Below 10,000')
    axs.set_title('Internet Usage in Countries with Income Below $10,000')
    axs.set_xlabel('Internet User Rate')
    axs.set_ylabel('Frequency')

    plt.savefig("hist1.png")
    #plt.show()

def above_10k_countries(above_10k_data):
    fig, axs = plt.subplots(figsize=(15, 5))

    axs.hist(above_10k_data, fc='none', edgecolor='red', label='10,000 and Above')
    axs.set_title('Internet Usage in Countries with Income $10,000 and Above')
    axs.set_xlabel('Internet User Rate')
    axs.set_ylabel('Frequency')

    plt.savefig("hist2.png")
    #plt.show()

with open("internetdata.json", 'r') as jsonfile:
    data = json.load(jsonfile) 
    
    below_10k = [country["country"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) < 10000]
    above_10k = [country["country"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) >= 10000]

    

    below_10k_data = [country["internetuserate"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) < 10000 and country["internetuserate"] != None]
    above_10k_data = [country["internetuserate"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) >= 10000 and country["internetuserate"] != None] 

    
    
    below_10k_countries(below_10k_data)
    above_10k_countries(above_10k_data)

