from users import User
from userInterface import Window

if __name__ == "__main__":
    #Handle User Initialisation
    player = User().initFromDB("Josh2")
    if player.isInitialised():
        print(player)
        print(dict(player))
    else:
        raise(Exception("Player was not initialised!"))
    
    #Create window
    win = Window(resolution=(60,20))
    win.renderFrame()
    #win.renderLoop()
    win.run(debug=False, fps=30)