#!/usr/bin/python3

import json
import urllib.parse
import urllib.request

# colors
# blue special notice
NOTICE = '\033[94m'
# red is important
ALERT = '\033[91m'
# green is console color default
CON = '\033[92m'
# you need the end encoding after the message
END = '\033[0m'

# set basic globals
cmd = ''
base_url = 'http://www.thecocktaildb.com/api/json/v1/1/'

title_top = '''
|-----------------------------------------------|
|                                               |
'''
frame_bot = '''
|                                               |
|-----------------------------------------------|
'''
ingredient_top = '''
|------------------Ingredient-------------------|
'''
measure_top = '''
|--------------------Measure--------------------|
'''
cell_bot = '''
|-----------------------------------------------|
'''

# modest lil banner
print(CON + '\n-------------------')
print('    Welcome To')
print('  Cocktail Console')
print('-------------------' + END)

def clean_json_response(dirty_json):
    '''
    Takes the HTTPResponse that is actually JSON and makes it to a string
    so that it can be decoded by json.loads()
    :param dirty_json: HTTPResponse Object
    :return: json string
    '''

    # set encoding
    encoding = dirty_json.info().get_content_charset('utf-8')
    return dirty_json.read().decode(encoding)

def build_ingredient_list(cocktail_json):
    '''
    takes drinks json output and creates a dictionary of ingredient:measure
    :param cocktail_json:
    :return: dict
    '''
    ingredients = {}
    for key in cocktail_json.keys():
        if (cocktail_json[key].strip() == ''):
            continue
        elif not key.startswith('strIngredient'):
            continue
        elif key.startswith('strIngredient'):
            ingredients[cocktail_json[key]] = cocktail_json[
                'strMeasure' + key.split('strIngredient')[1]
            ]
    return ingredients

def get_drink(drink_id=None):
    '''
    gets drink by id or random
    :return: None
    '''
    try:
        if drink_id:
            clean_json = clean_json_response(
                urllib.request.urlopen(base_url + '/lookup.php?i=' + drink_id)
            )
        else:
            clean_json = clean_json_response(
                urllib.request.urlopen(base_url + '/random.php')
            )
        drink = json.loads(clean_json)
        ingredients = build_ingredient_list(drink['drinks'][0])
        title = drink['drinks'][0]['strDrink'].strip()
        drink_id = 'ID: ' + drink['drinks'][0]['idDrink']
        print(CON + title_top + END)
        print(CON + title.center(50, ' ') + END)
        print(CON + drink_id.center(50, ' ') + END)
        print(CON + frame_bot + END)
        for ing in ingredients:
            print(CON + ingredient_top + END)
            print(CON + ing.center(50, ' ') + END)
            print(CON + measure_top + END)
            print(CON + ingredients[ing].center(50, ' ') + END)
            print(CON + frame_bot + END)

    except urllib.error.HTTPError as e:
        print(
            '{0}{1}'.format(
                ALERT + '[!]' + END,
                e.code
            )
        )

    except urllib.error.URLError as e:
        print(
            '{0}{1}'.format(
                ALERT + '[!]' + END,
                e.code
            )
        )

# menu
while cmd != 'q'.lower():
    # display menu and get cmd
    print(CON + '\nenter a command:' + END)
    print(CON + 'get | get drink by id (default random)' + END)
    print(CON + 'q | kill session' + END)
    cmd = input(CON + '==> ')
    if cmd == 'get'.lower():
        get_drink(input('ID of drink==> '))

    elif cmd == 'q'.lower():
        print(NOTICE + '[~]' + END + 'Closing Time!' + NOTICE + '[~]' + END)

    else:
        print(ALERT + '[!]' + END + 'INVALID COMMAND')