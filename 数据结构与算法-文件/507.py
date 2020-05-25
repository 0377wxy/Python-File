def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, frist, last):
    if frist < last:
        splitpoint = partition(alist, frist, last)
        quickSortHelper(alist, frist, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, frist, last):
    pivotvale = alist[frist]
    leftmark = frist+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvale:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvale:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[frist], alist[rightmark] = alist[rightmark], alist[frist]
    return rightmark


alist = [23, 67, 26, 13, 57, 96, 35, 34]
quickSort(alist)
print(alist)
