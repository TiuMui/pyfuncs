"""Функции для работы со списками (list) Python."""

RAW_DATA = [
    ['Name', 'Status', 10],
    ['Hgftye', 'Jhfewuc', '', True],
    ['Hfwqd', False, 'Hfkevrr vrev'],
    ['Kjfhdfbdfb dfbye', 'Nvcbyev', '', '', 5],
    ['11', ],
]


def normalizer_list_of_lists(
        raw_data: list[list],
        empty: str = ''
) -> list[list[str]]:
    """Нормализует список списков в двумерный псевдомассив.

    Принимает список списков с некоторыми данными, строку для
    недостающих элементов.
    Возвращает список списков одинаковой длины, содержащих строки.
    Недостающие элементы внутренних списков по умолчанию делает
    пустыми строками, иначе вставляет значение empty.
    """

    if not isinstance(raw_data, list) or not raw_data:
        raise ValueError('Данные должны быть в виде заполненного списка.')

    structure = all(
        isinstance(sub_list, list) for sub_list in raw_data
    ) and any(raw_data)

    if not structure:
        raise ValueError(
            'Данные должны быть списком списков, хотя бы с одним '
            'не пустым списком.'
        )

    if not isinstance(empty, str):
        raise ValueError(
            'Значение для недостающих элементов должно быть str.'
        )

    max_len_sub_list = max(len(sub_list) for sub_list in raw_data)

    norm_data = [
        [str(cell) for cell in sub_list] +
        [empty] * (max_len_sub_list - len(sub_list))
        for sub_list in raw_data
    ]

    return norm_data


if __name__ == '__main__':
    norm_data = normalizer_list_of_lists(RAW_DATA)
    print(norm_data)
