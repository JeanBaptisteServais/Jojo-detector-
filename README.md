<h2>Second treatment</h2>

<h3>Multiple objects</h3>

We recover and separate objects from each other in a scene like:

1) - Here we have many knife, again we found contours by a thresholding to thresh: 250 and max value: 255, if the pixel value is less 250 this pixel is black or 0 else the pixel is define to white or 255. 

2) - Next, we course the black and white picture and recup all contours (when we speak about contours we speak about the border of the object) 


3) - and course them one by one, if the first contour is white, superpose this to the orignal picture and make all the rest in white. 

4) - And we can have only have a knife. We repeat the operation for all objects <em>here 4 times for 4 knifes !</em>

5) - Before training we detect objects, includes them into a rectangle who's gave us (x, y) and (width, height) coordiantes; then we take the object without the white background.

<br><br>

<p>


<img width="250" height="150" align="left" src="https://user-images.githubusercontent.com/54853371/67782765-8ae0a900-fa69-11e9-9c87-12c8ec772e18.png">


<img width="130" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784042-743b5180-fa6b-11e9-8a8f-05865c2e3dce.png">

<img width="130" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67783588-c4fe7a80-fa6a-11e9-9f45-b5edc42d508c.png">


<img width="150" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784689-6d610e80-fa6c-11e9-98b6-75ef626dac9f.png">

<img width="100" height="150" align="center" src="https://user-images.githubusercontent.com/54853371/67784688-6cc87800-fa6c-11e9-8777-6e42c9bb3ad6.png">

</p>






























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
