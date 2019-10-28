<h1>Presentation</h1>
<br>
Hey my name's JB, i 25 years old, French, i a young Web developer i just graduate from 2 month. I coding from a little more than one year. Indeed i'm issue from Litterature and Sciences cognitives. <br>

I tested to make programs based on image processing.<br> Because I think it's really cool and funny. I love picture and the pixel's problems aspects ! I just discover IA, so i try to make program with IA (who's a wow tool) couple with image processing. (You can tcheck my captchat resolver or my plate detector with a slider !!!!)
<br><br>

<h1>Projet presentation</h1>
<br>

<h3>Resum of the project</h3>

We want this project to learn by itself to learn to recognize objects without external help. Like a personn goes search on internet informations when she doesn't know something.

<h3>what is this project doing</h3>

In some, we <strong>learn initially</strong> our program some objects and present to it a picture. <em>Here we learn to it a plate and present to it a picture with a plate, two spoons, a fork and a knife.</em>
<br>
It will cut all objects and rewrite it in a new picture. For each pictures we'll <strong>try to detect our objects from our models. </strong><em>Here we try to detect the plate and rewrite all others objects into new picture.</em><br>
After detection of our objects it'll <strong>search category of our detection</strong>, <em>Here it'll search plate on internet and search all other items from the category (washing up) of plate and return items</em>. We <strong>download all of this items and train it.</strong> and remake a detection.

<br><br>


<h1>Problematic</h1>

We know importance of dataset. Imagine a cloud just for IA programs. We know the new dream to archieve an strong IA. The dream to learn itself and solving itself new problem and to writte itself program.
<br><br>

<strong>Our answer:</strong> 

<details>We tried with low result. But it didn't answer to the problematic it just for catching eyes ^^

<br><br>

<h2>This is what we do in real.</h2>
<h3>We try to detect unknow objects from plate by learning from google image.</h3>

![diagramme](https://user-images.githubusercontent.com/54853371/67506530-7e390b00-f68d-11e9-8085-913d96b38d0e.png)

</details>

<br><br>








<strong><h1>STEP ONE</h1></strong>

The first step is for <strong>enter our picture</strong> And from this entrance we <strong>treat picture.</strong> Care it only work with our picture. why? because it's so exausting...
<br>
So we treat the picture. Indeed we:
<br>
- <strong>clean the background</strong> if the background of the picture is different from a white background we replace it by a white background.

- <strong>Separate object in case where there are too many objects</strong> and rewrite them in a new picture.

- <strong>We recuperate positions</strong> of all of the last objects from the inital image for display it at the end.

- Finally <strong>Make a rotation of objects in case where objects are horizontally or leaning</strong>
                                      


<br><br><br><br>



<strong><h1>STEP TWO</h1></strong>

So, we course the picture to search eventually an object from our database. <em>Here we have learn a plate.</em> and try to detect it.


We make a label file who say to us <strong>the name of the model, the name of the object, the label of this object, the name of his part and his dimension</strong>.
<br> 

For example : spoon spoon 1 handle,tank 50x50

Now we can detect objects in memory like that :

<p align="center">
  <img width="400" height="250" src="https://user-images.githubusercontent.com/54853371/67530531-9de92700-f6bf-11e9-9baa-2014c7e99217.jpg">
</p>


<strong>Finally</strong> we can recup the detection and try to make a reconciliation of object liaison from a situation. We serve to a plate in one situation for eat, so we search all others objects who can be use in the situation.


<strong>why did we do a label file ?</strong> We need the dimension for detect an object. For example a plate can be 50 cm width and 50 cm height but a spoon need to have for example 5 cm width and 20 cm height. Moreover, for a next version we can only detect the part of object for example a handle + a tank is a spoon, a handle + tine = fork !!

<br><br><br><br>     











<h1>Step Three</h1>

We have the last detection the plate.

Now we can search on internet, environement of computer, library of computer if we want.

 - Here we search category of the detection, here the plate from google who's give us : "wikipedia category:plate". 

 - After have found the wikipédia page we go on it and recup all href (In our case only the 10 firsts).

 - and continue to filter word to category 
 
 for example:
 
 we <strong>got</strong> plate who's <strong>gave</strong> washing up who's <strong>gave</strong> spoon, fork, food ect...

But food isn't a category of object so we continue to filter word to category and food gave tomato  ect... (i don't know if it doing it but it's "ideal" scrap version)

<br><br>






<h1>Step Fourth</h1>

Now we have our objects from internet and we'll try to make a learning to the program and finally detect our unknows objects. 

We'll download 200 objects of this last search thank to <strong>penseeartificielle/google-image-scrapping</strong>.


<br><br>




<h1>Step Five</h1>

Here we apply fourth or five treatments (five for a next version who's gave part of the objects).
<br><br>

<br><br>
6
<br><br>
7
<br><br>
8
<br><br>
résultats
<br><br>
amélioration
<br><br>
limits
<br><br>
pk ca ne marchera pas sur d'autres images (car je n'ai pas assez de temps blablabla)
<br><br>
