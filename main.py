# рекурсія

from numpy import random
import time
start_time = time.time()

def Generate(perestanovki, elements, positions):
    # якщо кількість елементів масиву з уже переставленими елементами (perestanovki) = довжині вхідного масиву (
    # elements), то виконувати цикл for

    if (len(perestanovki) == len(elements)):

        for it in perestanovki:
            print(it, end=' ')
        print('\n')

    # якщо кількість елементів масиву з уже переставленими елементами (perestanovki) НЕ = довжині вхідного масиву (
    # elements), то виконується наступний цикл for

    else:

        for i in range(0, len(elements)):

            if (positions[i]):
                continue

            # встановлюємо позицію, додаємо елемент до масиву з переставленими елементами
            positions[i] = True
          #  print(positions)
            perestanovki.append(elements[i])

            # викликаємо функцію, щоб перевірити чи кількість елементів масиву з уже переставленими елементами (
            # perestanovki) = довжині вхідного масиву (elements) якщо так, то виконується цикл for під першим if,
            # який виводить масив з переставленими елементами якщо ні, то беремо наступний елемент з вхідного масиву
            # (elements) і вставляємо його в масив (perestanovki) і так буде до тих пір, поки кількість елементів
            # масиву з уже переставленими елементами (perestanovki) = довжині вихідного масиву (elements)
            Generate(perestanovki, elements, positions)

            # видаляє позицію, видаляємо елемент з масиву з переставленими елементами
            positions[i] = False
         #   print(positions)
            perestanovki.pop()

# масив для зберігання переставлених елементів
perestanovki = []

size = input("Кількість елементів масиву : ")
# через метод randint створюємо масив з випадковими числами
elements = random.randint(1000, size=(int(size)))

print(elements)
print("\n")

# for i in range(0, int(size)):
#     x = input("Елемент " + str(i) + " : ")
#     elements.append(x)

positions = [False] * int(size)

print("\nПерестановки:\n")

Generate(perestanovki, elements, positions)

print("--- %s секунд ---" % (time.time() - start_time))
