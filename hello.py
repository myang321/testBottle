

import bottle


@bottle.route('/')
def home_page():
    mythings = ['apple', 'banana', 'peach']
    # option 1
    return bottle.template('hello', username='Lily', things=mythings)
    # option 2 use dic
    # return bottle.template('hello_world',{'username':'Steve2','things':mythings})


@bottle.post('/fav_fruit')
def fav_fruit():
    fruit = bottle.request.forms.get('fruit')
    if (fruit == None or fruit == ''):
        fruit = 'no Fruit'
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")


@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return bottle.template('fruit_select', {"fruit": fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8082)