<!-- 
Note : If you are reading this README.md file on any editor then I recommend to you to please read it on my github at https://github.com/4NUR46/MLM.git to understand easily.
Because there are soo many things which will make you confuse to understanf it at any editor.
-->

_____________________________________________________________________
_____________________________________________________________________
# <p align="center" > ❤ Multilevel-Marketing ❤ </p>
_____________________________________________________________________
_____________________________________________________________________

Summery : This is an e-commerce web app using django framework of python.
In this there are three types of user.
1. Unregistered users - Who can review only 
2. Registered users - Who can review items, add items into cart check own profile after login.
3. Admin - Who can add new items, edit items dtails, check profile, check who have order which item and delete the item etc.

_____________________________________________________________________

## <p align="center" > ❤ Documentation of using project(Ewebgo) ❤ </p>

#### Project Homepage Link :  <a href='https://ewebgo.herokuapp.com/'> Ewebgo Home </a>
The above link will took you at the homepage of my webapp which is running on heroku.
There you can access all the facilities which can be access by a visitors on the webapp.

#### Register as User page Link :  <a href='https://ewebgo.herokuapp.com/register'> Ewebgo User Register </a>
The above link will redirect to you at the page of registration where you will get a form to fill your info to get register.
Remember register page is only made for register you on the webapp. After registration you have to logged in with your phone number and password.
Because registration page is not made for redirect to you on the homepage by direct login, because of you will be lazy and forget your password.
If you have registered at the webapp then you can abale to add items at the carts and access your user profile etc.

#### Register as Admin page Link :  <a href='https://ewebgo.herokuapp.com/ad_reg'> Ewebgo Admin Register </a>
The above link will redirect to you at the admin registration page. Where you can register to yourself as an admin of this project to get admin access after login.
After registeration you can use that number and password on login page to logged in as an admin.
The login page is same for both user and admin but database are different.
After login as an admin you can use only some admin access like
- Add items in database,
- Update item details,
- Delete/Remove item from database,
- Check the ordered item by the user,
- Check own profile page.
There are many things are remaining to provide for an admin to access and make changes in place of doing it from the django-admin.

Be remember if you are thinking to register as user and admin by using same number and password then you can not access admin pannel.
You will redirect to user page by that credentials if you try to do that because of admin access is only allowed if you are not an user with the same credentials(including password).

#### Project Django-Admin page Link :  <a href='https://ewebgo.herokuapp.com/admin'> Ewebgo Django-admin </a>
This link will open the django-admin page from where you can access all the database and their data if you have a login id and password of superuser.


### Team members:-
- 1. Anurag kushwaha
- 2. Parvej khan
- 3. Santosh yadav
_____________________________________________________________________
_____________________________________________________________________

## <p align="center" > ❤ Documentation for run project(Ewebgo) ❤ </p>

Nevigate the folder of your project.

### Run following commands for installation.

```bash
> git clone https://github.com/4NUR46/Multilevel-Marketing.git
> cd Multilevel-Marketing
> python -m pip install --upgrade pip
> python -m pip install --upgrade virtualenv
> python -m virtualenv venv
```
### If there is any problem of pip not find then use the following command for creating the virtual environment folder.
```bash
> python -m ensurepip
> python -m pip install --upgrade pip
> python -m pip install virtualenv
> python -m virtualenv venv
```
### For activate the virtual environment and install the requirements.
```bash
> cd venv
> Scripts\activate
> cd..
> python -m pip install -r requirements.txt
```
### If want to use updated version of django can use following command oterwise skip it.
```bash
> python -m pip install --upgrade django
```
### Use the following command to run the server.
```bash
> python manage.py runserver
```
### Now open browser and search 
```bash
localhost:8000
```

- If you want to use this project on *PyCharm* IDE then also you have to run above commands on CMD
- But remember to close the server from CMD before starting on PyCharm.
- Then after that you can open the project.
- Remember to set the interpreter of pyCharm before running the server. Otherwise it will not run

### Process to set interpreter on PyCharm
- Go to **`File`** menu and select **`Setting`**. or you can use shortcut  **`Ctrl+Alt+s`**
- Select the **`Project`** option and then  **`Project Interpreter`**
- Now click on setting icon that will be appear on the right-top cornor in the opened window after the location-bar
- NOw click on **`Add Local`**
- Now click on **`Existing Environment`** and click on browse icon that will be after location-bar
- Now go to your project location **`(Example : 'D:project\env')`** and open **`Scripts`** folder(by clicking on arrow showing before name) and click on python.exe to select.
- Now click on **`OK`**
- Again click on **`OK`**
- Now click on **`Apply`**
- Now click on **`OK`**
_____________________________________________________________________

- For accessing admin pannel you can visit on **`localhost:8000\admin`** after running the server.
- username : *`love`*
- password : *`anu`*

The above username and password will works only when you install https://github.com/4NUR46/MLM.git repo on your syste and run.
But this will not works for my webapp project <a href='https://ewebgo.herokuapp.com/'> Ewebgo Home </a> which is running on heroku.
I have made that repository private for personal use and for security purpose of the visitors who have register at my webapp.
The repository of that project is private.

