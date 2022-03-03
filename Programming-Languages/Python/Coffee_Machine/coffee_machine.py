class End(ValueError):
    pass
class CoffeeMachine:
    supplies = {'water':400,
                'milk':540,
                'coffee':120,
                'cups':9,
                'money':550}
    coffee_types = {1:[250, 0, 16, 4],
                    2:[350, 75, 20, 7],
                    3:[200, 100, 12, 6]} # water, milk, coffee, price
    treshold = 0
    def tresholder(self):
        water_amount = CoffeeMachine.supplies['water'] // 200
        milk_amount = CoffeeMachine.supplies['milk'] // 50
        coffee_amount = CoffeeMachine.supplies['coffee'] // 15
        if water_amount == 0:
            print('Sorry, not enough water!')
        elif milk_amount == 0:
            print('Sorry, not enough milk!')
        elif CoffeeMachine.supplies['cups'] == 0:
            print('Sorry, not enough cups!')
        elif coffee_amount == 0:        
            print('Sorry, not enough coffee beans!')
        # if water_amount <= milk_amount:
        #     if water_amount <= coffee_amount:
        #         CoffeeMachine.treshold = water_amount
        #     else:
        #         CoffeeMachine.treshold = coffee_amount
        # else:
        #     if milk_amount <= coffee_amount:
        #         CoffeeMachine.treshold = milk_amount
        #     else:
        #         CoffeeMachine.treshold = coffee_amount
    
    
    # def coffee(self, type):
    # add cups
    #     return self * CoffeeMachine.coffee_types[type][0], self * CoffeeMachine.coffee_types[type][1], self * CoffeeMachine.coffee_types[type][2], self * CoffeeMachine.coffee_types[type][4]
    # in case it wants to increase the numbers
    def calculator(desired):
        '''
        Needed things
        '''
        water = CoffeeMachine.coffee_types[desired][0]
        milk = CoffeeMachine.coffee_types[desired][1]
        coffee = CoffeeMachine.coffee_types[desired][2]
        cups = 1
        if water <= CoffeeMachine.supplies['water'] and milk <= CoffeeMachine.supplies['milk'] and coffee <= CoffeeMachine.supplies['coffee'] and cups <= CoffeeMachine.supplies['cups']:
            print('I have enough resources, making you a coffee!')
            CoffeeMachine.supplies['water'] -= water
            CoffeeMachine.supplies['milk'] -= milk
            CoffeeMachine.supplies['coffee'] -= coffee
            CoffeeMachine.supplies['cups'] -= cups
            CoffeeMachine.supplies['money'] += CoffeeMachine.coffee_types[desired][3] 
        else:
            CoffeeMachine.tresholder(0)
    def actions(taken):
        if taken == 'buy':
            desired = commands(str(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')))
            if desired is None:
                global end
                end = True
            else:
                CoffeeMachine.calculator(int(desired))
        elif taken == 'fill':
            CoffeeMachine.supplies['water'] += int(input('Write how many ml of water the coffee machine has:\n'))
            CoffeeMachine.supplies['milk'] += int(input('Write how many ml of milk the coffee machine has:\n'))
            CoffeeMachine.supplies['coffee'] += int(input('Write how many grams of coffee beans the coffee machine has:\n'))
            CoffeeMachine.supplies['cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
        elif taken == 'take':
            print('I gave you ${}'.format(CoffeeMachine.supplies['money']))
            CoffeeMachine.supplies['money'] = 0
            
def make_coffee():
    # I use 'end' to control the flow
    while end == False:
        try:
            action = commands(str(input('Write action (buy, fill, take, exit, remaining):\n')))
            CoffeeMachine.actions(action)
        except End:
            break
def commands(taken):
    if taken == 'remaining':
        print(f'''The coffee machine has:
{CoffeeMachine.supplies['water']} of water
{CoffeeMachine.supplies['milk']} of milk
{CoffeeMachine.supplies['coffee']} of coffee beans
{CoffeeMachine.supplies['cups']} of disposable cups
${CoffeeMachine.supplies['money']} of money''')
    elif taken == 'exit':
        raise End
    elif taken == 'back':
        make_coffee()
    else:
        return taken 
end = False
make_coffee()