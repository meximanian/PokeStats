from functions import remove, add, combine, selector, end_chat

def remove(duplicate):

    Pokemon_List = remove(Pokemon)
    
    assert callable(remove)
    assert isinstance(remove(Pokemon), list)
    assert '' in remove(Pokemon)

def add(new_list):

    New_Pokemon = add(Pokemon_List)
    
    assert callable(add)
    assert isinstance(add(Pokemon_List), list)
    assert '' not in add(Pokemon_List)

def combine(list1, list2, list3, list4, list5, list6, list7, list8, list9):

    Pokelist = combine(New_Pokemon, Number, Total, HP, Attack, Defense, Special_Attack, Special_Defense, Speed)
    
    assert callable(combine)
    assert isinstance(combine(Pokemon, Number, Total, HP, Attack, Defense, Special_Attack, Special_Defense, Speed), list)

def selector(pokemon, check_list):

    New_pokelist = dict(zip(New_Pokemon, Pokelist))

    assert callable(selector)
    assert isinstance(selector('Charmander', New_Pokemon), list)
    assert selector('Pikachu', New_Pokemon) == ['Pokemon: Pikachu', 'Number: 025', 'Total: 320', 'HP: 35', 'Attack: 55', 
                                            'Defense: 40', 'Special_Attack: 50', 'Special_Defense: 50', 'Speed: 90']

def end_chat(input_list):

    assert callable(end_chat)
    assert isinstance(end_chat(['Charmander', 'Squirtle']), bool)
    assert end_chat(['quit']) == True

