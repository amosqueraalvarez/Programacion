# boletin 4.1

articulo = 10000


if articulo <= 100:
    print('Articulo de bajo consumo')
else:
    if articulo > 100 and articulo <= 500:
        print('Articulo de consumo medio')
    else:
        if articulo > 500 and articulo <= 1000:
            print('Articulo de alto consumo')
        else:
            if articulo > 1000:
                print('Articulo de primera necesidad')
