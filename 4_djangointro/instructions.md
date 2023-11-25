- In this activity we use Django to make a simple website. It will follow a
  similar pattern to Activity 3, except we will be getting to use Django's
  handy features to make the process easier.

- As before, the goal of this activity is further conceptual understanding.
  You probably will not want to use code here as a template for anything you
  will be doing for homework or project work.



Challenge 1
------------

Get the code working!
1. Run "pipenv --python 3"
2. Run "pipenv shell" to enable pipenv
3. Run "pipenv install django" to install Django
4. Run "python manage.py runserver" to run the Django Python server itself

Now, visit localhost:8000 or 127.0.0.1:8000 (both will do the same
thing). You should see a "Page not found" error page.

Can you figure out how to navigate to the "Hello Django World" message?

For the remaining challenges, you will be modifying the manage.py -- but don't
touch the "boilerplate" at the bottom (except for the advanced challenge).


Challenge 2
------------

As mentioned before, in addition to adding a print to every file you are
editing, another good habit to get into when learning a new web framework is
adding a print statement to each "view function".
- Like you did with the previous activity, add a print to the `hello_world`
  "view function", so it says "--- viewing hello world" to the terminal.
- NOTE: Django automatically restarts the server when you save a change.



Challenge 3
------------

- Add a "About me" view, that responds with `<h1>About me!</h1>`

- Hint: You will both need to add a new "path" in the "urlpatterns", and a new
  view function




Challenge 4
------------

As with the previous activity, add a "magic 8 ball" page.

HINT: Here's the view function from the previous activity, how might you modify
it to work with Django?

    def magic_8_ball():
        messages = [
            'You bet',
            'Future looks good',
            'Not likely',
            'Impossible',
        ]
        message = random.choice(messages)
        return '<h1>8 ball says: ' + message + '</h1>'





Challenge 5
------------

Your goal now is to these 3 pages link to each other, much like the solution to
Activity 3. Feel free to put what ever you want on them, the only requirement
is you return HTML code that includes `<a>` links to the different pages.






Bonus Challenge
----------------
Can you incorporate templating to build a guestbook? Here are the steps:

1. Use Django's built-in templating -- this requires adding an additional
setting to the "configure" settings boilerplate. Add the following lines:

    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }],

Then, at the top, import Template and Context:

    from django.template import Template, Context

Django's templating is almost identical to Jinjas (they are essentially 2
"dialects" of the same language).

2. Once again, it's time to replicate the behavior of the previous activity.
This time, in creating a guestbook.

- HINT 1: To access the name from the ?name=XYZ in the URL, use the following
  code:

    name = request.GET['name']

- HINT 2: To use the Django templates, try:

    template = Template('''
        ... Template stuff goes here... eg:
        {{ guestbook }}
    ''')

    context = Context({
        'guestbook': names,
    })

    return HttpResponse(template.render(context))

- HINT 3: Try changing the form to POST to make it so that refreshing the page
  won't accidentally add duplicates. This requires changing the `method` in the
  `<form>` to be POST instead of GET. To check if there is POST data in Django,
  you can use an if statement like the following:

    if 'name' in request.POST:

