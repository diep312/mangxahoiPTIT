from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, User, UserAdditionalInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import PostForm, CreateUserForm, UpdateUserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Hàm view cho trang web
@csrf_protect
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower() 
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Mật khẩu hoặc tài khoản không đúng. Hãy thử lại')
        except:
            messages.error(request, 'Người dùng không tồn tại')


    context = {'page': page}
    return render(request, 'base/loginandregister.html', context)
             
@login_required(login_url='login')  
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST': 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            UserAdditionalInfo.objects.create(
                user = user
            )
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Đã có lỗi xảy ra trong quá trình đăng ký...')

    return render(request, 'base/loginandregister.html', {'form': form})

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all().order_by('-created_on')
    user = User.objects.all().order_by('?')[:3]
    page = 'not-edit'
    context = {
        'post_list': posts,
        'page': page,
        'user_info': user,
    }
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def postPost(request):
    posts = Post.objects.all().order_by('-created_on')
    page = 'post'
    form = PostForm()
    
    context ={
        'page': page,
        'form': form,
        'post_list': posts
    }
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')
        else:
            messages.error(request, 'Đã có lỗi xảy ra...')
        
    return render(request, 'base/home.html', context)
        

@login_required(login_url='login')
def friendspage(request, pk):
    user = User.objects.get(id=pk)
    user_info = UserAdditionalInfo.objects.get(user_id=pk)
    posts = Post.objects.filter(author=pk)
    page = 'see-profile'
    context = {
        'user': user,
        'user_info': user_info,
        'post_list': posts,
        'page': page,
    }
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def editprofile(request, pk):
    cur_user = User.objects.get(id=pk)
    user_info = UserAdditionalInfo.objects.get(user_id=pk)
    page = 'edit'
    form = UpdateUserForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            newinfo = form.save(commit=False)
            newinfo.user = cur_user
            if(newinfo.bg == None):
                newinfo.bg = "https://t3.ftcdn.net/jpg/04/53/92/04/360_F_453920448_yMcff4E8ctdXQQegdaQ7WcXnHM3y3aMM.jpg"
            if(newinfo.avt == None):
                newinfo.avt = "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png"
            newinfo.save()
            messages.success(request, 'Cập nhật thành công')
            return redirect('home')

    context ={
        'user': cur_user,
        'user_info': user_info,
        'page': page,
        'form': form
    }
    
    return render(request, 'base/profile.html', context)
    

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'comments': comments
        }
        return render(request, 'base/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST':
            post = Post.objects.get(pk=pk)
            new_comment = Comment.objects.create(
                post=post,
                author=request.user,
                comment=request.POST.get('comment')
            )

            comments = Comment.objects.filter(post=post).order_by('-created_on')

            context = {
                'post': post,
                'comments': comments,
            }
            return render(request, 'base/post_detail.html', context)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body', 'img']
    template_name = 'base/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'base/post_delete.html'
    success_url = reverse_lazy('home')
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'base/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        
        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        
        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)