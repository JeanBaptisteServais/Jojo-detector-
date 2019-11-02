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

Now we can detect objects in memory like that :<br><br>

<p align="center">
  <img width="400" height="250" src="https://user-images.githubusercontent.com/54853371/67530531-9de92700-f6bf-11e9-9baa-2014c7e99217.jpg">
</p>


<strong>Finally</strong> we can recup the detection and try to make a reconciliation of object liaison from a situation. We serve to a plate in one situation for eat, so we search all others objects who can be use in the situation.


<strong>why did we do a label file ?</strong> We need the dimension for detect an object. For example a plate can be 50 cm width and 50 cm height but a spoon need to have for example 5 cm width and 20 cm height. Moreover, for a next version we can only detect the part of object for example a handle + a tank is a spoon, a handle + tine = fork !!

<br><br>   





<h1>STEP THREE PART 1</h1>

<h2>scrap</h2>

We have the last detection the plate.

Now we can search on internet, environement of computer, library of computer if we want.

 - Here we search category of the detection, here the plate from google who's give us : "wikipedia category:plate". 

 - After have found the wikipédia page we go on it and recup all href (In our case only the 10 firsts).

 - and continue to filter word to category 
 
 for example:
 
 we <strong>got</strong> plate who's <strong>gave</strong> washing up who's <strong>gave</strong> spoon, fork, food ect...

But food isn't a category of object so we continue to filter word to category and food gave tomato  ect... (i don't know if it doing it but it's "ideal" scrap version)

<br><br>



<h1>STEP THREE PART 2</h1>

<h2>Download</h2>

Now we have our objects from internet and we'll try to make a learning to the program and finally detect our unknows objects. 

We'll download 200 objects of this last search, we use <strong>penseeartificielle/google-image-scrapping</strong> script. 
This script allows to download x images from ènieme to x on google image !!!

<br><br>













<h1>STEP FOURTH</h1>

Here we apply fourth or five treatments (five for a next version who's gave part of the objects).

<h2>First treatment</h2>

<h3>Background</h3>

<br>
So we treat the picture, we clean the background (if the background isn't white). From that we trying to take contours (except the smaller contour who's represent noise, pixels that we do not want. We ignore too the highter who's represent the border of the frame), so we try to take objects in the picture. And to copy them in a new white picture. We have a white in most of the cases, background !

<br><br>
<strong>For example:</strong>
<br><br>
<p align="center">
  <img width="460" height="250" src="https://user-images.githubusercontent.com/54853371/67151961-803a4d00-f2ce-11e9-8b6c-12888f8b0f5c.png">
</p>


Here we dont want the accuraccy, we just want the form for the next steps. For apply a threshold
filter who's bynarize the picture, who's make the picture in black and white and give us the form of the object
(here the spoon'll only white and the background only black). If you want you can check car detection who's use maybe an ok remove background for cars !

<p align="left">
<img width="200" height="200" src="https://user-images.githubusercontent.com/54853371/67644702-2bc54c00-f924-11e9-81de-ca7e3b34e6ea.png"> <em>Here it's the best case we can have. Sometime the treatment destroy the picture... </em>
</p>
<br><br>





<h2>Second treatment</h2>

<h3>Multiple objects</h3>

We recover and separate objects from each other in a scene like:

1) - Here we have many knife, again we found contours by a thresholding to thresh: 250 and max value: 255, if the pixel value is less 250 this pixel is black or 0 else the pixel is define to white or 255. 

2) - Next, we course the black and white picture and recup all contours (when we speak about contours we speak about the border of the object) 


3) - and course them one by one, if the first contour is white, superpose this to the orignal picture and make all the rest in white. 

4) - And we can have only have a knife. We repeat the operation for all objects <em>here 4 times for 4 knifes !</em>

5) - Before training we detect objects, includes them into a rectangle who's gave us (x, y) and (width, height) coordiantes; then we take the object without the rest of the picture.

<br><br>

<p>


<img width="250" height="150" align="left" src="https://user-images.githubusercontent.com/54853371/67782765-8ae0a900-fa69-11e9-9c87-12c8ec772e18.png">


