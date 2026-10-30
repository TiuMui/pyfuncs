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
        horisontal: str = '-',
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
    # Сделать валидацию data - длины вложенных списков должны быть одинаковы.

    num_column = max(len(row) for row in data)
    max_len_cell = (max(len(cell_text) for row in data for cell_text in row) +
                    2 * indent)

    # Реализовать не одну максимальную ширину ячейки на всю таблицу,
    # а у каждого столбца свою ширину (например, построить список с ширинами
    # столбцов).

    result = []

    top_bottom_line = ((intersection + horisontal * max_len_cell) *
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
