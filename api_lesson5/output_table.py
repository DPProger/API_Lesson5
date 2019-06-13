from terminaltables import AsciiTable


def print_table(language, title):
    headings = [
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]
    table_data = []
    table_data.append(headings)
    for column, row in language.items():
        data = [
            column,
            row['vacancies_found'],
            row['vacancies_processed'],
            row['average_salary']
        ]
        table_data.append(data)
    table = AsciiTable(table_data)
    table.title = title
    print(table.table)
