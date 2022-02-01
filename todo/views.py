from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()

    context = {"todos": todos}

    return render(request, "todo/todo_list.html", context)


def todo_add(request):

    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {"form": form}

    return render(request, "todo/todo_add.html", context)

#içeride olan veriyi istediğimiz verimi degil mi diye eşleştirmek için id kullanıyoruz
#Yani id ye göre veri çektik
def todo_update(request, id):
#todo değişkenine id si benim yazdığım id ile aynı olan varsa databasede onu atadık
    todo = Todo.objects.get(id=id)
#form değişkeninin içini todo ile doldurduk instance kalıp
    form = TodoForm(instance=todo)

    if request.method == "POST":
#request.POSTtan gelen veri ile instance yani databasedeki verimi karşılaştırıyor değişen bir yer varsa
# değiştiriyor tek bir veri haline getiriyor  
        form = TodoForm(request.POST, instance=todo)
#validasyonu yaptık yani fieldlar uygun mu gibi seyler
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {"todo": todo, "form": form}

    return render(request, "todo/todo_update.html", context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        todo.delete()
        return redirect("list")

    context = {"todo": todo}
    return render(request, "todo/todo_delete.html", context)
