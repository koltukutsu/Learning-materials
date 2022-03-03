import random
class InvalidInput(ValueError):
    pass
class Game:
    user_name = ''
    choices = {'rock': [['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'], ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']],
    'fire': [['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'], ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock']],
    'scissors': [['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'], ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire']],
    'snake': [['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'], ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors']],
    'human': [['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'], ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake']],
    'tree': [['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'], ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human']],
    'wolf': [['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'], ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree']],
    'sponge': [['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'], ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']],
    'paper': [['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'], ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge']],
    'air': [['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'], ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']],
    'water': [['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'], ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air']],
    'dragon': [['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'], ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water']],
    'devil': [['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'], ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon']],
    'lightning': [['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'], ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil']],
    'gun': [['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'], ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning']]}
    normal = {'rock': [['scissors'],['paper']],
            'paper': [['rock'],['scissors']],
            'scissors': [['paper'],['rock']]}
    game = {}
    score = 0
    new = 1
    def finish(self):        
        if Game.new == 1:
            scores = open('C:/Users/msemi/Documents/Work_Space/tried_projects/rsp_multiVariabled/scores.txt', 'a')
            scores.write(f'{Game.user_name} {Game.score}\n')
        else:
            scores = open('C:/Users/msemi/Documents/Work_Space/tried_projects/rsp_multiVariabled/scores.txt', 'r')
            lines = scores.readlines()
            scores.close()
            new_scores = open('C:/Users/msemi/Documents/Work_Space/tried_projects/rsp_multiVariabled/scores.txt', 'w')
            for line in lines:
                if Game.user_name in line:
                    new_scores.write(f'{Game.user_name} {Game.score}\n')
                    continue
                new_scores.write(line)
            new_scores.close()
    def starter(self):
        scores_2 = open('C:/Users/msemi/Documents/Work_Space/tried_projects/rsp_multiVariabled/scores.txt', 'r')
        Game.user_name = str(input('Enter your name: ')).replace(' ', '')
        print(f'Hello, {Game.user_name}')
        while True:
            try:    
                for i in scores_2:
                    if i.split()[0] == Game.user_name:
                        Game.new = 0
                        Game.score = int(i.split()[1])
                        break
                mod = str(input(f'Choose some from {list(Game.choices.keys())}\nif you want the normal mode, pass it-press enter!\n>')).replace(' ', '').split(',')
                if mod == ['']:
                    Game.game.update(Game.normal)
                else:
                    for item in mod:
                        Game.game[item] = Game.choices[item]
                print('"score" for your score\n"exit" to quit')
                print("Okay, let's start")
                scores_2.close()
                break
            except KeyError:
                print('Try again!\nWrite valid options')
                continue

def command_controller(taken):
    if taken == 'exit':
        raise Exception('B')
    elif taken == 'score':
        raise Exception('S')
    elif taken in Game.game.keys():
       return taken
    else:
        raise Exception('!')
def result_returner(taken_u, taken_c):
    computer_strong = Game.game[taken_c][0]
    computer_weak = Game.game[taken_c][1]
    # user_strong = Game.game[taken_u][0]
    # user_weak = Game.game[taken_u][1]

    if taken_u == taken_c:
        return f'There is a draw ({taken_c})', 50
    else:
        if taken_u in computer_strong:
            return f'Sorry, but the computer chose {taken_c}', 0
        elif taken_u in computer_weak:
            return f'Well done. The computer chose {taken_c} and failed', 100

Game.starter(0)
while True:
    try:
        taken_user = command_controller(str(input()))
        taken_computer = random.choice(list(Game.game.keys()))
        answer = result_returner(taken_user, taken_computer)
        Game.score += answer[1]
        print(answer[0])
    except Exception as inp:
        value = inp.args[0]
        if value == '!':
            print('Invalid input')
            continue
        elif value == 'S':
            print(f'Your rating: {Game.score}')
            continue
        elif value == 'B':
            print('Bye!')
            Game.finish(0)
            break