import uuid
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from guestbook.models import Post



def test_view(request, user_id, post_id):
    print user_id, post_id

    return HttpResponse()

def add_view(request):

    print "fsdfsf"

    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        
        post = Post(
            name =name,
            content=content,
        )
        post.save()

        print "Add success!!"

        return HttpResponseRedirect("/")

    return HttpResponse("....")




def index(request):

    #posts = list(Post.objects.all())

    t1 = datetime.now() - timedelta(seconds=100)
    #
    posts = list(Post.objects.filter(date_created__gte=t1)) 

    print("index !!")

    return TemplateResponse(request, "index.html", {
        "name": "ahui",
        "posts": posts,

    })



def login(request):
    print("login!!")
    return HttpResponse('<h1>DDDD</h1>')




"""
public void func1(string name, string content)
{

}

func1("fsfs", "fsdfs")

def func1(**kwargs):
    if kwargs.has_key("name"):
        self.name = name

func1("fsfsf", "dfasdf")
func1(name="a", content="b")
func1(name="a")

"""