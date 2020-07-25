----------------------------------------------------------------------------------
                    Application
----------------------------------------------------------------------------------

This application was devloped as part of coding learning with Open Classroom.  
The application install tables, insert data and allow interraction with its. 

Data are collect from Open Food Facts API :
https://documenter.getpostman.com/view/8470508/SVtN3Wzy

In fact the programme allow user to find a product and propose a substitute for it. 

----------------------------------------------------------------------------------
                    Installation
----------------------------------------------------------------------------------

The application works with SQL database : https://dev.mysql.com

First you need to create a database :

    "CREATE DATABASE nom_db CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';"

Fill the 'config.py' file with a user, a password which have 
access to your database. Fill also a database name used.

Set up by default :

    name = 'root'
    password = ''
    database = 'p5'

!!! Don't forget the quotes !!!

You can optionally set up the number of data collect by the api request and 
the location.

Second you need to install the virtual environment :

    "pipenv install"

Then launch the virtual environment :

    "pipenv shell"

----------------------------------------------------------------------------------
                    Usage
----------------------------------------------------------------------------------

Launch the application with :

    "python run.py"

User can interract with the programme by number input.
Options are describe in the terminal.

First user have to install the tables and data by input '1' corresponding to 
'Installer le programme'.