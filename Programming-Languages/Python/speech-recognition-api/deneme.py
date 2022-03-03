import numpy as np
n = int(input("give me the number of soldiers"))
s_strengths = np.array(list(map(int, input(">").split())))
new_strengths = np.zeros(n)

m = int(input("give the number of dragons: "))

dragons = []
for _ in range(m):
   dragons.append(list(map(int, input("> ").split())))
dragons = np.array(dragons)

# attacked = np.zeros(n)
# defensed_chosed = np.zeros(n) 
needed_coins = 0
total = np.zeros((m, n))

for attack, defense in dragons:
    strengths_in = s_strengths - defense
    if len(np.where(strengths_in == 0)[0]) > 0:
        chosen = np.where(strengths_in == 0)[0]
    else:
       lowest = np.amin(strengths_in)
       needed_coins += lowest
       chosen = np.where(lowest == strengths_in)
    
    strengths_in = s_strengths - attack
    strengths_in = np.delete(strengths_in, chosen)
    total = strengths_in.sum() - attack 
    if total < 0:     
        needed_coins += abs(total) 
    print(final) 