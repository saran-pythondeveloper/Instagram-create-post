from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import User
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# SIGNUPFORM
def signupPage(request):

    context={
        "error": ""
    }

    if request.method == "POST":
        user_check = User.objects.filter(username= request.POST['username'])
        if len(user_check) > 0:
            context={
                "error": "username already exist!"
            }
            return render(request, 'signup.html',context)
        else:
            new_user = User(username = request.POST['username'],email = request.POST['email'])
            # pwd____
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('loginPage')

    return render(request, 'signup.html',context)

# LOGINFIRM
def loginPage(request):
    context={
        "error": ""
    }
    if request.method == "POST":
        User= authenticate(username=request.POST['username'] ,password=request.POST['password'])
        
        if User is not None:
            login(request,User)
            return redirect('homePage')
        else:
           context={
              "error":"*Invalid username or password!"
           }
           return render(request,'login.html',context)


    return render(request,'login.html', context) 


# HOMEPAGE
@login_required
def homePage(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html',{'posts': posts})

#LOGOUT
def logoutUser(request): 
    
    logout(request)
    return redirect('/')

# View for creating a new post
@login_required
def createPostPage(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been created!")
            return redirect('homePage')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# View for liking a post
@login_required
def likePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        messages.warning(request, "You have already liked this post.")
    else:
        messages.success(request, "You liked the post.")
    
    return redirect('homePage')

# View for commenting on a post
@login_required
def commentPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('homePage')
    else:
        form = CommentForm()
    
    return render(request, 'comment_post.html', {'form': form, 'post': post})
    
    
 
