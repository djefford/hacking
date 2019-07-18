import random

messages = ['It is certain',
    'Reply hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'Yes, definitely',
    'It is decidedly so',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) -1)])