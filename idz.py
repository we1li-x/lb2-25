#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import multiprocessing

def compute_sum(x, eps, result_queue):
    n = 0
    sum = 0
    while True:
        term = (x ** n * (math.log(3)) ** n) / math.factorial(n)
        if abs(term) < eps:
            break
        sum += term
        n += 1
    result_queue.put(sum)

def compare_sums(x, y, eps):
    result_queue1 = multiprocessing.Queue()
    result_queue2 = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=compute_sum, args=(x, eps, result_queue1))
    process2 = multiprocessing.Process(target=compute_sum, args=(y, eps, result_queue2))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    sum1 = result_queue1.get()
    sum2 = result_queue2.get()

    print(f"Сумма ряда для x: {sum1}")
    print(f"Сумма ряда для y: {sum2}")

    if abs(sum1 - sum2) < eps:
        print("Суммы рядов равны.")
    else:
        print("Суммы рядов не равны.")

if __name__ == "__main__":
    compare_sums(1, 3 ** 1, 10 ** -7)
