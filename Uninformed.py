from Etat import Etat
import time
etat_final = Etat(matrix=[[0,1,2],[3,4,5],[6,7,8]])
etat_init = etat_final.shuffle(5) #Etat(matrix=[[3,1,2],[4,5,0],[6,7,8]], etat_final=etat_final)
#etat_init = etat_final.shuffle(5)
#etat_final = Etat(matrix=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
#etat_init = Etat(matrix=[[3,1,2,9],[4,5,10,0],[6,7,12,8],[11,13,14,15]],etat_final=etat_final)
etat_visited = {}
etat_list = [etat_init]
total_iterations = 0

def print_list(list):
    for elem in list:
        print(elem.toString())

def recherche_largeur():
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
                etat_list.append(etat_up)
        if etat_first.canGoRight():
            etat_right = etat_first.right()
            if not etat_right.get_hash() in etat_visited:
                etat_list.append(etat_right)
        if etat_first.canGoDown():
            etat_down = etat_first.down()
            if not etat_down.get_hash() in etat_visited:
                etat_list.append(etat_down)
        if etat_first.canGoLeft():
            etat_left = etat_first.left()
            if not etat_left.get_hash() in etat_visited:
                etat_list.append(etat_left)
    print(f"result found after {total_iterations} iterations")
    print(etat_list[0].toString())
    print(etat_list[0].depth)

def recherche_profondeur_dab():
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
                etat_list.insert(0,etat_up)
        if etat_first.canGoRight():
            etat_right = etat_first.right()
            if not etat_right.get_hash() in etat_visited:
                etat_list.insert(0,etat_right)
        if etat_first.canGoDown():
            etat_down = etat_first.down()
            if not etat_down.get_hash() in etat_visited:
                etat_list.insert(0,etat_down)
        if etat_first.canGoLeft():
            etat_left = etat_first.left()
            if not etat_left.get_hash() in etat_visited:
                etat_list.insert(0,etat_left)
    print(f"result found after {total_iterations} iterations")
    print(etat_list[0].toString())
    print(etat_list[0].depth)

def recherche_profondeur_limitee(depth):
    global total_iterations

    etat_visited = {}
    stack = []
    etat_list = [etat_init]
    while etat_list and etat_list[0] != etat_final:
        total_iterations += 1
        etat_first = etat_list[0]
        etat_visited[etat_first.get_hash()] = True
        etat_list.pop(0)
        nb_childern = 0
        if len(stack)!=depth:
            if etat_first.canGoUp():
                etat_up = etat_first.up()
                if not etat_up.get_hash() in etat_visited:
                    nb_childern += 1
                    etat_list.insert(0,etat_up)
            if etat_first.canGoRight():
                etat_right = etat_first.right()
                if not etat_right.get_hash() in etat_visited:
                    nb_childern += 1
                    etat_list.insert(0,etat_right)
            if etat_first.canGoDown():
                etat_down = etat_first.down()
                if not etat_down.get_hash() in etat_visited:
                    nb_childern += 1
                    etat_list.insert(0,etat_down)
            if etat_first.canGoLeft():
                etat_left = etat_first.left()
                if not etat_left.get_hash() in etat_visited:
                    nb_childern += 1
                    etat_list.insert(0,etat_left)
        if(stack):
            stack[len(stack)-1] -= 1
        if(nb_childern!=0):
            if(len(stack)!=depth):
                if(stack and stack[len(stack)-1]==0):
                    stack.pop()
                stack.append(nb_childern)
        else:
            if(stack and stack[len(stack)-1]==0):
                stack.pop()
    if(etat_list):
        print(f"result found after {total_iterations} iterations")
        print(etat_list[0].toString())
        print(f"state depth = {etat_list[0].depth}")
        return True
    else:
        return False

def recherche_profondeur_iter():
    depth = 0
    print("depth = 0")
    while not recherche_profondeur_limitee(depth=depth):
        depth += 1
        print(f"depth = {depth}")
    print(f"found at depth {depth}")


print("initial state:")
print(etat_init.toString())
start_time = time.time()
print("start")
recherche_profondeur_iter()
print("end")
end_time = time.time()
print(f"time taken = {(end_time - start_time)*1000}ms")

# result_stats = {"iterations":[],"temps":[]}
# for x in range(10):
#     etat_final = Etat(matrix=[[0,1,2],[3,4,5],[6,7,8]])
#     etat_init = etat_final.shuffle(5*x)
#     etat_visited = {}
#     etat_list = [etat_init]
#     total_iterations = 0
#     print("initial state:")
#     print(etat_init.toString())
#     start_time = time.time()
#     print("start")
#     recherche_A()
#     print("end")
#     end_time = time.time()
#     print(f"time taken = {(end_time - start_time)*1000}ms")
#     result_stats["iterations"].append(total_iterations)
#     result_stats["temps"].append(int((end_time - start_time)*1000))
#     #print(etat_init.depth)
#     #for item in etat_list:
#     #    print(item.depth)

# print(result_stats)


