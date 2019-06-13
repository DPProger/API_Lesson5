import os
import general_methods
import downloads_vacancies


def get_data_from_superjob(language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': os.environ['secret_key'],
        'Content - Type': 'application / x - www - form - urlencoded',
    }

    params = {
        'keyword': language,
        'town': 4,
        'catalogues': 48,
        'page': None,
        'count': 100
    }

    returned_value = 'total'

    language_superjob = {}
    vacancies_found = general_methods.get_count_vacancies(
        language,
        url,
        headers,
        params,
        returned_value
    )

    source = 'superjob'
    field_page_count = 'total'
    field_vacancies = 'objects'

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
    salaryes = get_salary_from_superjob(vacancies)
    average_salary = general_methods.get_average_salary(
        salaryes,
        vacancies_processed
    )

    vacancies = {
        language: {'vacancies_found': vacancies_found,
                   'vacancies_processed': vacancies_processed,
                   'average_salary': average_salary
                  }
    }
    language_superjob.update(vacancies)
    return language_superjob


def get_salary_from_superjob(vacancies):
    sum_salary = 0
    for vacancion in vacancies:
        sum_salary += general_methods.predict_rub_salary(
            vacancion['currency'],
            'rub',
            vacancion['payment_from'],
            vacancion['payment_to']
        )
    return sum_salary
