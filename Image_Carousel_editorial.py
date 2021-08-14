# Class that represents a Node.
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Class that forms and maintains a Doubly linked list
class DoublyLinkedList:

    # Initializing head, so that we can always retain pointer to head.
   def __init__(self):
      self.head = None

    # Method which pushes a node in Doubly linked list.
   def node_push(self, new_value):
      new_node = Node(new_value)
      new_node.next = self.head
      if self.head is not None:
         self.head.prev = new_node
      self.head = new_node


# Method which will print the entire list.
def list_print(node):
    while node:
        print(node.data)
        last = node
        node = node.next

# Method which holds and displays the current image.
def display_image(node):
    print("Displaying image:")
    print(node.data)

# Method which helps us move forward in the image carousel.
def go_forward(node):
    print("moving forward")
    display_image(node.next)
    return node.next

# Method which helps us move backwards in the image carousel.
def go_back(node):
    print("going back")
    display_image(node.prev)
    return node.prev

# This is the 'main' driver method
if __name__ == '__main__':
    # Instantiating the Doubly linked list
    dll = DoublyLinkedList()

    # Pushing nodes
    dll.node_push("horse.png")
    dll.node_push("cat.png")
    dll.node_push("mouse.png")
    dll.node_push("lion.png")
    dll.node_push("hippo.png")

    #Printing the entire list
    list_print(dll.head)

    # Displaying images from head
    display_image(dll.head)

    # swap will behave as current image holder which is being displayed.
    swap = go_forward(dll.head)
    swap = go_forward(swap)
    swap = go_forward(swap)
    swap = go_back(swap)

