import requests


def predict_rub_salary(salary_currency, currency, salary_from, salary_to):

    if salary_currency!=currency:
        return 0
    if salary_from!=None and salary_to != None:
        return (salary_from+salary_to)/2
    if salary_from!=None and salary_to == None:
        return salary_from*1.2
    if salary_from==None and salary_to != None:
        return salary_to*0.8


def get_count_vacancies(language, url, headers, params, returned_value):
    response = requests.get(
        url,
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()[returned_value]


def get_average_salary(sum_salary, count_vacancies):
    try:
        average_salary = int(sum_salary / count_vacancies)
    except ZeroDivisionError as error:
        average_salary = None
    return average_salary
