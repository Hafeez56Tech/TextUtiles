
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    SantCase=request.GET.get('SantCase','off')
    Lowcase=request.GET.get('Lowcase','off')
    rnewline=request.GET.get('rnewline','off')
    rlongspace=request.GET.get('rlongspace','off')
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char in punctuations:
                pass
            else:
                analyzed = analyzed + char
        if fullcaps=='on':
            analyzed=analyzed.upper()
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
        elif SantCase=='on':
            analyzed=analyzed.capitalize()
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
        elif Lowcase=='on':
            analyzed=analyzed.lower()
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
        else:
            pass
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps=="on"):
        analyzed=djtext.upper()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (SantCase=="on"):
        analyzed=djtext.capitalize()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (Lowcase=="on"):
        analyzed=djtext.lower()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    
    elif (rnewline=="on"):
        analyzed = ""
        for index in range(len(djtext)):
            if (djtext[index] !='\n' and djtext[index] != '\r'):
                analyzed=analyzed+djtext[index]
            else:
                pass
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (rlongspace=="on"):
        analyzed = ""
        for index in range(len(djtext)):
            if (djtext[index]==" " and djtext[index+1]==" "):
                pass
            else:
                analyzed=analyzed+djtext[index]
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("select at least one of the following")
