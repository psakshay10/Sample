from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, UpdateView
# Create your views here.
def home(request):
    #Fetch top 3 posts based number of on views
    # allPosts = Post.objects.all()
    # context = {'allPosts': allPosts}
    return render(request,'home/home.html')


def about(request):
    messages.success(request, 'This is about')
    return render(request,'home/about.html')

def contact(request):
    messages.success(request, 'welcome to contact')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name, email, phone, content)
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request,'home/contact.html')

# def addpost(request):
#     messages.success(request, 'Lets create a new blogpost')
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         author = request.POST['author']
#         slug = request.POST['slug']
#         timestamp = request.POST['timestamp']
#     return render(request,'home/addpost.html')
class AddPostView(CreateView):
    model = Post
    template_name = 'home\Addpost.html'
    fields = '__all__'


    


def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, 'no results for your query! try agian')
    params = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #Cheks for erroneous inputs

        #username must ne under 10 characters
        if len(username) > 10:
            messages.error(request, 'Your username must be under 10 characters')
            return redirect('home')
        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request, 'Your username must be letter and numbers')
            return redirect('home')
        
        #passwords should match
        if pass1 != pass2:
            messages.error(request, 'Your passwors didnt match')
            return redirect('home')
        

            
        #Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'your blog account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('home')


    return HttpResponse('404- Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'You have been sucessfully logged out')
    return redirect('home')