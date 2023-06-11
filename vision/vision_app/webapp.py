# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.

events = [
    {
        'todo' : 'CI102',
        'date' : '2023-02-14'
    },
        {
        'todo' : 'MATH',
        'date' : '2023-02-15'
    },    {
        'todo' : 'CS420',
        'date' : '2023-02-16'
    },    {
        'todo' : 'Pushing P',
        'date' : '2023-02-17'
    },    {
        'todo' : 'Watch Netflix',
        'date' : '2023-02-18'
    },    {
        'todo' : 'Watch YouTube',
        'date' : '2023-02-19'
    },    {
        'todo' : 'Edit',
        'date' : '2023-02-14'
    },    {
        'todo' : 'Coding',
        'date' : '2023-02-14'
    },  {
        'todo' : 'Sprint Review',
        'date' : '2023-03-10'
    },  {
        'todo' : 'MATH122-QUIZ ',
        'date' : '2023-03-09'
    },
]