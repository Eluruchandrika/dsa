def create_stack():
    stack = []
    return stack    

def push(stack, data):
    stack.append(data)

def pop(stack):
    if not isempty(stack):
        return stack.pop()

def isempty(stack):
    return len(stack) == 0

def move_disk(sou_st, des_st, sou, des):
    disk = pop(sou_st)
    push(des_st, disk)
    print("Move disk", "from", sou, "to", des)

def tower_of_honoi(n, sou, aux, des):
    sou_stack = create_stack()
    aux_stack = create_stack()
    des_stack = create_stack()
    for i in range(n, 0, -1):
        push(sou_stack, i)
    total_moves = (2 ** n) - 1
    if n % 2 == 0:
        aux, des = des, aux
    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            move_disk(sou_stack, des_stack, sou, des)
        elif move % 3 == 2:
            move_disk(sou_stack, aux_stack, sou, aux)
        elif move % 3 == 0:
            move_disk(aux_stack, des_stack, aux, des)

n = 4
tower_of_honoi(n, 'a', 'b', 'c')