class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        if not del_node.next:
            del_node=none
        else:
            del_node.data=del_node.next.data
            del_node.next=del_node.next.next
            
