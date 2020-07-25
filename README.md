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

## Setup

This tool requires Django for its server and Telegram Bot API from sending messages.

1.  Setup requirements for python (>=3.x) using the requirements.txt. Don't forget to setup a virtual environment first.

```bash
pip install -r requirements.txt
```

2.  Setup you backend server using postgres, add your password to `settings.py`.

3.  Run the django server

    ```shell
    python server/manage.py runserver
    ```

4.  Run the client
    ```shell
    python client/main.py
    ```

```
This is not the perfect version of the idea. It requires a lot of developement.
It is not perfect but its something.
If you have any other idea feel free to contact me. :)
```
