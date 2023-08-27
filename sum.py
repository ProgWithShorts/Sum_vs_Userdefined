import time

x = []
count = 0
while (count < 10_000_000):
    count += 1
    x.append(count)

start = time.time()
sum(x)
end = time.time()

print((end-start)*1000, " ms")
