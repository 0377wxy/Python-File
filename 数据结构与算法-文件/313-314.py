class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getDate(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def sizs(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        fount = False
        while current != None and not fount:
            if current.getDate() == item:
                fount = True
            else:
                current = current.getNext()
        return fount

    def remove(self, item):
        currrent = self.head
        previous = None
        found = False
        while not found:
            if currrent.getDate() == item:
                found = True
            else:
                previous = currrent
                currrent = currrent.getNext()
        if previous == None:
            self.head = currrent.getNext()
        else:
            previous.setNext(currrent.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getDate() == item:
                found = True
            elif current.getDate() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getDate() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
