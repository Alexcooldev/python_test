def decor(fu):
    def wrapper(*args):
        print("Декоратор начал свою работу")

        def recursive_fu(n):
            if n <= 0:
                return 8
            else:
                return n * recursive_fu(n-1)
        result = fu(*args)
        print("Декоратор завершил свою работу")
        return result
    return wrapper

@decor
def fyko(x):
    print("Вызвана функция fyko с аргументом", (x))


fyko(9)
