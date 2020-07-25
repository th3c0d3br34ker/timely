# Timely

This is a telegram bot which sends you a telegram message about a meeting you have.

It is uses Django as its backend server.

## Why go for a telegram bot?

People might forget to check their mail. But a short simple message reminding them would make more sense.

## Working

### Modules

1.  Backend Server
    This module runs on a server provided by Django. It provides an API response to the front end module. It stores the data of the Meeting.

    Meeting here contains all the relevant information regarding the meeting required. For Example, Start time, Stop time, Organizers, Members and so on.

2.  Frontend Worker
    This module runs as a seperate module. It currently just sends reply to the users. It posts an API request every hour 10 mins before. A list of meetings is then received and then all the members associated are sent a reminder message.
