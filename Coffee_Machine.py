machLevels = {
    'water': 400,
    'milk': 540,
    'beans': 120,
    'disposable cups': 9,
    'money': 550
}
espressoOrder = {
    'water': 250,
    'milk': 0,
    'beans': 16,
    'money': 4
}
latteOrder = {
    'water': 350,
    'milk': 75,
    'beans': 20,
    'money': 7
}
cappuccinoOrder = {
    'water': 200,
    'milk': 100,
    'beans': 12,
    'money': 6
}


def machine():
    print('The coffee machine has:')
    print(str(machLevels['water']) + ' of water')
    print(str(machLevels['milk']) + ' of milk')
    print(str(machLevels['beans']) + ' of coffee beans')
    print(str(machLevels['disposable cups']) + ' of disposable cups')
    print(str(machLevels['money']) + ' of money')
    print()


action = ''


def main_screen():
    global action
    while action != 'exit':
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            coffee_order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            if coffee_order == '1':
                if machLevels['water'] >= espressoOrder['water'] and machLevels['beans'] >= espressoOrder['beans'] and machLevels['disposable cups'] > 0:
                    print('I have enough resources, making you a coffee!')
                    print()
                    machLevels['water'] -= espressoOrder['water']
                    machLevels['milk'] -= espressoOrder['milk']
                    machLevels['beans'] -= espressoOrder['beans']
                    machLevels['money'] += espressoOrder['money']
                    machLevels['disposable cups'] -= 1
                elif machLevels['water'] < espressoOrder['water']:
                    print('Sorry, not enough water!')
                    print()
                elif machLevels['beans'] < espressoOrder['beans']:
                    print('Sorry, not enough coffee!')
                    print()
                elif machLevels['disposable cups'] == 0:
                    print('Sorry, not enough disposable cups')
                    print()

            if coffee_order == '2':
                if machLevels['water'] >= latteOrder['water'] and machLevels['beans'] >= latteOrder['beans'] and \
                        machLevels['milk'] >= latteOrder['milk'] and machLevels['disposable cups'] > 0:
                    print('I have enough resources, making you a coffee!')
                    print()
                    machLevels['water'] -= latteOrder['water']
                    machLevels['milk'] -= latteOrder['milk']
                    machLevels['beans'] -= latteOrder['beans']
                    machLevels['money'] += latteOrder['money']
                    machLevels['disposable cups'] -= 1
                elif machLevels['water'] < latteOrder['water']:
                    print('Sorry, not enough water!')
                    print()
                elif machLevels['milk'] < latteOrder['milk']:
                    print('Sorry, not enough milk!')
                    print()
                elif machLevels['beans'] < latteOrder['beans']:
                    print('Sorry, not enough coffee!')
                    print()
                elif machLevels['disposable cups'] == 0:
                    print('Sorry, not enough disposable cups')
                    print()

            if coffee_order == '3':
                if machLevels['water'] >= cappuccinoOrder['water'] and machLevels['beans'] >= cappuccinoOrder['beans'] and machLevels['milk'] >= cappuccinoOrder['milk'] and machLevels['disposable cups'] > 0:
                    print('I have enough resources, making you a coffee!')
                    print()
                    machLevels['water'] -= cappuccinoOrder['water']
                    machLevels['milk'] -= cappuccinoOrder['milk']
                    machLevels['beans'] -= cappuccinoOrder['beans']
                    machLevels['money'] += cappuccinoOrder['money']
                    machLevels['disposable cups'] -= 1
                elif machLevels['water'] < cappuccinoOrder['water']:
                    print('Sorry, not enough water!')
                    print()
                elif machLevels['milk'] < cappuccinoOrder['milk']:
                    print('Sorry, not enough milk!')
                    print()
                elif machLevels['beans'] < cappuccinoOrder['beans']:
                    print('Sorry, not enough coffee!')
                    print()
                elif machLevels['disposable cups'] == 0:
                    print('Sorry, not enough disposable cups')
                    print()

        elif action == 'fill':
            machLevels['water'] += int(input('Write how many ml of water do you want to add: '))
            machLevels['milk'] += int(input('Write how many ml of milk do you want to add: '))
            machLevels['beans'] += int(input('Write how many grams of coffee beans do you want to add: '))
            machLevels['disposable cups'] += int(
                input('Write how many disposable cups of coffee do you want to add: '))
            print()

        elif action == 'take':
            print('I give you $' + str(machLevels['money']))
            print()
            machLevels['money'] -= machLevels['money']

        elif action == 'back':
            main_screen()

        elif action == 'remaining':
            print()
            machine()


main_screen()
