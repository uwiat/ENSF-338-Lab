import json
import numpy as np
import matplotlib.pyplot as plt

with open("internetdata.json", 'r') as jsonfile:
    data = json.load(jsonfile) 
    
    below_10k = [country["country"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) < 10000]
    above_10k = [country["country"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) >= 10000]

    print("Countries with income below 10,000:", below_10k)
    print("Countries with income 10,000 and above:", above_10k)

    below_10k_countries = [country["internetuserate"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) < 10000 and country["internetuserate"] != None]
    above_10k_countries = [country["internetuserate"] for country in data if country['incomeperperson'] != None and int(country['incomeperperson']) >= 10000 and country["internetuserate"] != None] 

    print("Countries with income below 10,000 internet usage:", below_10k_countries)
    print("Countries with income 10,000 and above internet usage:", below_10k_countries)

fig, (axs1, axs2) = plt.subplots(1, 2, figsize=(15, 3))



axs1.hist(below_10k_countries,fc='none',edgecolor='blue', label='Below 10,000')
axs1.set_title('Internet Usage in Countries with Income Below $10,000')
axs1.set_xlabel('Internet User Rate')
axs1.set_ylabel('Frequency')

axs2.hist(above_10k_countries, fc='none',edgecolor='red', label='10,000 and Above')
axs2.set_title('Internet Usage in Countries with Income $10,000 and Above')
axs2.set_xlabel('Internet User Rate')
axs2.set_ylabel('Frequency')


plt.show()
