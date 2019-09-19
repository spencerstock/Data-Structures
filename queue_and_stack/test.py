
from doubly_linked_list import DoublyLinkedList


myList = DoublyLinkedList()
list: 0,1,2,3,4,5,6,7,8,9,10,None



fastnode = root
slowNode = root
while fastNode:
  slowNode = slowNode.next 
  if not fastnode.next:
    break
  fastNode = fastnode.next.next

return slowNode