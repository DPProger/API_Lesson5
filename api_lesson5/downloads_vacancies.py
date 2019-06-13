import requests


def fetch_vacancies(language, url, headers, params, source, field_page_count, field_vacancies):
    response = requests.get(
        url,
        headers=headers,
        params=params
    )
    response.raise_for_status()

    page_count = response.json()[field_page_count]
    vacancies = []
    for page in range(page_count):
        params_page = {}
        if (source=='superjob'):
            params_page = {
                'text': language,
                'town': 4,
                'catalogues': 48,
                'page': page,
                'count': 100
            }
        if (source=='headhunter'):
            params_page = {
                'text': language,
                'area': 1,
                'period': 30,
                'only_with_salary': True,
                'per_page': page,
                'page': page
            }

        response = requests.get(
            url,
            headers=headers,
            params=params_page
        )
        response.raise_for_status()
        for vacancy in response.json()[field_vacancies]:
            vacancies.append(vacancy)
    return vacancies
