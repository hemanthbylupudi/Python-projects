def bubble_sort(a1, a2):
    n = len(a1)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a1[j] > a1[j + 1]:
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
                a2[j], a2[j + 1] = a2[j + 1], a2[j]
    return a2

# Taking input from the user
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
sorted_a2 = bubble_sort(a1, a2)
print(*sorted_a2)
