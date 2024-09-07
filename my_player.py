from song import Song
from binary_search_tree import BinarySearchTree
from stack import Stack


class MyPlayer:
    def __init__(self):
        """

        :return:
        """
        self.songList = []
        self.is_sorted = False
        self.yearMemory = None
        self.playHistory = None
        # TODO: Modify the above attribute for Task 6

    def loadLibrary(self, filename: str):
        """

        :param filename:
        :return:
        """
        with open(filename, "r") as file:
            line = file.readline()
            for line in file:
                song_data = line.strip().split('|')
                artist_name, song_title, song_id, duration, year = song_data
                song = Song(artist_name, song_title,song_id,float(duration),int(year))
                self.songList.append(song)



    def quickSort(self):
        """

        :return:
        """
        # TODO: Sort your songList here...
        self.is_sorted = True

    def playSong(self, title):
        """

        :param title:
        :return:
        """
        #i = 0
        #found = False
        #while i < len(self.songList) and not found:
            #if self.songList[i].song_title == title:
                #self.songList[i].play()
                #self.playHistory = self.songList[i]
                #found = True
            #i = (i + 1)

        #if not found:
            #print(f"Song '{title} not found in the library")


    def getLastPlayed(self):
        """

        :return:
        """
        return (self.playHistory)

    def buildYearMemory(self):
        """

        :return:
        """
        self.yearMemory = None

    def getYearMemory(self, year, title):
        """

        :param year:
        :param title:
        :return:
        """
        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song

        # TODO: Search for the song, note, you are NOT allowed to use self.songList in this method
        # TODO: You can assume self.buildYearMemory is already called, no need to call it here

        # Do not modify the return line, assign proper values for
        # steps and song above
        return {"steps": steps, "song": the_song}

    def getSong(self, year, title):
        """

        :param year:
        :param title:
        :return:
        """
        steps = 0  # Number of steps used to search for the song
        the_song = None  # The song

        # TODO: Search for the song, Note, you are NOT allowed to use self.yearMemory in this method

        # Do not modify the return line, assign proper values for
        # steps and song above
        return {"steps": steps, "song": the_song}


# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_my_player.py
