idade = int(input('digite a idade do nadador: '))

if idade >=18:
    print('adulto')
elif idade >= 14 and idade < 18:
    print('juvenil')
elif idade >= 9 and idade < 14:
    print('infantil')
elif idade < 9:
    print('mirim')