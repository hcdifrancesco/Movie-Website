import fresh_tomatoes
import media


#Creating an instance of Movie called The Hurt Locker.
the_hurt_locker = media.Movie("The Hurt Locker",
                        "A revealing and subtle portrait of the war in the Iraq through the story of a 3 man EOD team.",
                        "https://upload.wikimedia.org/wikipedia/en/6/6c/HLposterUSA2.jpg",
                        "https://www.youtube.com/watch?v=2GxSDZc8etg",
                        "Jeremy Renner",
                        "Best Picture, Best Director, Best Original Screenplay, Best Film Editing, Best Sound Mixing, Best Sound Editing")   


#Creating an instance of Movie called Avatar.
rain_man = media.Movie("Rain Man",
                     "Charlie Babbitt discovers that his father has given the entire estate to Raymond, his father's other son and an autistic savant.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b2/Rain_Man_poster.jpg",
                     "https://www.youtube.com/watch?v=KKC3W0awjm0",
                     "Dusting Hoffman and Tom Cruise",
                     "Best Picture, Best Original Screenplay, Best Director, Best Actor in a Leading Role")


#Creating an instance of Movie called A Beautiful Mind.
a_beautiful_mind = media.Movie("A Beautiful Mind",
                               "John Nash, brilliant mathematician, accepts work in cryptography and his life takes a turn for the worse.",
                               "https://s-media-cache-ak0.pinimg.com/originals/57/f3/a2/57f3a2eb9703ceb3700ead00eb4f2c63.jpg",
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
                               "Russell Crowe and Jennifer Connelly",
                               "Best Picture, Best Actress in a Supporting Role, Best Director, Best Writing")

#Creating an instance of Movie called Lawrence of Arabia.
lawrence_of_arabia = media.Movie("Lawrence of Arabia",
                                 "T.E Lawrence is sent to Arabia to liaise between British and Bedouin tribes but ends up going rogue and rallying the Arabs to attach Aqaba from the Desert.",
                                 "http://www.gaiahealthblog.com/wordpress1/wp-content/uploads/2015/03/MPW-21346.jpg",
                                 "https://www.youtube.com/watch?v=7nH5iPgNkoY",
                                 "Peter O'toole and Omar Sharif",
                                 "Best Picture, Best Director, Best Cinematography, Best Art Direction, Best Sound, Best Film Editing, Best Original Score")

#Creating an instance of Movie called Birdman.
birdman = media.Movie("Birdman",
                     "Riggan Thompson, failed Hollywood star, tries to mount a Broadway adaptation of a Raymond Carver short story.",
                     "http://www.filmjabber.com/movie-poster-thumbs/birdman-movie-poster-5097.jpg",
                     "https://www.youtube.com/watch?v=uJfLoE6hanc",
                      "Michael Keaton",
                      "Best Picture, Best Director, Best Original Screenplay, Best Achievement in Cinematography")

#Creating an instance of Movie called Slumdog Millionaire.
slumdog_millionaire = media.Movie("Slumdog Millionaire",
                                  "Jamal Malik, an eighteen year-old from a slum, is about to win India's version of Who Wants to Be A Millionaire. Then reality catches up. Or at least for a bit.",
                                  "https://www.movieposter.com/posters/archive/main/110/MPW-55462",
                                  "https://www.youtube.com/watch?v=AIzbwV7on6Q",
                                  "Dev Patel and Freida Pinto",
                                  "Best Picture, Best Director, Best Adapted Screenplay, Best Achievement in Cinematography, Best Achievement in Film Editing, Best Original Score, Best Original Song, Best Achievement in Sound Mixing")

#Storing instances of Movie in an Array.
movies = [the_hurt_locker, rain_man, a_beautiful_mind, lawrence_of_arabia, birdman, slumdog_millionaire]

#Opening the movies page with the fresh_tomatoes file.
fresh_tomatoes.open_movies_page(movies)






                      
