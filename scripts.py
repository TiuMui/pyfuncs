"""Скрипты проверки функций."""


def table_from_data():
    from terminal.tables import create_table
    from arrays.lists import normalizer_list_of_lists

    RAW_DATA = [
        ['Kjdwe', 'Jfbcewz', 10, 11, '12', False],
        ['Hgftye', 'Jhfewuc', '', True, ''],
        [False, 'Hfkevrr vrev'],
        ['Kjfhdfbdfb dfbye', 'Nvcbyev', '', '', 5],
        ['1', ],
        ['', '', 3, True, '']
    ]

    normalize_data = normalizer_list_of_lists(RAW_DATA, '-')
    for data in normalize_data:
        print(data)

    table = create_table(
        normalize_data,
        intersection='#',
        horizontal='=',
        vertical=' '
    )
    print('\nДанные в табличном виде:')
    print(*table, sep='\n')


if __name__ == '__main__':
    table_from_data()
