def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)


def moveDisk(disk, fromPole, toPole):
    print('disk[{}] from {} to {} '.format(disk, fromPole, toPole))


moveTower(4, '#1', '#2', '#3')