You can create new super user to access admin pannel.
_____________________________________________________________________
### For hack the admin access.
Note : This can be only use when you have full project file in your system.
That is not a hack by the way, that is just a way to create a new super user to gain access of django-admin pannel.
That above method is can be use when you forget you username or password.
This can be only use when you have this full running project code.
- You can create new superuser by using cmd or going through the terminal of pycharm where you have open this project.
- For creating new superuser you can use the following command.
```
python manage.py createsuperuser
```
- Read given instruction prompt on bash\shell after running the above command and act accordingly.
- Remember the password text will not be visible during creating the new superusername.
_____________________________________________________________________

<!--
### Simple Way to fix errors related to database tables or changes.
Warning : This method can be only use when you are just getting errors in developing phase.
In this way you can loose your all registered database tables of your project.
In this just .... will tell after getting 10 stars on my repo.

_____________________________________________________________________
-->

<!---
->J:\Final Project> python -m pip install --upgrade pip
->J:\Final Project> python -m pip install --upgrade virtualenv
->J:\Final Project> python -m virtualenv "Name_of_previous_Environment_folder or Prsee Tab key to auto fill."
->J:\Final Project>cd environment_folder "You can use tab key to auto fill after cd"
->J:\Final Project\mainEnv> python -m pip install --upgrade django    # This is just for trying. This line has no means.
->J:\Final Project> python -m pip install --upgrade pip
->J:\Final Project\mainEnv> cd app_name				#ex. Ewebgo
->J:\Final Project\mainEnv\Ewebgo> python -m pip install --upgrade django
->J:\Final Project\mainEnv\Ewebgo>cd..
->J:\Final Project\mainEnv>Scripts\activate
->(mainEnv) J:\Final Project\mainEnv>cd Ewebgo
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python -m pip install --upgrade django
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python -m pip install --upgrade pillow
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python manage.py runserver

<!---
--->
<!---
Try your common sense to use above command. I already confused by which line I get sucess.
<!--
-->
_____________________________________________________________________

## <p align="center" >❤ To Do ❤</p> 

There are many things left to complete.
- Like Buy item,
- Add a Connect us page,
- Add notifications by admin,
- Get Notifiy about new updated items,
- Give access to the admin for review the user activities,
- Create a database for handling enrollment of course by user,
- Add books and pdfs from admin pannel to access by the user,
- Add slider content or new launched items, course, books from admin pannel to access by the admin,
- Add video lectur Courses from admin pannel to access by the user,
- Enhance Features of video player,
- Adding Screenshorts of program running etc.

Currently I am trying for getting a job because of this I am unable to enhance these things in my projects.</br>
If you want to do any help you are welcome to enhance this project :)</br>
You can help me by connecting with me if you are getting any error or bad response from this project.</br>
I will feel happy to get help from you in my project correction.

_____________________________________________________________________

## <p align="center" > ❤ Contact info ❤ </p> 

You can contact with me if any issue or want help regarding with this repository. 
- Phone number : +917985532371 
- Email id : anurag.cse016@gmail.com
- For Whatsapp : <a href="wa.me/917985532371"> Click here </a>
_____________________________________________________________________
---------------------------------------------------------------------
_____________________________________________________________________

## <p align="center" >❤ Thank You ❤ </p> 

<p align="center">Thanks for reading and visiting on this repository.</br>
Please give a star and support to my project if it is useful.</br>
Giving a star will not took anything from you but it will give a smile to me :)</p>

_____________________________________________________________________
_____________________________________________________________________

## <p align="center" > Developed with ❤ by Anurag Kushwaha </p>
_____________________________________________________________________











<!---
1.Download latest version of python 3.x series.
2.Connect to internet.
3.Extract the package(final project) in a specified drive. e.g: H:\project\Ewebgo\ 
4.Open command prompt and install following packages:-
	* H:\project\Ewebgo\>python -m pip install --upgrade pip
5.After upgrade pip  use following command for run server.
	*H:\project\Ewebgo\env\speedex>python manage.py runserver
6.After run server open browser and write specified url:-
	localhost:8000/
7.Now speedex project will be open and you will be redirect to homepage.
--->
<!---
   			OR
--->
<!---
1.If any error occured during process then:
	*download pycharm (IDE)
	*open file and select the project/Myenv/Ewebgo
	*set virtual enviroment to python in project setting
	*After succesful enviroment set click on terminal and write command :-
		python manage.py runserver
2.After run server open browser and write specified url:-
	localhost:8000/
--->  











