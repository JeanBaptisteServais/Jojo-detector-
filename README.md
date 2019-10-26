# work-on-picture (in finish)


I had a lot of fun, most of the time! to work on the image for have the best dataset ever ! possible (<em>it doesn't work, blam the dataset</em>).


this program is intelligent because it learns by itself and writes itself (to make eye-catching) or this program downloads images on the internet and makes comparaisons..



<h4>Maybe it work only on the current type of picture bacause we need to : </h4> <br> 

for the v2 we want detect part of objects, compare it ect but not now so boring boring for now increase the scrap and make loop turns, increase the speed, in any situation detect objects and not that in this scene, do not have a starting object, make a smart system that does not detect a plate on a football field (stop put me keeper ...) because it only work maybe for this type of picture. improve the rewrite system and put more


![diagramme](https://user-images.githubusercontent.com/54853371/67506530-7e390b00-f68d-11e9-8085-913d96b38d0e.png)











<strong><h1>STEP ONE</h1></strong>

<h4>We enter a picture. Then we treat it. Delete background if the background isn't white. Next we separate all object in a new picture. Finally we make a rotation if the objects is'nt horizontal. <br><br>
 
Finally we recuperate the position on the complete picture of the crop for the second step in a position file. So we can say crop picture (independant objet) is here (in the complete scene)</h4>



<strong><h1>STEP TWO</h1></strong>
<h4>We try to verify if we have the current object in our model. <br>
We can have x models with 10 labels.<br><br>
for example :<br><br>
 
 - first model can has 0 -> dog &nbsp;&nbsp; 1 -> cat &nbsp;&nbsp; 5 -> bird &nbsp;&nbsp; 9 -> snake<br><br>
 - second model can has 0 -> car &nbsp;&nbsp; 5 -> roller &nbsp;&nbsp; 9 -> ball<br><br>

So we make a label file who say to us the label of this object, the number of the model and csv, the part of the object and finnally his dimension for the training.<br><br>

For has the dimension we course the dataset where we have download picture (transform pixel to cm) and make an approximation of size (who's writted into label file).
During the first training we only put the label and the name of the object. We enter the lasts informations like model number if we have a detection at the end.


So we'll try to match with dimension of the label file if we get this objet into our model.<br><br>

This second step is essentially for display the picture, recup dimension, recup label and... recup object with a detection ! For the displaying we recuperate the lasts positions of the first step from the position file and display the complete picture with the independant picture of the object with arrow. Name of the detection if we have a detection or interogative points if we havn't got the detection. In the last case we recuperate the object with detection into a list.


<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/54853371/67530531-9de92700-f6bf-11e9-9baa-2014c7e99217.jpg">
</p>

<em>This is maybe ugly but there are a slot system who make it more beauty !</em>


</h4>


<h1>Step Three</h1>
<h2>scrap</h2>








<h1>Step Fourth</h1>

<h2>Image processing</h2>


<h2>Delete background</h2>

Here we try to recup the object in a background different from a white background 

not a robust background because it remove an unify background because we just need the form

![aa-ConvertImage](https://user-images.githubusercontent.com/54853371/67151961-803a4d00-f2ce-11e9-8b6c-12888f8b0f5c.png)

<em>Background to remove background</em>

<br><br><br>



<h2>repair multiple object</h2>

Here we recover and separate objects from each other in a scene like:

![a-ConvertImage](https://user-images.githubusercontent.com/54853371/67152924-c77d0980-f2df-11e9-9a47-8c671cad8bbe.png)

<em>Scene with multiple objects to object by object</em>

<br><br><br>

<h2>positioning</h2>

here we rotate the image to put the object in a desired direction with soh cah toa

<h3>For that</h3>

Thank to <strong>Simon Belleguy</strong> who's help me a lot for mathematic formula !

- We take the max point, the head and the footer of the current object

PICTURE

- We define 4 categories because rotation isn't the same by inclinaison:
 
  - 1) top bot (top up, bot down)
  
  - 2) bot top (top down, bot up)
  
  - 3) horinzontal leaning
  
  - 4) normal

- We calculate the arctangeante because we have opposite and adjacent side.

- We rotate it to 45 - current degrees (x1; y1) - current degrees (x2; y2) 

- We re took current position of head and footer

- calculate distance on y axis on the two (we want |y1 - y2| < 10)

- We try a direction if |y1 - y2| increment from the last point we tried the opposite direction

- It make me so proud !

![cc-ConvertImage](https://user-images.githubusercontent.com/54853371/67152972-5a6a7380-f2e1-11e9-96ec-17d701f1d5d4.png)

![bb-ConvertImage](https://user-images.githubusercontent.com/54853371/67152957-f182fb80-f2e0-11e9-8a12-cd832d0d4ce7.png)

<em>Data to good rotation</em>

<br><br><br>

<h2>delete</h2>

Here we delete data destroy by last operations (background who break some picture or didn't worked)...

Indeed we removing small and big contours 1400 < contour > 11000




<h2>Dimension</h2>





<h2>Find part</h2>
 for v2










<br><br><br><br>

<h1>Step five</h1>

<h2>Recuperate dimensions by Thread/Auto programming</h2>

could be ! maybe... maybe an arg** do the same


<h1>Step six</h1>

<h2>Supervised learning</h2>

 only 4 lines from a tuto



<h1>Step seven</h1>

<h2>Decection from last leanning</h2>


<h1>Step height</h1>

<h2>modify current csv and model from csv and model training</h2>

we only can obtein the spoons and the fork (in reality it detect fork + spoon) and not the cut

but we can say it's correct ! because we never choose our dataset and quality from our start picture has a bad quality and for the cut, and we only download 200 pictures (case it's so long) and among the last 200 pictures there are a lot of strange objets !
i think have understood how train a classifier so it's ok for me. How terminator could detect unknow objects maybe with this u_u 



<p align="center">
 <img width="460" height="300" src="https://user-images.githubusercontent.com/54853371/67612661-8cc61600-f7a4-11e9-88aa-672bfe426dea.jpg">

</p>


<br><br><br><br><br><br><br><br><br><br><br><br><br>
<h1>Limits</h1>

 - our remove background destroy a lot of data
 
 - our detector detect only form, and if we have many object with the same form ?
 
 - scraping
 
 - false detection in case plate section has a multiple object (can redetection and raise the csv line)
 
 - one operation can be ok on a picture and not ok on another







<h4>Hey my name's JB, I tested to make programs based on image processing. Because I think it's really cool and funny ! i tried to make a programm who by the presentation of a complex scene and the learning of detection of a plate would seek several objects at random and automatically detect other objects without explicite objects learning. It based on scrap and download picture on the web. </h4>
