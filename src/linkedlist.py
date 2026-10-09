class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, x, data):
        current = self.head
        while current and current.data != x:
            current = current.next
        if current:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Element tapıldı.")
                return
            current = current.next
        print("Element tapılmadı.")

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def max_min(self):
        current = self.head
        mx = mn = current.data
        while current:
            if current.data > mx:
                mx = current.data
            if current.data < mn:
                mn = current.data
            current = current.next
        return mx, mn

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    # Tapşırıq 1
    Node(15)

    # Tapşırıq 2
    l = LinkedList()
    for v in [10, 20, 30, 40]:
        l.insert_at_end(v)
    l.display()

    # Tapşırıq 3
    l = LinkedList()
    for v in [20, 30, 40]:
        l.insert_at_end(v)
    l.insert_at_beginning(10)
    l.display()

    # Tapşırıq 4
    l = LinkedList()
    for v in [10, 20, 40]:
        l.insert_at_end(v)
    l.insert_after(20, 30)
    l.display()

    # Tapşırıq 5
    l = LinkedList()
    for v in [10, 20, 30, 40, 50]:
        l.insert_at_end(v)
    l.delete(30)
    l.display()

    # Tapşırıq 6
    l.search(40)
    l.search(99)

    # Tapşırıq 7
    l = LinkedList()
    for v in [11, 22, 33, 44, 55]:
        l.insert_at_end(v)
    print("List length =", l.length())

    # Tapşırıq 8
    l = LinkedList()
    for v in [23, 8, 91, 15, 42]:
        l.insert_at_end(v)
    mx, mn = l.max_min()
    print("Maksimum element =", mx)
    print("Minimum element =", mn)

    # Tapşırıq 9
    l = LinkedList()
    for v in [10, 20, 30, 40, 50]:
        l.insert_at_end(v)
    l.reverse()
    l.display()
