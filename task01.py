import timeit

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(total: int):
    """
    Find a way to provide return to customer in coins using greedy algorithm
    That means - to give as bigger coin as possible each time
    """
    result = { coin : 0 for coin in COINS }
    for coin in COINS:
        result[coin] = total // coin
        total = total % coin
    return { coin:quantity for coin, quantity in result.items() if quantity > 0 }

def find_min_coins(total: int):
    """
    Find an optimal way to provide return to customer 
    using methods of dynamic programming 
    """
    results = { i:{ coin : 0 for coin in COINS } for i in range(0, total+1) }
    for i in range(0, total+1):
        results[i]["total"] = 0
    for coin in COINS[::-1]:
        for i in range(0, total+1-coin):
            if (results[i]["total"] + 1 < results[i+coin]["total"]) or results[i+coin]["total"] == 0:
                results[i+coin]["total"] = results[i]["total"] + 1
                for cc in COINS:
                    results[i+coin][cc] = results[i][cc]
                results[i+coin][coin] += 1
    #for key, value in results.items():
    #    print(f"{key} => {value}")
    return { coin:quantity for coin, quantity in results[total].items() if quantity > 0 and coin in COINS }

for i in [1001, 1234, 2345]:
    print(f"Greedy algorithm performance: value {i}, 100 repeats per each value:")
    print(timeit.timeit('find_coins_greedy(i)', number=100, globals=globals()))

for i in [1001, 1234, 2345]:
    print(f"Dynamic algorithm performance: value {i}, 100 repeats per each value:")
    print(timeit.timeit('find_min_coins(i)', number=100, globals=globals()))

    
