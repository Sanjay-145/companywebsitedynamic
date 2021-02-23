# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel="icon" href="{% static 'img/titleicon.png' %}" type="image/x-icon">

</head>

<body>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div>
        <div class="menuitem"><a href="/products">Products</a></div>
        <div class="menuitem"><a>Silicon<br>Corp</a></div>
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact Us</a></div>
    </div>
    <div class="content">
        <div class="container">
            <div class="banner">
                <h1 id="title">Silicon<br>Corp<br>Limited</h1>
            </div>

            {% block content %}
            {% endblock  %}
        </div>
        <div class="footer">
            Copyright © 2020 Silicon Corp Limited, Developed by Sanjay Boven
        </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "companyapp/base.html" %}

{% block content %}
<h2>Our Story</h2>
        
        <p>Silicon Corp Ltd, provides a wide range of semiconductor and infrastructure software applications that serve
            the data center, networking, software, broadband, wireless, and storage and industrial markets. Common
            applications for its products include data center networking, home connectivity, broadband access,
            telecommunucations equipment, smartphones, base stations, data center servers and storage, factory
            automation, power generation and alternative energy systems, displays,and mainframe operations and
            management, and application software development. 
        </p>
     <img class="imgstyle" src="/static/img/office.jpg" alt="home">
     <p> Some of Silicon's core technologies and products include: </p>
    <ul class="margin">
        <li>|     Memory Chips     |</li>
        <li>|     SATA HDD     |</li>
        <li>|    SATA SSD     |</li>
        <li>|     Broadband Modems     |</li>
        <li>|     Wifi Devices      |</li>
        <li>|     Switching Devices      |</li>
        <li>|     Optical Sensors     |</li>
    </ul> 
    
{% endblock  %}
```
### products.html
```
{% extends "companyapp/base.html" %}

{% block content %}
<div class="productcontent">
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for products in productss %}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ products.photo.url }}" alt="product image" height="200" width="200">
            </div>
            <div id="#pn" class="productsname">{{ products.name }}</div>
            <div class="productsprice">{{ products.price }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}
```
### people.html
```
{% extends "companyapp/base.html" %}

{% block content %}
<div class="peoplecontent">
    <h1>Our Crew</h1>
    <div class="crewmembers">
        {% for people in peoples %}
        <div class="crewmember">
            <div class="memberimage">
                <img src="{{ people.photo.url }}" alt="member image" height="200" width="250">
            </div>
            <div class="membername">{{ people.name }}</div>
            <div class="designation">{{ people.designation }}</div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock  %}


{% endblock  %}
```
### contactus.html
```
{% extends "companyapp/base.html" %}

{% block content %}
<form action="//submit.form" id="ContactUs100" method="post" onsubmit="return ValidateForm(this);">
<script type="text/javascript">
function ValidateForm(frm) {
if (frm.Name.value == "") { alert('Name is required.'); frm.Name.focus(); return false; }
if (frm.FromEmailAddress.value == "") { alert('Email address is required.'); frm.FromEmailAddress.focus(); return false; }
if (frm.FromEmailAddress.value.indexOf("@") < 1 || frm.FromEmailAddress.value.indexOf(".") < 1) { alert('Please enter a valid email address.'); frm.FromEmailAddress.focus(); return false; }
if (frm.Comments.value == "") { alert('Please enter comments or questions.'); frm.Comments.focus(); return false; }
return true; }
</script>
<table style="width:100%;max-width:550px;border:0;" cellpadding="8" cellspacing="0">
<tr> <td>
<label for="Name">Name*:</label>
</td> <td>
<input name="Name" type="text" maxlength="60" style="width:100%;max-width:250px;" />
</td> </tr> <tr> <td>
<label for="PhoneNumber">Phone number:</label>
</td> <td>
<input name="PhoneNumber" type="text" maxlength="43" style="width:100%;max-width:250px;" />
</td> </tr> <tr> <td>
<label for="FromEmailAddress">Email address*:</label>
</td> <td>
<input name="FromEmailAddress" type="text" maxlength="90" style="width:100%;max-width:250px;" />
</td> </tr> <tr> <td>
<label for="Comments">Comments*:</label>
</td> <td>
<textarea name="Comments" rows="7" cols="40" style="width:100%;max-width:350px;"></textarea>
</td> </tr> <tr> <td>
* - required fields
</td> <td>
<input name="skip_Submit" type="submit" value="Submit" />
</td> </tr>
</table>
</form>
{% endblock  %}
```
## OUTPUT:
![output](./static/img/home.png)

![output](./static/img/products.png)

![output](./static/img/people.png)

![output](./static/img/contactus.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://sanjay.student.saveetha.in:8000/home. HTML code is validated.