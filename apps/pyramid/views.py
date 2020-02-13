from django.shortcuts import render, redirect, HttpResponse

def index(request):

    context = {
        "result": None
    }

    return render(request, 'pyramid/index.html', context)

def input_check(request):

    result = request.POST["input"]
    dict = {}
    
    ##make dictionary object with the characters and the times they appear, change to uppercase
    for char in result:
        if char.upper() in dict:
            dict[char.upper()] = dict[char.upper()]+1
        else:
            dict[char.upper()] = 1
    
    ##find length of the dictionary
    length = len(dict)
    ##trigger for pyramid check
    verdict = True

    ##check to make sure every value between 1 and the length is in the dictionary
    for x in range(1, length+1):
        if x in dict.values():
            continue
        else:
            verdict = False
            break


    ##RESULTS   

    if verdict == True:
        context = {
            "result" : True,
            "dict" : dict
        }
        return render(request, 'pyramid/index.html', context)


    if verdict == False:
        context = {
            "result" : False,
            "dict" : dict
        }
        return render(request, 'pyramid/index.html', context)
