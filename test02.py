import test03


def add_add():
    result = test03.add(1, 2)
    result += 2
    print(result)
    return result


if __name__ == '__main__':
    add_add()