<img width="130" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784042-743b5180-fa6b-11e9-8a8f-05865c2e3dce.png">

<img width="130" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67783588-c4fe7a80-fa6a-11e9-9f45-b5edc42d508c.png">


<img width="150" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784689-6d610e80-fa6c-11e9-98b6-75ef626dac9f.png">

<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784688-6cc87800-fa6c-11e9-8777-6e42c9bb3ad6.png">

</p>


<br><br>




<h2>Third treatment</h2>

<h3>positioning</h3>

here we rotate the image to put the object in a desired direction with soh cah toa Thank to <strong>Simon Belleguy</strong> who's help me a lot for mathematic formula !

We need to positionnate our object because our model (i think) because it isn't robust to rotation of picture. In some if the object's horizontally or leanning it could doesn't pass to the detection.

<p align="center">
<strong>Horizontally &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; leaning &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; normal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; leaning</strong>
</p>


<p align="center">
<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67785659-df862300-fa6d-11e9-99a5-5a2aeb032263.jpg">



<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67785661-e01eb980-fa6d-11e9-8751-45ce919013b8.jpg">



<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67785663-e01eb980-fa6d-11e9-86bd-b07210d0f455.jpg">



<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67785664-e01eb980-fa6d-11e9-9586-e1d6af132daf.jpg">

</p>


So we want only a normal object in our dataset.

- We define 4 categories because rotation isn't the same by inclinaison:
 
  - 1) top bot (top up, bot down)
  
  - 2) bot top (top down, bot up)
  
  - 3) horinzontal leaning
  
  - 4) normal



For that we take the max point, the head and the footer of the current object like that:

<p align="center">
<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67785661-e01eb980-fa6d-11e9-8751-45ce919013b8.jpg">

<img width="150" height="200" align="center" src="https://user-images.githubusercontent.com/54853371/67786734-acdd2a00-fa6f-11e9-969f-030dae907d3a.png">

<img width="150" height="200" align="center" src="https://user-images.githubusercontent.com/54853371/67786893-ed3ca800-fa6f-11e9-8d89-0efe87af1f3c.png">


</p>






After have define this:


- We calculate the arctangeante because we have opposite and adjacent side.

- We rotate it to 45 - current degrees (x1; y1) - current degrees (x2; y2) 

- We re took current position of head and footer

- calculate distance on y axis on the two (we want |y1 - y2| < 10)

- We try a direction if |y1 - y2| increment from the last point we tried the opposite direction

- It make me so proud !




  
![cc-ConvertImage](https://user-images.githubusercontent.com/54853371/67152972-5a6a7380-f2e1-11e9-96ec-17d701f1d5d4.png)

<p align="center">
 
 <img  align="center" src="https://user-images.githubusercontent.com/54853371/67152957-f182fb80-f2e0-11e9-8a12-cd832d0d4ce7.png">
 

</p>


<br><br>












<h2>Third treatment</h2>

<h3>Find part</h3>


<h2>Fourth treatment</h2>

<h3>delete</h3>

Here we delete data destroy by last operations (background who break some picture or didn't worked)...

Indeed we removing small and big contours 1400 < contour > 11000




<h1>Step Five</h1>

<h2>Find dimensions</h2>

Here we don't know how many objects we have download. So we make a file who's writting an other file. We course all the objects from our dataset object by object. We recup the head and footer, the right and the left of the object.

After have do that we convert pixel to cm.

For do that we lunch a thread.

These dimensions are important for the training and the detections.

<h1>Step Six</h1>

We training each objects. Negativ are all other objects downloaded.

<h1>Step Seven</h1>

Is the second step


<h1>Step Height</h1>

<h1>Results:</h1>

Are not good we only can detect spoon, fork are detected in on fork and spoon and knife isn't detected  

<br><br>

<p align="center">
<img src="https://user-images.githubusercontent.com/54853371/68077799-8817e800-fdca-11e9-9604-dbf41f862d72.jpg"
</p>

where fork = fourchette<br>
spoon = cuillère<br>
plate = assiette<br>
knife = oh didn't found...
