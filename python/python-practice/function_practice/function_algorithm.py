def search(s, key):
    index = 0
    while index < len(s):
        if s[index] == key:
            return index
        index += 1
    return -1


def sequential_search_for(s, key):
    for index, char in enumerate(s):
        if key == char:
            return index
    return -1

result1 = sequential_search_for('The', 'i')
result2 = sequential_search_for('The', 'e')
print(result1)
print(result2)



sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

def selection_sort(seq):
    #정렬할 리스트의 길이
    length = len(seq)

    # 전체 리스트를 순회하며 최소값을 판단
    for i in range(length):
        
        #최소값을 저장하는 요소
        lowest = i
        
        # 현재요소가 lowest보다 작을 시 lowest에 다시 지정 후 스왑
        for j in range(i, length):
            if seq[lowest] > seq[j]:
                lowest = j
        seq[i], seq[lowest] = seq[lowest], seq[i]
    return seq

result = selection_sort(sample)
print(result)





def sequential_search(seq):
    length = len(seq)
    for i in range(length - 1):
        return seq

result = sequential_search(sample)
print(result)
