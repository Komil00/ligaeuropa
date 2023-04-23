# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         dict = {'(' : ')', '[' : ']', '{' : '}'}
#         stack = []
#         for i in s:
#             if i in dict.keys():
#                 stack.append(i)
#             else:
#                 if stack == []:
#                     return False
#                 a = stack.pop()
#                 print(a)
#                 if i!= dict[a]:
#                     return False
#         return stack == []
    
# x = Solution()
# print(x.isValid('{}()'))


# import ccxt
# import time

# # Создаем объект для доступа к бирже Binance
# exchange = ccxt.binance()

# # Список цен
# prices = []

# while True:
#     # Запрашиваем текущую цену фьючерса ETHUSDT
#     ticker = exchange.fetch_ticker('ETH/USDT')
#     price = ticker['last']

#     # Добавляем цену в список
#     prices.append(price)

#     # Если список содержит больше 60 цен, удаляем первую цену
#     if len(prices) > 60:
#         prices.pop(0)

#     # Если список содержит 60 цен, вычисляем процентное изменение цены
#     if len(prices) == 60:
#         percent_change = ((prices[-1] - prices[0]) / prices[0]) * 100

#         # Если процентное изменение цены превышает 1%, выводим сообщение в консоль
#         if abs(percent_change) > 1:
#             print(f'Price changed by {percent_change}% over the last 60 minutes')

#     # Задержка выполнения программы на 1 секунду
#     time.sleep(1)


# import ccxt
# import time

# # Создаем объект для работы с биржей Binance
# exchange = ccxt.binance()

# # Устанавливаем пару ETH/USDT
# symbol = 'ETH/USDT'

# # Задаем период для скользящего среднего в минутах
# ma_period = 60

# # Инициализируем переменные для хранения предыдущего и текущего значений цены
# prev_price = None
# curr_price = None

# # Запускаем бесконечный цикл, который будет выполняться до остановки программы
# while True:
#     try:
#         # Получаем актуальную цену для заданной пары
#         ticker = exchange.fetch_ticker(symbol)
#         curr_price = ticker['last']

#         # Если это первый запуск программы, то предыдущее значение цены равно текущей цене
#         if prev_price is None:
#             prev_price = curr_price
#             continue

#         # Вычисляем скользящее среднее для предыдущего периода
#         candles = exchange.fetch_ohlcv(symbol, '1m', limit=ma_period)
#         ma_price = sum([candle[4] for candle in candles])/ma_period

#         # Сравниваем текущую цену с ее средним значением за предыдущий период
#         price_change = (curr_price - ma_price)/ma_price

#         # Если цена изменилась на 1% или более, выводим сообщение в консоль
#         if abs(price_change) >= 0.01:
#             print(f"Price changed by {price_change:.2%} in the last {ma_period} minutes")

#         # Запоминаем текущее значение цены для следующей итерации цикла
#         prev_price = curr_price

#         # Добавляем задержку, чтобы не нагружать сервер биржи слишком частыми запросами
#         time.sleep(10)

#     # Обрабатываем ошибки при выполнении запросов к API биржи
#     except ccxt.BaseError as e:
#         print(f"Error occurred: {e}")

# import ccxt
# import time

# # Создаем объект для работы с биржей Binance
# exchange = ccxt.binance()

# # Устанавливаем пару BTC/USDT
# symbol = 'BNB/USDT'

# # Задаем период для скользящего среднего в минутах
# ma_period = 60

# # Инициализируем переменные для хранения предыдущего и текущего значений цены
# prev_price = None
# curr_price = None

# # Запускаем бесконечный цикл, который будет выполняться до остановки программы
# while True:
#     try:
#         # Получаем актуальную цену для заданной пары
#         ticker = exchange.fetch_ticker(symbol)
#         curr_price = ticker['last']

#         # Если это первый запуск программы, то предыдущее значение цены равно текущей цене
#         if prev_price is None:
#             prev_price = curr_price
#             continue

#         # Вычисляем скользящее среднее для предыдущего периода
#         candles = exchange.fetch_ohlcv(symbol, '1m', limit=ma_period)
#         ma_price = sum([candle[4] for candle in candles])/ma_period

#         # Сравниваем текущую цену с ее средним значением за предыдущий период
#         price_change = (curr_price - ma_price)/ma_price

#         # Если цена изменилась на 1% или более, выводим сообщение в консоль
#         if abs(price_change) >= 0.01:
#             print(f"Price changed by {price_change:.2%} in the last {ma_period} minutes")

#         # Запоминаем текущее значение цены для следующей итерации цикла
#         prev_price = curr_price

#         # Добавляем задержку, чтобы не нагружать сервер биржи слишком частыми запросами
#         time.sleep(10)

#     # Обрабатываем ошибки при выполнении запросов к API биржи
#     except ccxt.BaseError as e:
#         print(f"Error occurred: {e}")


# Консольное приложение на Python для создания списка целых чисел от 1 до 10 и вычисления суммы элементов:

# # python
# # Copy code
# # создаем список чисел от 1 до 10
# numbers = list(range(1, 11))

# # вычисляем сумму элементов списка
# sum_of_numbers = sum(numbers)

# # выводим результат на экран
# print("Сумма элементов списка:", sum_of_numbers)
# # Сначала мы создаем список чисел от 1 до 10 с помощью функции range() и преобразуем его в список с помощью функции list(). Затем мы вычисляем сумму элементов списка с помощью встроенной функции sum(). Наконец, мы выводим результат на экран с помощью функции print().



# # создаем список строк
# words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog']

# # сортируем список по алфавиту
# words.sort()

# # выводим результат на экран
# print("Список строк, отсортированных по алфавиту:")
# for word in words:
#     print(word)

#     # создаем кортеж из трех элементов разных типов данных
# my_tuple = ('apple', 5, 2.3)

# # выводим тип данных каждого элемента
# for item in my_tuple:
#     print("Элемент", item, "имеет тип данных", type(item))

# for i in range(10):
#     a=pow(i,i)
# with open('readme.txt') as books:
#     lines = books.readlines()
#     print(lines)
# lines.sort()
# with open('readme.txt', 'w') as sortedbooks:
#     sortedbooks.writelines(lines)
# # open('readme.txt', 'w').write(f'\n{a}')


# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)

# while True:
#     GPIO.output(18, True)
#     time.sleep(1)
#     GPIO.output(18, False)
#     time.sleep(1)

# pow(x,2
# import math
# print(math.sqrt(4))
# print('komil tursunboy')

# import shutil
# free_b = shutil.disk_usage('.')
# gb = pow(2,10)
# print(int(format(free_b))/gb)
# print(gb)

