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






After have define this we:


- We calculate the arctangeante because we have opposite and adjacent side.

- We rotate it to 45 - current degrees (x1; y1) - current degrees (x2; y2) 

- We re took current position of head and footer

- calculate distance on y axis on the two (we want |y1 - y2| < 10)

- We try a direction if |y1 - y2| increment from the last point we tried the opposite direction

- It make me so proud !




  
![cc-ConvertImage](https://user-images.githubusercontent.com/54853371/67152972-5a6a7380-f2e1-11e9-96ec-17d701f1d5d4.png)

![bb-ConvertImage](https://user-images.githubusercontent.com/54853371/67152957-f182fb80-f2e0-11e9-8a12-cd832d0d4ce7.png)









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
