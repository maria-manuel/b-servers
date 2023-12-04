from django.urls import path
from django.http import HttpResponse

import random

# View -- This function, called a "view", is the function that will accept an
# incoming request, and return a response. In this case, it is just sending
# back a message in large fonts, but any logic can go in here to conditionally
# send back any sort of response.
def hello_world(request):
    # <--- HINT: Challenge 2 goes here
    print('viewing hello world')
    return HttpResponse('<h1>Hello Django World!</h1>')

# <--- HINT: One part of Challenge 3 goes here

def about_me(request):
    # <--- HINT: Challenge 2 goes here
    print('viewing about me')
    return HttpResponse('<h1>about me</h1>')

def magic_8_ball(request):
    messages = [
        'You bet',
        'Future looks good', 
        'Not likely',
        'Impossible',
    ]
    message = random.choice(messages)
    return HttpResponse ('<h1>8 ball says: ' + message + '</h1>')


# Routing -- This list is the list of "URL patterns" that Django will try, in
# order, in order to match the incoming request to a function that will handle
# it and return a response.
urlpatterns = [
    # <--- HINT: One part of Challenge 3 goes here
    path('hello-world/', hello_world),
    path('about-me/', about_me),
    path('magic8/', magic_8_ball),
]


# Boilerplate -- Don't worry about understanding anything from here down -- we
# won't be doing stuff this way in the future anyway
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line
    settings.configure(
        DEBUG=True,
        SECRET_KEY='rre1h#l@&z!zcbg',
        ROOT_URLCONF=sys.modules[__name__],
    )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
