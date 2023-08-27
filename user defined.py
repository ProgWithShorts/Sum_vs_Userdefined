import time

x = []
count = 0
while (count < 10_000_000):
    count += 1
    x.append(count)


def total(list):
    total = 0
    for num in list:
        total += num
    return total


start = time.time()
total(x)
end = time.time()

print((end-start)*1000, " ms")
