def f1(x):
    x =3
    def f2():
        print(x)
    return f2
x = f1(3)
x()


