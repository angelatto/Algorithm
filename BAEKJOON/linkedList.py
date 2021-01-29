class Node:
    def __init__(self, data, next=None):
        print("init 진입 ")
        self.data = data
        self.next = next
#--------------------------------------------------------------------
def init_list():
    print("init list 진입 ")
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.n_dir

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.n_dir = next_node.n_dir
            del next_node
            break
        pre_node = next_node
        next_node = next_node.n_dir


def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node

def print_list():
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print


if __name__ == "__main__":
    all = int(input());
    init_list() #연결리스트 초기화
    print_list()
