"""Функции генерации таблиц для отображения в терминале."""

DATA = [
    ['Name', 'Status', ''],
    ['Hgftye', 'Jhfewuc', ''],
    ['Hfwqd', 'Hretcv', 'Hfkevrr vrev'],
    ['Kjfhdfbdfb dfbye', 'Nvcbyev', ''],
    ['Ldhfyeg', 'Gf', '']
]


def create_table(
        data: list[list[str]],
        intersection: str = '+',
        horizontal: str = '-',
        vertical: str = '|',
        indent: int = 1
) -> list[str]:
    """Строит таблицу для входного двумерного массива данных data.

    Принимает список списков с данными, графические элементы таблицы
    и отступы внутри ячеек для текста.
    Помещает данные в таблицу по схеме:
        список списков - строки таблицы;
        элементы списков - столбцы таблицы.
    Возвращает список готовых для вывода строк с графическими
    элементами таблицы.
    """

    if not isinstance(data, list) or not data:
        raise ValueError('Данные должны быть в виде заполненного списка.')

    if type(indent) is not int or indent < 0:
        raise ValueError('Отступ должен быть целым неотрицательным числом.')

    column_count = len(data[0])
    column_widths = [2 * indent] * column_count
    len_sub_list = None

    for step, row_cells in enumerate(data):
        if not isinstance(row_cells, list):
            raise ValueError('Входные данные должны быть списком списков.')
        if not row_cells:
            raise ValueError('Ни один вложенный список не должен быть пустым.')

        prew_len_sub_list = len_sub_list
        len_sub_list = len(row_cells)
        if step > 0 and len_sub_list != prew_len_sub_list:
            raise ValueError('Вложенные списки должны иметь одинаковую длину.')

        for i, cell in enumerate(row_cells):
            if not isinstance(cell, str):
                raise ValueError(
                    'Вложенные списки должны содержать только строки.'
                )
            if column_widths[i] < (cell_width := len(cell) + 2 * indent):
                column_widths[i] = cell_width

    line_gen = (intersection + horizontal * width for width in column_widths)
    top_bottom_line = ''.join(line_gen) + intersection

    result = [top_bottom_line]

    for row_cells in data:
        cells_gen = (vertical + cell.center(column_widths[i])
                     for i, cell in enumerate(row_cells))
        row_str = ''.join(cells_gen) + vertical
        result.extend([row_str, top_bottom_line])

    return result


if __name__ == '__main__':
    table_data = create_table(DATA)
    print(*table_data, sep='\n')
