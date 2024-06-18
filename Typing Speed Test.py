from time import time
def type_test():
    print("Click Enter to start Typing")
    print("Double Click Enter to stop Typing")
    new_list=[]
    input("--------------------------------------------------------")
    start = time()
    while True:
        n = input()
        if not n:
            break
        new_list.append(n)
    end = time()
    count = 0
    for i in new_list:
        count += (len(i))
    total_characters = count
    total_word = total_characters/5
    time_taken = (end-start)/60
    wpm = round((total_word/time_taken),3)
    return wpm

        
res= type_test()
print(res)
