import webbrowser
class Movie():
    """this is class"""
    def __init__(self,movie_title,movie_storyline,movie_poster_image,youtube):
        self.title=movie_title
        self.story_line=movie_storyline
        self.poster_image_url=movie_poster_image
        self.trailer_youtube_url=youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
