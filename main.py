from circular_list import Node, List

def main():
    list = List()
    
    # Add first item in list
    list.add_node(Node(name="Juan Sanchez", code='20171020131', salary=3000))
    # Add second item in list
    list.add_node(Node(name="Julian Barrios", code='20171020123', salary=3500))
    # Add third item in list
    list.add_node(Node(name="Eliana Gonzalez", code='20171020145', salary=4000))
    # Add fourth item in list
    list.add_node(Node(name="Nicolas Alarancon", code='20171020102', salary=1000))

    list.print_list()

if __name__ == '__main__':
    main()