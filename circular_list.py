from email import header
from time import sleep

class Node:
    code: str = ''
    name: str = ''
    salary: int = 0
    next = None

    def __init__(self, code: str, name: str, salary: int) -> None:
        self.code = code
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return "this is a node with name {} and code {}".format(self.name, self.code)

class List:
    head: Node = None

    def add_node(self, node:Node):
        if not self.head:
            self.head = node
            node.next = node
        else:
            node.next = self.head
            temp = self.head
            while temp.next is not None and temp.next != self.head:
                temp = temp.next
            temp.next = node

    def print_list(self):
        # Print head
        print(f"Node {self.head}")

        # Print other nodes
        node = self.head.next
        while node !=self.head:
            print(f"Node {node}")
            node = node.next

        # Print head in circular round
        print(f"Node {node}")

