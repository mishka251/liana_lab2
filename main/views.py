from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'index.html', {'types': enabled_types})


enabled_types = ['Тонна', 'Килограмм', 'Грамм', 'Милиграмм', 'Фунт']


def calculator(request):
    inputType: str = request.GET.get('inputType')
    outputType: str = request.GET.get('outputType')
    inputValue: str = request.GET.get('inputValue')
    if (inputType is None) or (outputType is None) or (inputValue is None):
        return HttpResponseBadRequest('Not enough params or incorrect names')
    result = convert(inputValue, inputType, outputType)
    if inputType not in enabled_types:
        return HttpResponseBadRequest('InputType is not valid')
    if outputType not in enabled_types:
        return HttpResponseBadRequest('outputType is not valid')
    return JsonResponse({
        'outputValue': result
    })


def convert(inputValue: str, inputType: str, outputType: str) -> float:
    if inputType == outputType:
        return float(inputValue)

    inputKG: float = toKG(inputType, float(inputValue))

    return fromKG(outputType, inputKG)


def toKG(type: str, val: float) -> float:
    if type == 'Тонна':
        return val * 1000
    if type == 'Килограмм':
        return val
    if type == 'Грамм':
        return val / 1000
    if type == 'Милиграмм':
        return val / (1000 * 1000)
    if type == 'Фунт':
        return 0.453592 * val


def fromKG(type: str, val: float) -> float:
    if type == 'Тонна':
        return val / 1000

    if type == 'Килограмм':
        return val

    if type == 'Грамм':
        return val * 1000

    if type == 'Милиграмм':
        return val * (1000 * 1000)

    if type == 'Фунт':
        return val / 0.453592
