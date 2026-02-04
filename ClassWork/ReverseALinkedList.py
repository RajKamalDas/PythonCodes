class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    newHead = reverseList(head.next)

    head.next.next = head
    head.next = None

    return newHead


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
display(head)

head = reverseList(head)

print("Reversed List:")
display(head)
