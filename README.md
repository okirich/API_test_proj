# **API_test_proj**
Small API for testing my skills
<!-- First of all, a few words about this tiny project.   -->
For my personal education, I create a simple API for shop catalog.
I used **Django** and **Django REST framework** to create it. It's a little bit messy, but remember, I am just learning :)

Of course, there're dozens of options "how to improve it!" and I'd love to hear it!
***
At this moment realized this endpoints:

1. You can create **address** (may be in the future it will contain some GPS data) with two fields:
   - Street
   - Building

2. You can create **shop** (with all the stuff in it, but now only) with fields:
   - Name
   - Address (*Looking ahead, it's a foreign key for Address table*)
   - "Changed" timestamp

3. You can view and change any **address** and **shop** you created.

## **Dependencies and setups**
***
To start my project on your machine you will need some Python packages, and to be sure we don't break anything let's create virtual environment:

### **1.Python VENV**

I think you have already installed python since you are reading this, so by your leave, I will skip this step and start right away with setting up a virtual environment:

1. Let's create our test environment and activate it.

    \> `python3 -m venv c:\path\to\myenv`
    
    If you're using Windows as I:

    \> `env\Scripts\activate`

    And if you're using UNIX/Linux:

    \$ `. /path/to/myenv/env/activate`


2. After that, we can collect our dependencies, we will use **pip** for it
   (*Sorry, I know I could ship the script with dependencies along with the projects, but I haven't managed to do it yet* ):

    \>>> `pip install django`

    \>>> `pip install django_rest_framework`

### 2. **Cloning the code**

We're almost done! Let's initialize git in **our venv folder**! (*I hope that you already know what it is*)

1. \>`git init`
2. \>`git clone https://github.com/okirich/API_test_proj.git`
   
That's all! You're great! Evrything we need to test on our device!

### 3. **Startup configuration and first run**

Before you can test our project, we should to prepare some configurations.

1. First, we should to setup special enviranmental variable **$MY_DJANGO_KEY** - it's very important varible (*but i have no idea what it do, but of course, i'll found out it!*)
2. If you use UNIX/Linux, you should change **TIME_ZONE** parameter in `API_test_proj/api_proj/settings.py` to your current timezone.If you use Windows, don't even touch it! It doesn't work the proper way :(
3. Set the **DEBUG** flag in `API_test_proj/api_proj/settings.py` to **False**.
4. We need to create *database*:

   \>python3 `manage.py` makemigrations
   
   \>python3 `manage.py` migrate 
5. Type in your console:
   
   \>python3 `manage.py` runserver

## **Let's *taste* it!**
***
Finaly, we can test our API! We have several routes:

- / - root of the API

- /addresses/ - endpoint for inspecting list of addresses

- /shops/ - endpoint for inspecting list of shops

- /addresses/\<int:id> - endpoint for editing existing address

- /shops/\<int:id> - endpoint for editing existing shop

Use your favorite tool, my personal choice is  [HTTpie](https://httpie.io/).

***

If you have any questions or ideas - contact me:

Telegram: https://t.me/cheesus_back

email: kirillgren@gmail.com
