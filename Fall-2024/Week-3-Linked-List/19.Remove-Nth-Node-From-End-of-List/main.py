# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummyNode = ListNode()
    dummyNode.next = head
    a = b = dummyNode
    
    for i in range(0,n+1): # if n = 2 => loop 0 to 2
    #we want n + 1 so later behind can stop at the node before the node we need to delete
    #since if we loop with n, behind will stop right at the node we ean to delete
    #the key is too maintain the n position betwen ahead and behind
        a = a.next
    while a != None:
        b = b.next
        a = a.next
    b.next = b.next.next

    return dummyNode.next

def main():
    print(f"this is the result: {removeNthFromEnd([1,2,3,4,5], 2)}")
                                   
if __name__ == "__main__":
    main()