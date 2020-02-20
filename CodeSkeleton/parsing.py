def parse(filename):
    with open(filename, 'r') as fi:
        knapsize, ntypes = map(int,fi.readline().split())
        pizzas = list(map(int, fi.readline().split()))
        assert pizzas == sorted(pizzas)
        dataset = {
            'pizzas': pizzas,
            'knapsize': knapsize}
        return dataset