Project: Movie Trailer Website  - Harry DiFrancesco
================================

Required Libraries and Dependencies
-----------------------------------
This program requires Python v2.7.10 to be installed


How to Run Project
------------------
1.Navigate to the github repo at https://github.com/hcdifrancesco/Movie-Website
2.Download the zip file.
3.Open a browser
4.Open Python 2.7.10
5.Open the entertainment_center.py file.
6.Run the program from the toolbar or keyboard shortcut (fn F5 on a Mac)
7.The page should appear in your browser: you can watch the trailers by clicking on the movie posters and learn more about the movies by hovering over "Additional Information"


Extra Credit Description
------------------------
I added additional information for actors each movie and the oscar wins each movie collected. In the media.py file these appear as further attribute in the __init__ function. In the entertainment_center.py file these appear below the youtube links for each movie.

As part of adding this additional info I created some extra CSS and HTML in the fresh_tomatoes.py file . The CSS is located below the navbar-header class——I added comments to note it. The HTML is located in movie_tile_content.

I added an “Additional Information” section to each movie, which appears below its title. So as not to make the page too busy I added a popup box that shows only when the cursor hovers over “Additional Information.” The popup box shows the movie’s oscar wins and actor’s names. 

Miscellaneous
-------------
I’d like to point out that the basic architecture for the popupbox that I created was found through searching through various stackoverflow forums. 

I’d also like to ask a question about making the popup boxes more responsive——in other words I would like them to appear even if their location is currently of the screen. Not sure if there is a simple fix to this but if there is and you have time or a good resource to look at please let me know——dug around a little but couldn’t get it to fit well and perform. 