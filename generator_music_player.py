
def music_player():
    playlist = range(1, 6)
    # Creating a for loop to give a choice to the user.
    for song in playlist:
        print("Playing son #:", song)
        yield song
        
