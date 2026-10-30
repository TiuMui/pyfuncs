"""Функции генерации таблиц для отображения в терминале."""

DATA = [
    ['Name', 'Status', 'Description'],
    ['Hgftye', 'Jhfewuc', 'Kjfhebc'],
    ['Hfwqd', 'Hretcv', 'Ytercbs'],
    ['Kjfhye', 'Nvcbyev', 'Rsddvcg dtwtfad'],
    ['Ldhfyeg', 'Gf', 'Trea'],
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

    num_column = len(data[0])
    max_len_cell = (max(len(cell_text) for row in data for cell_text in row) +
                    2 * indent)

    # Реализовать не одну максимальную ширину ячейки на всю таблицу,
    # а у каждого столбца свою ширину (например, построить список с ширинами
    # столбцов).

    result = []

    top_bottom_line = ((intersection + horizontal * max_len_cell) *
                       num_column + intersection)
    result.append(top_bottom_line)

    for row_cells in data:
        row_str = ''
        for cell in row_cells:
            row_str += vertical + cell.center(max_len_cell)
        row_str += vertical
        result.extend([row_str, top_bottom_line])

    return result


if __name__ == '__main__':
    table_data = create_table(DATA)
    print(*table_data, sep='\n')
