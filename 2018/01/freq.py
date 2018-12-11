"""Sum data in a text file until the first duplicate sum is reached."""


def get_numbers():
    with open('data.txt', 'r') as file:
        for row in file:
            yield int(row)


def main():
    sum = 0
    sums = set()
    while True:
        for number in get_numbers():
            sum += number
            if sum in sums:
                return sum
            sums.add(sum)


if __name__ == '__main__':
    print(main())
