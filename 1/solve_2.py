import queue

f = open('input')
input_lines = f.readlines()

total = 0
top_3 = queue.PriorityQueue(maxsize=3)
for line in input_lines:
    try:
        total = total + int(line)
    except ValueError:
        pass # We don't care about non-numeric lines
    
    
    if len(line.strip('\n')) == 0 or line == input_lines[-1]:
        if len(top_3.queue) == 0 or any([total >= x for x in top_3.queue]):
            if top_3.full():
                top_3.get()
            top_3.put(total)
        total = 0

print(sum(top_3.queue))