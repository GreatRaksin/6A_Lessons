def post_office(name):
    print(f'{name}\nBelskogo 15,\n220082, Minsk, Belarus')


def taxes(price, rate):
    tax = price * rate / 100
    summary = price + tax
    return tax, summary

post_office('Demid Raksin')
tax_res, sum_res = taxes(848, 6)
print(f'Сумма налога ${tax_res}, итоговая стоимость ${sum_res}')