<!-- # Multilevel-Marketing
This is an e-commerce web app using python's framework django. In this user can review and buy items and same an admin can add, delete and alter items details etc.
<!--
# Project Link :  <a href='https://ewebgo.herokuapp.com/'> Ewebgo </a>
<!--
# ______ Documentation for run project(Ewebgo) ______
<!--
### Team members:-
- 1. Anurag kushwaha
- 2. Parvej khan
- 3. Santosh yadav
<!--
_____________________________________________________________________
<!--
Nevigate the folder of your project.
Run following commands for installation.
<!--
```bash
> python -m pip install --upgrade pip
> python -m pip install --upgrade virtualenv
> python -m virtualenv myenv
> cd myenv
> git clone https://github.com/4NUR46/Multilevel-Marketing.git
> Scripts\activate
> cd Multilevel-Marketing
> python -m pip install --upgrade django
> python manage.py runserver
```
### Now open browser and search 
```
loaclhost:8000
```
<!--
- If you want to use this project on *PyCharm* IDE then also you have to run above commands on CMD
- But remember to close the server from CMD before starting on PyCharm.
- Then after that you can open the project.
- Remember to set the interpreter of pyCharm before running the server. Otherwise it will not run
<!-- 
### Process to set interpreter on PyCharm
- Go to **`File`** menu and select **`Setting`**. or you can use shortcut  **`Ctrl+Alt+s`**
- Select the **`Project`** option and then  **`Project Interpreter`**
- Now click on setting icon that will be appear on the right-top cornor in the opened window after the location-bar
- NOw click on **`Add Local`**
- Now click on **`Existing Environment`** and click on browse icon that will be after location-bar
- Now go to your project location **`(Example : 'D:project\env')`** and open **`Scripts`** folder(by clicking on arrow showing before name) and click on python.exe to select.
- Now click on **`OK`**
- Again click on **`OK`**
- Now click on **`Apply`**
- Now click on **`OK`**
<!--
_____________________________________________________________________
<!--
- For accessing admin pannel you can visit on **`localhost:8000\admin`** after running the server.
- username : *`love`*
- password : *`anu`*
<!--
The above username and password will works only when you install https://github.com/4NUR46/Multilevel-Marketing.git repo.
This will not works for my deployed project which is running on heroku.

<!--
_____________________________________________________________________
<!--
- You can create new superuser by using cmd or going through that above link.
- For creating new superuser you can use the following command
```
python manage.py createsuperuser
```
--!>
<!--
- Read given instruction prompt on shell/bash after running the above command and act accordingly.
- Remember the password text will not be visible during creating the new superusername
<!--
_____________________________________________________________________




<!---
->J:\Final Project> python -m pip install --upgrade pip
->J:\Final Project> python -m pip install --upgrade virtualenv
->J:\Final Project> python -m virtualenv "Name_of_previous_Environment_folder or Prsee Tab key to auto fill."
->J:\Final Project>cd environment_folder "You can use tab key to auto fill after cd"
->J:\Final Project\mainEnv> python -m pip install --upgrade django    # This is just for trying. This line has no means.
->J:\Final Project> python -m pip install --upgrade pip
->J:\Final Project\mainEnv> cd app_name				#ex. Ewebgo
->J:\Final Project\mainEnv\Ewebgo> python -m pip install --upgrade django
->J:\Final Project\mainEnv\Ewebgo>cd..
->J:\Final Project\mainEnv>Scripts\activate
->(mainEnv) J:\Final Project\mainEnv>cd Ewebgo
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python -m pip install --upgrade django
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python -m pip install --upgrade pillow
->(mainEnv) J:\Final Project\mainEnv\Ewebgo>python manage.py runserver

<!---
--->
<!---
Try your common sense to use above command. I already confused by which line I get sucess.
<!--
-->
<!--
_____________________________________________________________________
<!--
There are many things left to complete. Like Buy item, Get Notifiy, Add video lectur Courses, Enhance Features of video player etc. If you want to do any help you are welcome to enhance this project :)
_____________________________________________________________________
Thanks for visiting on this repository.
Please give a star and support to my project if it is useful.
_____________________________________________________________________
# Contact info
- Phone number : +917985532371 
- Email id : anurag.cse016@gmail.com
- or click on <a href="wa.me/917985532371"> Contact on Whatsapp </a>
<!--
You can contact with me if any issue or want help regarding with this repo.
_____________________________________________________________________
<!--
<p align="center" > Developed with ❤ by Anurag Kushwaha
</p>
<!---
1.Download latest version of python 3.x series.
2.Connect to internet.
3.Extract the package(final project) in a specified drive. e.g: H:\project\Ewebgo\ 
4.Open command prompt and install following packages:-
	* H:\project\Ewebgo\>python -m pip install --upgrade pip
5.After upgrade pip  use following command for run server.
	*H:\project\Ewebgo\env\speedex>python manage.py runserver
6.After run server open browser and write specified url:-
	localhost:8000/
7.Now speedex project will be open and you will be redirect to homepage.
--->
<!---
   			OR
--->
<!---
1.If any error occured during process then:
	*download pycharm (IDE)
	*open file and select the project/Myenv/Ewebgo
	*set virtual enviroment to python in project setting
	*After succesful enviroment set click on terminal and write command :-
		python manage.py runserver
2.After run server open browser and write specified url:-
	localhost:8000/
--->  
