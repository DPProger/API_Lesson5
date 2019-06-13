import requests
from dotenv import load_dotenv
import headhunter
import superjob
import output_table


if __name__ == "__main__":
    load_dotenv()
    languages = {
        'Программист Go': None,
        'Программист C': None,
        'Программист C#': None,
        'Программист Scala': None,
        'Программист C++': None,
        'Программист PHP': None,
        'Программист Ruby': None,
        'Программист Python': None,
        'Программист Java': None,
        'Программист 1С': None
    }

    data_headhunter = {}
    data_superjob = {}
    for language  in languages:
        try:
            language_headhunter = headhunter.get_data_from_headhunter(language)
            data_headhunter.update(language_headhunter)

            language_superjob = superjob.get_data_from_superjob(language)
            data_superjob.update(language_superjob)
        except requests.exceptions.HTTPError as error:
           exit("Can't get data from server:\n{0}".format(error))

    output_table.print_table(data_headhunter, 'Head Hunter Moscow')
    output_table.print_table(data_superjob, 'Superjob Moscow')
