# Для подсчета баллов, набранных студентами группы надо обработать информацию, представленную в виде взаимосвязанных структур данных:
# group - список словарей, где словарь описывает информацию о студенте.
#     hw_results: список с информацией о решенных д/з.
# Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных д/з.
#     test1_results: список с информацией о решенном Test1.
# Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных заданий
#     test1_costs: словарь с весами заданий Test1.
# Ключ - номер задачи, значение - вес задачи (кол-во баллов, которое начисляется за ее решение).
#
# Между этими данными связь устанавливается с помощью ключа студента.
# Например, студенту с id=1024, соответствуют домашние задания и задачи из Test1, у которых ключу “id” соответствует значение 1024 .
# Связь между весом задачи Test1 и ее номером устанавливается по ключу в словаре test1_weights.
#
# Необходимо написать 2 функции:
#     update_students_results: обновляет рейтинг студента, на основании предоставленной информации. См. описание ф-ции.
#     print_students_info: распечатывает информацию о студенте, сортируя по указанному ключу из словаря студента.
# По умолчанию сортировка по ключу ‘fullname’.

group = [
    {"id": 1024, "fullname": "Александр Скворцов",    "email": "", "github": "https://github.com/Agskvortsov", "rank": 0},
    {"id": 1025, "fullname": "Андрей Рожко",          "email": "", "github": "https://github.com/rozhkoandrew", "rank": 0},
    {"id": 1026, "fullname": "Кулишенко Алексей",     "email": "", "github": "https://github.com/", "rank": 0},
    {"id": 1027, "fullname": "Виталий Рыжков",        "email": "", "github": "https://github.com/vitalyryzhkov", "rank": 0},
    {"id": 1028, "fullname": "Гавеля Виталина",       "email": "", "github": "https://github.com/", "rank": 0},
    {"id": 1029, "fullname": "Виктор Бурлаков",       "email": "", "github": "https://github.com/SancheeZzz", "rank": 0},
    {"id": 1030, "fullname": "Виктор Горовой",        "email": "", "github": "https://github.com/lamboosanproject", "rank": 0},
    {"id": 1031, "fullname": "Надежда Симанович",     "email": "", "github": "https://github.com/simanadya", "rank": 0},
    {"id": 1032, "fullname": "Николай Марушевский",   "email": "", "github": "https://github.com/Gelios-Sky", "rank": 0},
    {"id": 1033, "fullname": "Андрей Кравчук",        "email": "", "github": "https://github.com/albaderon", "rank": 0},
    {"id": 1034, "fullname": "Шадрина Екатерина",     "email": "", "github": "https://github.com/katefeline", "rank": 0},
    {"id": 1035, "fullname": "Александр Малышев",     "email": "", "github": "https://github.com/Barabasha", "rank": 0},
    {"id": 1036, "fullname": "Владимир Веренчук",     "email": "", "github": "https://github.com/", "rank": 0}
]

hw_results = [
    {"id": 1024, "task_completion": [1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1025, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0] },
    {"id": 1026, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1027, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1028, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1029, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1031, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1032, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1034, "task_completion": [1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1036, "task_completion": [1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] }
]


test1_results = [
    {"id": 1024, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1025, "task_completion": [1,1,1,1,1,1,1,1,1,0,0,1] },
    {"id": 1026, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1027, "task_completion": [1,1,1,1,1,1,1,1,0,0,0,0] },
    {"id": 1028, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1029, "task_completion": [1,1,1,1,1,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [1,1,1,1,1,1,1,1,0,0,0,0] },
    {"id": 1031, "task_completion": [1,1,1,1,0,0,0,0,0,0,0,0] },
    {"id": 1032, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,1,1,1,0,0,1] },
    {"id": 1034, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [1,1,1,1,1,1,1,1,1,0,1,1] },
    {"id": 1036, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] }
]

test1_weights = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 2,
    6 : 2,
    7 : 4,
    8 : 4,
    9 : 4,
    10 : 8,
    11 : 8,
    12 : 15
}


def update_students_results(group):
    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    hw_rank = []
    test1_rank = []
    num_students = len(hw_results)
    num_test = len(test1_weights)

    for student in hw_results:
        hw_rank.append(sum(student["task_completion"]))

    for student in test1_results:
        test_result = []
        for i in range(num_test):
            test_result.append(student["task_completion"][i] * test1_weights[i + 1])
        test1_rank.append(sum(test_result))

    for student in range(num_students):
        rank = hw_rank[student] + test1_rank[student]
        group[student]["rank"] = rank


def print_students_info(group, sort_by_key="fullname"):
    # Prints students info sorted according to the passed key in dictionary). By default, sort by students names.
    # Student info should be presented as a card that includes the following information:
    #     - id,
    #     - name,
    #     - email,
    #     - githu11j;.j\un7b account (only name, not URL path)
    #     }Ujk,
    #     - rank1
    # Example (format is not strictly required):
    #     -----------------------------------------
    #     : ID:                               1025:
    #     :.......................................:
    #     : Full name:          Александр Скворцов:
    #     : Email:           agskvortsov@gmail.com:
    #     : Github:                    Agskvortsov:
    #     : Rank:                               42:
    #     -----------------------------------------
    # :return: None

    for student in sorted(group, key=lambda student: student.get(sort_by_key)):
        print(35*'-')
        print(": ID:        %20s :" %student["id"])
        print(':'+33*'.'+':')
        print(": Full name: %20s :" % student["fullname"])
        print(": Email:     %20s :" % student["email"])
        print(": Github:    %20s :" % student["github"][student["github"].rindex('/')+1:])
        print(": Rank:      %20s :" % student["rank"])
        print(35 * '-')

if __name__ == "__main__":
    update_students_results(group)
    print_students_info(group, "rank")
