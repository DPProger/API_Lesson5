import general_methods
import downloads_vacancies


def get_data_from_headhunter(language):

    url = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': language,
              'area': 1,
              'period': 30,
              'only_with_salary': True,
              'per_page': None,
              'page': None
              }
    returned_value = 'found'

    language_headhunter = {}
    vacancies_found = general_methods.get_count_vacancies(
        language,
        url,
        headers,
        params,
        returned_value
    )

    source = 'headhunter'
    field_page_count = 'pages'
    field_vacancies = 'items'

    vacancies = downloads_vacancies.fetch_vacancies(
        language,
        url,
        headers,
        params,
        source,
        field_page_count,
        field_vacancies
    )

    vacancies_processed = len(vacancies)
    salaryes = get_salary_from_headhunter(vacancies)
    average_salary = general_methods.get_average_salary(
        salaryes,
        vacancies_processed
    )

    vacancies = {
        language: {'vacancies_found': vacancies_found,
                   'vacancies_processed': vacancies_processed,
                   'average_salary': average_salary}
    }
    language_headhunter.update(vacancies)
    return language_headhunter


def get_salary_from_headhunter(vacancies):
    sum_salary = 0
    for vacancion in vacancies:
        sum_salary += general_methods.predict_rub_salary(
            vacancion['salary']['currency'],
            'RUR',
            vacancion['salary']['from'],
            vacancion['salary']['to']
        )
    return sum_salary
