from Etat import Etat
import time
import bisect

etat_final = Etat(matrix=[[0,1,2],[3,4,5],[6,7,8]])
etat_init = etat_final.shuffle(5) #Etat(matrix=[[3,1,2],[4,5,0],[6,7,8]], etat_final=etat_final)
#etat_init = etat_final.shuffle(5)
#etat_final = Etat(matrix=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
#etat_init = Etat(matrix=[[3,1,2,9],[4,5,10,0],[6,7,12,8],[11,13,14,15]],etat_final=etat_final)
etat_visited = {}
etat_list = [etat_init]
total_iterations = 0

def recherche_A():
    global total_iterations
    while etat_list and etat_list[0] != etat_final:
        total_iterations += 1
        if(total_iterations % 50000 == 0):
            print(f"total_iterations = {total_iterations}")
        etat_first = etat_list[0]
        etat_visited[etat_first.get_hash()] = True
        etat_list.pop(0)
        if etat_first.canGoUp():
            etat_up = etat_first.up()
            if not etat_up.get_hash() in etat_visited:
                insert_sorted_by_heuristic(etat_up)
        if etat_first.canGoRight():
            etat_right = etat_first.right()
            if not etat_right.get_hash() in etat_visited:
                insert_sorted_by_heuristic(etat_right)
        if etat_first.canGoDown():
            etat_down = etat_first.down()
            if not etat_down.get_hash() in etat_visited:
                insert_sorted_by_heuristic(etat_down)
        if etat_first.canGoLeft():
            etat_left = etat_first.left()
            if not etat_left.get_hash() in etat_visited:
                insert_sorted_by_heuristic(etat_left)
        #print(f"depth = {stack}")
    print(f"result found after {total_iterations} iterations")
    print(etat_list[0].toString())

def insert_sorted_by_heuristic(etat):
    #print('insert sorted called')
    if(not etat_list):
        etat_list.append(etat)
    else:
        bisect.insort(etat_list, etat, key = lambda e: e.get_heuristic() + e.depth)

print("initial state:")
print(etat_init.toString())
start_time = time.time()
print("start")
recherche_A()
print("end")
end_time = time.time()
print(f"time taken = {(end_time - start_time)*1000}ms")