import multiprocessing as mp

def square(x):
    return x * x

if __name__ == '__main__':
    with mp.Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    
    print(results)  # 输出: [1, 4, 9, 16, 25]