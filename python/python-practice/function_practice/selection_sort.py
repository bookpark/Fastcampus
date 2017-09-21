sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

def sequential_search(seq):
    length = len(seq)
    for i in range(length):
        min_index = i
        min_value = seq[i]

        for j in range(i, length):
            if seq[j] < min_value:
                min_index = j
                min_value = seq[j]
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq

result = sequential_search(sample)
print(result)
