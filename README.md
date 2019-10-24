# work-on-picture (write pep8 and testing)

Hey my name's JB, I tested to make programs based on image processing. Because I think it's really cool and funny ! i tried to make a programm who by the presentation of a complex scene and the learning of detection of a plate would seek several objects at random and automatically detect other objects without explicite objects learning. It based on scrap and download picture on the web. 

I had a lot of fun, most of the time! to work on the image for have the best dataset ever ! possible (<em>it doesn't work, blam the dataset</em>).



![diagramme](https://user-images.githubusercontent.com/54853371/67506455-5ba6f200-f68d-11e9-8cde-234bdfe8ba0f.png)





here are some applications:





<h1>scrap</h1>

<h2>Categories</h2>

first: plate ->  search categorie -> give -> washing up (i hate that) -> give -> aliment, -> spoon, cut, tomato...

<h2>Composition object</h2>

Here we define size of our objects

Thank to that we can define resize and matching for leaning for ewample a plate can be 50x50 dimension and spoon can be 100x200 (A faire label)

<br><br><br><br>

<h1>Image processing</h1>


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

<br><br><br><br>



<h2>Supervised learning</h2>












<br><br><br><br><br><br><br><br><br><br><br><br><br>
<h1>Limits</h1>

 - our remove background destroy a lot of data
 
 - our detector detect only form, and if we have many object with the same form ?
 
 - scraping
 
 - false detection in case plate section has a multiple object (can redetection and raise the csv line)
 
 - one operation can be ok on a picture and not ok on another
