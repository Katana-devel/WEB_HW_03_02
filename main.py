import time
from multiprocessing import Pool, cpu_count

def factorize(number):
    result = []
    for j in range(1, number + 1):
        if number % j == 0:
            result.append(j)
    return result

if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]

    print(f"cpu count: {cpu_count()}")
    with Pool(cpu_count()) as pool:
        start_time = time.perf_counter()
        parallel_results = pool.map(factorize, numbers)
        end_time = time.perf_counter()
        print(f"Результаты (параллельно): {parallel_results}")
        print(f"Время выполнения (параллельно): {end_time - start_time:.6f} секунд")