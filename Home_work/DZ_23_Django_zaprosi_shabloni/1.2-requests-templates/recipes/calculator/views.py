from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}



def get_dish(request):
    return render(request, 'calculator/index.html')

def get_count(request, dish):
    return render(request, 'calculator/count.html')

def get_indigrients(request, dish, count):
    result = DATA.get(dish)
    lst = [i * count for i in result.values()]
    ready_dict = dict(zip(result.keys(), lst))
    # context = ready_dict
    # return HttpResponse(context)
    context = {
        'recipe': ready_dict
        }
    return render(request, 'calculator/indigrients.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
