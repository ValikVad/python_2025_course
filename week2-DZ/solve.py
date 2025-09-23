import random
mass = []
for i in range(20):
    mass.append(random.randint(1, 25))


mass = [2, 2, 4]


def find_size(l1, l2, h1, h2):
    return abs(l2-l1-1)*min(h1, h2)

def max_container(mass: list[int]):
    ans = 0
    ind1 = 0; ind2 = len(mass)-1
    while ind1!=ind2:
        ans = max(ans, find_size(ind1, ind2, mass[ind1], mass[ind2]))
        if mass[ind1]>mass[ind2]:
            ind2-=1
        else:
            ind1+=1
    return ans
print(max_container(mass))
