# Zombie-Game

For the PlayerCharacter class, we define three functions that can give us the surrounding information
to help us determine what the player do in the next step. The following three methods calculate
the distance between the player and all zombies in the scanned area, the smallest distance between
the player and zombies, and a safe location that the player can move in the next step, respectively.

``class PlayerCharacter(ICharacter)``:

``def selectBehavior(self)``:

``def distance(x, y, zombie)``: calculating the distance between the player and all zombies in
the scanned area and saving the information (zombies' IDs and the corresponding positions) into a
dictionary;

``def mini dis(x, y)``: using the information from self.getScanResults() function to nd
current zombies' IDs and positions in the scanned area and calling def distance(x, y, zombie) to
calculate the minimum distance between the player and zombies;

``def location(x, y, size x, size y)``: finding a player location that can maximize the
minimum distance between the player and zombies in the scanned area so that the player can move
to a safer location in the next step;

For the ZombieCharacter class, we add some codes to enable zombies to target and attack. If
there are zombies in the scanned area, zombies will target and attack the player. If there are no
zombies in the scanned area, zombies will move to next location or heal themselves.
