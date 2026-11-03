"""Функции генерации таблиц для отображения в терминале."""

DATA = [
    ['Name', 'Status', ''],
    ['Hgftye', 'Jhfewuc', ''],
    ['Hfwqd', 'Hretcv', 'Hfkevrr vrev'],
    ['Kjfhdfbdfb dfbye', 'Nvcbyev', ''],
    ['Ldhfyeg', 'Gf', ''],
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

    # Объединить проверку структуры data и вычисление ширин столбцов
    # для уменьшения количества проходов по данным:
    if not isinstance(data, list) or not data:
        raise ValueError('Данные должны быть в виде заполненного списка.')

    structure = (all(isinstance(row, list) for row in data) and
                 data[0] and
                 all(len(row) == len(data[0]) for row in data) and
                 all(isinstance(cell, str) for row in data for cell in row))

    if not structure:
        raise ValueError(
            'Вложенные списки должны иметь одинаковую ненулевую длину и '
            'содержать строки.'
        )

    if type(indent) is not int or indent < 0:
        raise ValueError('Отступ должен быть целым неотрицательным числом.')

    column_count = len(data[0])
    column_widths = [2 * indent] * column_count

    for row_cells in data:
        for i, cell in enumerate(row_cells):
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
