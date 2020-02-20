def score(solution, dataset):
    res = 0
    for idx in solution:
        res += dataset['pizzas'][idx]
    return 0 if res > dataset['knapsize'] else res