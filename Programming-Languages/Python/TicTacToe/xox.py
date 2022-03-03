import string
class Xox:
    lst = ''
    places = ['' for _ in range(9)]
    put = 'X'
    def place_adder(self):
        result = 0
        remained = 0
        for i, item in enumerate(Xox.lst):
            result = int(i/3) + 1
            remained = 3 if (i + 1) % 3 == 0 else (i + 1) % 3
            if item in 'XO':
                Xox.places[i] = f'({result},{remained}) taken'
            else:
                Xox.places[i] = f'(~{result},{remained} not taken)'
    def sign_adder(self, coordinate):
        first = Xox.lst[:coordinate]
        last = Xox.lst[coordinate + 1:]
        Xox.lst = first + self + last
    def put_new(self):
        if self.put == 'X':
            self.put = 'O'
        else:
            self.put = 'X'
class PlaceTakenError(ValueError):
    pass
class CoordinateError(ValueError):
    pass
class CharacterError(ValueError):
    pass
class Continue(ValueError):
    pass
def placer(place):
    for item in Xox.places:
        if item[:5] == f'({place[0]},{place[1]})': 
            raise PlaceTakenError
    # sonraki sistem
    if place == (1,1):
        return 0
    elif place == (1,2):
        return 1
    elif place == (1,3):
        return 2
    elif place == (2,1):
        return 3
    elif place == (2,2):
        return 4
    elif place == (2,3):
        return 5
    elif place == (3,1):
        return 6
    elif place == (3,2):
        return 7
    elif place == (3,3):
        return 8
    else:
        raise CoordinateError
def adder(taken):
    result = [[],[],[]]
    for i in range(len(taken)):
        if i == 2:
            result[0] = [item for item in taken[:3]]
        elif i == 5:
            result[1] = [item for item in taken[3:6]]
        elif i == 8:
            result[2] = [item for item in taken[6:9]]
    return result
def control_printer(result, impossbl, x, o):
    if impossbl == 1:
        return 'Impossible'
    elif x == 1 and o == 0:
        # return 'X wins'
        raise Exception('X')
    elif x == 0 and o == 1:
        # return 'O wins'
        raise Exception('O')
    elif x == 1 and o == 1:
        return 'Impossible'
    elif x == 0 and 0 == 0 and ' ' not in result:    
        # return 'Draw'
        raise Exception('D')
    # else:
    #     return 'Game not finished'
def co_checker(taken):
    if not taken:
        raise Continue
    for item in taken:
        for part in item:
            if part in string.digits:
                pass
            else:
                raise CharacterError
def impsbl_checker(result):
    count_x = 0
    count_o = 0
    impossbl = 0
    for i in result:
        if i in 'X':
            count_x += 1
        elif i in 'O':
            count_o += 1

    if count_x + count_o == 9 and (count_o != 0 and count_x != 0):
        if count_x > 5 or count_o > 5:
            impossbl == 1
    else:
        if count_x == count_o:
            impossbl = 0
        elif count_x == count_o + 1:
            impossbl = 0
        else:
            impossbl = 1
     
    return impossbl
def controller(taken):
    result = taken
    impossbl = impsbl_checker(result)
    x = 0
    o = 0
    # for two different possibilities
    rows = [result[0:3], result[3:6], result[6:9]]
    crosses = [result[2] + result[4] + result[6], result[0] + result[4] + result[8]]
    columns = [result[0] + result[3] + result[6], result[1] + result[4] + result[7], result[2] + result[5] + result[8]]
    # for rows
    if rows[0] == 'XXX' or rows[1] == 'XXX' or rows[2] == 'XXX':
        x = 1
    elif rows[0] == 'OOO' or rows[1] == 'OOO' or rows[2] == 'OOO':
        o = 1
    # for columns
    elif columns[0] == 'XXX' or columns[1] == 'XXX' or columns[2] == 'XXX':
        x = 1
    elif columns[0] == 'OOO' or columns[1] == 'OOO' or columns[2] == 'OOO':
        o = 1
    # for crosses
    elif crosses[0] == 'XXX' or crosses[1] == 'XXX':
        x = 1
    elif crosses[0] == 'OOO' or crosses[1] == 'OOO':
        o = 1
    return control_printer(result, impossbl, x, o)
def image_printer(taken):
    # adds the blank spaces
    for i in range(len(taken)):
        taken[i].insert(1, ' ')
        taken[i].insert(3, ' ')
    # adds the others
    print('---------')
    for lst in taken:
        print('| ',end='')
        for item in lst:
            print(item,end='')
        print(' |')
    print('---------')
# initiator
Xox.lst = ' '* 9
Xox.place_adder(Xox.lst) 
# # first
typeOf = controller(Xox.lst)
matrices = adder(Xox.lst)
image_printer(matrices)
if typeOf is not None:
    print(typeOf)

while True:
    try:
        second_take = str(input('Enter the coordinates:')).split(' ')
        co_checker(second_take)
        coordinate = placer((int(second_take[0]), int(second_take[1])))
        Xox.sign_adder(Xox.put, coordinate)
        matrices = adder(Xox.lst)
        image_printer(matrices)
        typeOf = controller(Xox.lst)
        Xox.place_adder(Xox.lst)
        if typeOf is not None:
            print(typeOf)
        Xox.put_new(Xox)
    except CharacterError:
        print(f'You should enter numbers!')
    except CoordinateError:
        print(f'Coordinates should be from 1 to 3!')
    except PlaceTakenError:
        print(f'This cell is occupied! Choose another one!')
    except Continue:
        continue
    except Exception as end:
        value = end.args[0]
        if value == 'X':
            print('X wins')
            break
        elif value == 'O':
            print('O wins')
            break
        elif value == 'D':
            print('Draw')
            break
        else:
            print('Unknown insertion')
            continue
        