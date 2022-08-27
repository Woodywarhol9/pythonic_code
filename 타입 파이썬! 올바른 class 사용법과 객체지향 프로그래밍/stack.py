from typing import Optional

class Node:
    def __init__(self, item, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
    
    @property
    def length(self):
        if self.head is None:
            return 0
        cur_node : Node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count
    
    def __str__(self) -> str:
        result : str = ""
        if self.head is None:
            return result
        cur_node: Node = self.head
        result += f"{cur_node.item}"
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"
        return result

class Stack(LinkedList):
    def push(self, item) -> None:
        new_node: Node = Node(item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node
        
    def pop(self):
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            cur_node = self.head
        if cur_node.pointer is None:
            return cur_node.item
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer     
        result = cur_node.pointer
        cur_node.pointer = None
        
        return result.item

if __name__ == "__main__":
    stack = Stack()
    stack.push(12)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    stack.pop()
    print(stack.length)
    print(stack)