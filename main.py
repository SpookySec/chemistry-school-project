from programtable import table

try:
    option = '0'

    while option in table.keys():
        table[option]()
        option = input('>> ').strip()

    else:
        print('Goodbye')

except KeyboardInterrupt:
    print('Goodbye')