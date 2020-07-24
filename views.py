from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

    def result(request):
    
    computer = random.randint(1,3)
    print("\n1.주먹 2.가위 3. 보")
    print("1-3 Number input?")
    text = request.GET['fulltext']
    text = int(text)
    return render(request, 'result.html', {'full': text, 'computer' : computer})