from Node import Node 
class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,node: Node):
        currentHead = self.head
        if currentHead == None:
            currentHead = node 
            self.head = currentHead
        else:
            #loop till the last item of 
            #list, then insert the new node 
            while(currentHead.next != None):
                currentHead = currentHead.next
                currentHead.next = node
                node.next = None 

    def item_counts(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count +=1
        return count
    
    def display(self):
        currentNode = self.head
        print("", end = "")
        while currentNode != None:
            print("|", currentNode.content, "| --->", ends ="" )
            currentNode = currentNode.next
        print("NULL \n")

    
    def delete (self, content_to_delete):

        current_head = self.head
        if current_head != None and current_head.content == content_to_delete:
            head = head.next
            current_head.next = None
            current_head = None
            return
        
        while current_head != None and current_head.next.content != content_to_delete:
            if current_head.next == content_to_delete:
                node_to_delete = current_head.next
                current_head.next = current_head.next.next 
                node_to_delete.next = None 
                node_to_delete = None 
            current_head = current_head.next

        
        