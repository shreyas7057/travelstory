from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Story
from .forms import StoryForm


User = get_user_model()


'''
# all means not of traveler views pages views here
means main(index page), view all the written stories, searching the story and detailed story reading views here
'''
# this will display all the stories that are written by the user
def index(request):
    stories = Story.objects.all()
    context = {
        'stories':stories,
    }
    return render(request,'index.html',context)



# this will show all the stories to the index page 
def all_story(request):
    stories = Story.objects.all()
    context = {
        'stories':stories
    }
    return render(request,'stories/all_story.html',context)


# detail story means it will show all the information once we click on the post/story that we want to read
def detail_story(request,id):
    story = Story.objects.get(id=id)
    context = {
        'story':story,
    }
    return render(request,'stories/detail_story.html',context)




'''
from here views of traveler will start
like there logged dashboard, then writing the story form
then delete there story, then update the story this types of views will be here
'''

# adding new story by the logged in user
@login_required(login_url='login-user')
def create_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST,request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('my_stories')
    else:
        form = StoryForm()
    context = {
        'form':form,
    }
    return render(request,'stories/create_story.html',context=context)


# dashboard of the logged in traveler/user
@login_required(login_url='dashboard')
def traveler_dashboard(request):
    logged_in_user = request.user.id
    # writer = Story.objects.get(traveker__user=logged_in_user)
    stories = Story.objects.filter(user=logged_in_user).count()

    context = {
        'stories':stories,
    }
    return render(request,'stories/traveler_dashboard.html',context)


# my stories it shows all the stories written by the particular logged in user
def my_stories(request):
    logged_in_user = request.user.id
    stories = Story.objects.filter(user = logged_in_user)
    context = {
        'stories':stories,
    }
    return render(request,'stories/my_stories.html',context)


# update story

# delete story

# 