class Song:
    def __init__(self, artist_name: str, song_title: str, song_id: str, duration: float, year: int):
        """

        :param artist_name:
        :param song_title:
        :param song_id:
        :param duration:
        :param year:
        :return:
        """
        self.artist_name = artist_name
        self.song_title = song_title
        self.song_id = song_id
        self.duration = duration
        self.year = year


    def __str__(self):
        """
        :return:
        """

        return (f"{self.song_title} by {self.artist_name} (ID: {self.song_id}) released in {self.year}")

    def play(self):
        """

        :return:
        """
        return (f"{self.song_title} is playing, with a duration of {self.duration} second(s)")