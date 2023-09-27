from django.shortcuts import render

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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def servering_handler(delicion, servings):
    context = {'recipe': dict()}

    if servings is not None:
        for key, value in DATA[delicion].items():
            context['recipe'][key] = round(value * int(servings), 1)
    else:
        context = {'recipe': DATA[delicion]}

    return context

def get_omlet(request):
    servings = request.GET.get('servings')
    context = servering_handler('omlet', servings)

    return render(request, 'calculator/index.html', context)

def get_pasta(request):
    servings = request.GET.get('servings')
    context = servering_handler('pasta', servings)

    return render(request, 'calculator/index.html', context)

def get_buter(request):
    servings = request.GET.get('servings')
    context = servering_handler('buter', servings)

    return render(request, 'calculator/index.html', context)
