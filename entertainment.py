import media
import fresh_tomatoes
toys_story=media.Movie("Toy Story","A story of toys","http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("Avatar","a marine on a quest","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6id5fJrnPWQgNvh9klWIivEyWtUruCxWNNciYsd6j4mlNsMx3","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
harry_potter=media.Movie("Harry Potter","quest of a wizard boy","http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster-150x250.jpg","https://www.youtube.com/watch?v=geNlXmmIp7w")
game_of_thrones=media.Movie("Game of thrones","story of westeros","https://s-media-cache-ak0.pinimg.com/originals/1c/fc/63/1cfc63ec179a6ddbb2cae7a5f06f4b06.jpg","https://www.youtube.com/watch?v=giYeaKsXnsI")
breaking_bad=media.Movie("Breaking bad","money is everything","https://i.pinimg.com/736x/89/10/2b/89102b3be2ed95df6edaa404a4d10301--breaking-bad-jesse-breaking-bad-poster.jpg","https://www.youtube.com/watch?v=HhesaQXLuRY")
movies=[toys_story,avatar,harry_potter,game_of_thrones,breaking_bad]
fresh_tomatoes.open_movies_page(movies)
