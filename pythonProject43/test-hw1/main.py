# Есть строка - посчитать количество каждой из букв

# aabbccdd

#Множество - список только уникальных значений aabcd -> abcd

# def strconter(s):
#     for symbol in set(s): # отвечает за перебор искомых значений
#         counter = 0
#         for sub_symbol in s: # отвечает за подсчет количества искомого сивола в строке
#             if symbol == sub_symbol:
#                 counter +=1
#         print(symbol, counter)
#
# strconter("aabcd")

def strcounter(s):  # O(2N) -> O(N)
    syms_counter ={}
    for symbol in s:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1

    for symbol, count in syms_counter.items():
        print(symbol, count)

strcounter("aabbccdd")