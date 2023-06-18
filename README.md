# Final Project

#### 📘 Final Project from Edx | Harvard CS50's Web Programming with Python and JavaScript Course

✒️ Designing and implementing a web application of your own with Python and JavaScript.

### Specification

🚀 https://cs50.harvard.edu/web/2020/projects/final/capstone/

### Video

🚀 [Capstone project on YouTube](https://youtu.be/v4welsQW_2Q)

### Requirements

* Python 3.11.1
* Django 4.1.4
* django-bootstrap-modal-forms 2.2.0 
* django-widget-tweaks 1.4.12

### How to run? 
1. Go to the directory which contains "__manage.py__" file. 
2. Then type this command: __python manage.py runserver__
3. In your Web browser use a URL: __http://127.0.0.1:8000/__

### Description

👉 __EPortfolio__ is a responsive, dynamic and most advanced web application that summarizes all my __CS50's Web Programming with Python and JavaScript__ projects in one place. 
My application uses the Django plugin to create AJAX-based forms in Bootstrap mode (__django-bootstrap-modal-forms__).
This application cost me the most work and was the most difficult to do. Anyone can see information about me, the course, and all my course projects. 
After registering and logging in, you can additionally create, edit or delete projects. The __EPortfolio__ application allows you to see the requirements of individual projects and watch a YouTube video showing them in action.

👉 My application uses new elements like as:
* __modal forms__ that use AJAX-based in Bootstrap mode,
* fonts from Google [__Nunito__](https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800) (online),
* icons for Designers and Developers [__Lineicons 2.0__](https://lineicons.com/) (offline),
* [__Bootstrap 5.0.5-alpha__](https://blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/) (offline),
* __active menu__, __close navbar-collapse when a clicked__, __get the navbar for menu scroll__, __back to Top button__ which is controlled by the Java Script (index.js file),
* __animations__ on the sections and pages such as alerts, buttons, avatar etc and __background gradients__ (style.css file),
* the main element **Accordion** (a Bootstrap component), which contains all information about my projects.

👉 The **ePortfolio** application includes mainly:
* __static__ folders with fonts, icons, images, css and js files, 
* __templates__ folder with 9 .html files,
* __compatibility.py__ file with that display the login form and handle the login action,
* __forms.py__ files with definitions of modal forms such as registration, login etc,
* __models.py__ file with the definition of model __Projects__,
* __urls.py__ file with define URLs for the views,
* __views.py__ with **C R U D** operations, which I based on __generic classes__ instead of functions as in earlier projects.  

❤️ __I believe that my final project meets the requirements and is different from the previous ones.
It is also the most complex and uses many new elements. This project developed me.__ ❤️
