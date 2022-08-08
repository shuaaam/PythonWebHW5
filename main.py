import requests
from time import time
from multiprocessing import Pool, cpu_count
from time import sleep


def factorize(*number):
    values = []
    for n in number:
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        values.append(result)
    return values


if __name__ == "__main__":
    timer = time()
    print(f'Starting simple script: {timer}')

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    time_passed = time() - timer

    print(f'Time passed (simple script): {time_passed}')
    print(f'Values :\n {a},\n {b},\n {c},\n {d}')

    nums = a, b, c, d

    sleep(3)
    timer = time()
    print(f'Starting multiprocessing script: {timer}')

    with Pool(cpu_count()) as pool:
        pool.map_async(factorize, nums, callback=print)
        pool.close()
        pool.join()

    time_passed = time() - timer
    print(f'Time passed (multiprocessing script): {time_passed}')
    print(f'Values :\n {a},\n {b},\n {c},\n {d}')
