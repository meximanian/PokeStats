#imports
from lxml import html
import requests

#This will retrieve the web page, parse it with the html module, and save it under Information
Page = requests.get('https://pokemondb.net/pokedex/all')
Information = html.fromstring(Page.content)

#This will create a list of Pokemon: 
Pokemon = Information.xpath('//a[@class= "ent-name"]/text()')

#This will create a list of the Pokemon's number:
Number = Information.xpath('//span[@class = "infocard-cell-data"]/text()')

#This will create a list of Alternative forms of Pokemon
Alt_form = Information.xpath('//small[@class = "text-muted"]/text()')

#This will create a list of the each Pokemon's stats added together:
Total = Information.xpath('//td[@class = "cell-total"]/text()')

#This will create a list of each Pokemon's stats:
Stats = Information.xpath('//td[@class= "cell-num"]/text()')

#This will create a list of each Pokemon's HP level:
HP = Stats[0::6]

#This will create a list of each Pokemon's Attack level:
Attack = Stats[1::6]

#This will create a list of each Pokemon's Defense level:
Defense = Stats[2::6]

#This will create a list of each Pokemon's Special Attack level:
Special_Attack = Stats[3::6]

#This will create a list of each Pokemon's Special Defense level:
Special_Defense = Stats[4::6]

#This will create a list of each Pokemon's Speed level:
Speed = Stats[5::6]

def remove(duplicate):
    """This function will remove duplicate Pokemon names."""
    new_list = []
    
    for pokemon in duplicate:
        
        if pokemon in new_list:
                pokemon = ''
            
        new_list.append(pokemon)
    
    return new_list

Pokemon_List = remove(Pokemon)

def add(new_list):
    """This function will add the Pokemon's alternative form to the empty spaces."""
    
    position = 0
    final_list = []
    
    for pokemon in new_list:

        if pokemon == '':
            
            pokemon = Alt_form[position]
            position += 1
        
        else:
            pokemon = pokemon
        
        final_list.append(pokemon)
    
    return final_list

New_Pokemon = add(Pokemon_List)

def combine(list1, list2, list3, list4, list5, list6, list7, list8, list9):
    """This function will take all of the lists and combine and label them."""
    
    pokelist = []    
    
    for it1, it2, it3, it4, it5, it6, it7, it8, it9 in zip(list1, list2, list3, list4, list5, list6, list7, list8, list9):
        
        output = ['Pokemon: ' + it1, 'Number: ' + it2, 'Total: ' + it3, 'HP: ' +  it4, 'Attack: ' + it5, 'Defense: ' + it6, 
                  'Special_Attack: ' + it7, 'Special_Defense: ' + it8, 'Speed: ' + it9]
        
        pokelist.append(output)
    
    return pokelist

Pokelist = combine(New_Pokemon, Number, Total, HP, Attack, Defense, Special_Attack, Special_Defense, Speed)

def selector(pokemon, check_list):
    """This function will pull the information for the Pokemon that is called."""
    
    output = None
    
    if pokemon in check_list:
        output = New_pokelist[pokemon]
    
    return output

New_pokelist = dict(zip(New_Pokemon, Pokelist))

def end_chat(input_list):
    """This function will end the Pokedex."""
    
    if 'quit' in input_list:
        output = True
    
    else:
        output = False
    
    return output

def Pokedex():
    """This function allows a bot to display the information of the Pokemon that is called."""
    
    pokedex = True
    while pokedex:
        
        # Gets a Pokemon name from the user
        msg = input('Please insert Pokemon name:\t')
        out_msg = None
        
        # Check for an end msg
        if end_chat(msg):
            out_msg = 'Closing Pokedex!'
            pokedex = False
        
        # Pull the information of the Pokemon that is called
        if not out_msg:
            out_msg = selector(msg, New_Pokemon)
        
        print('Pokemon Statistics:', out_msg)