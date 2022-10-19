import random
import math

from gamelib import *

class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)

class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        # You may add any instance attributes you find useful to save information between frames

    def selectBehavior(self):
        # Replace the body of this method with your character's behavior
        def distance(x, y, zombie):
              zombie_dist_dic = dict()
              for key, value in zombie.items():
                xi, yi = value
                dis = abs(int(x)-int(xi))+abs(int(y)-int(yi))
                zombie_dist_dic[key] = dis
              return zombie_dist_dic
        # find minimum distance among the above distance
        def find_mini_dis(x, y):
              scan_res = self.getScanResults()
              if len(scan_res):
                scanned_dict = dict()
                for z in scan_res:
                    scanned_dict[z.getID()] = z.getPos()
                zombie_dist = distance(x, y, scanned_dict)
                mini_dis    = min(list(zombie_dist.values()))
                #print("mini distance+++++++++++++++++++++++++++++++++")
                #print(mini_dis)                          
                return mini_dis  
        # find a player location that can maximize the minimum distance 
        def find_location(x, y, size_x, size_y):
              old_mini_dis = find_mini_dis(x, y)
              x_max = x
              y_max = y
              for i in range(size_x):
                   for j in range(size_y):
                      if (abs(i - x) + abs(j - y)) <= 3:
                        if find_mini_dis(i, j):
                            new_mini_dis = find_mini_dis(i, j)
                            if new_mini_dis > old_mini_dis:
                                  old_mini_dis = new_mini_dis
                                  x_max = i
                                  y_max = j
              next_position = [x_max, y_max]                 
              return next_position
                        

        x, y = self.getPos()
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        radius = math.sqrt(1.0 / (4.0 * 3.14) * size_x * size_y)
        # select behavior for next step
        print("find next player location +++++++++++++++++++++++++++++++++")
        next_pos = find_location(x, y, size_x, size_y)
        print(next_pos)
        health  = self.getHealth()
        # current_health = health._health
        # if x != next_pos[0] or y != next_pos[1]:
        #      return MoveEvent(self, next_pos[0], next_pos[1])
        # elif current_health <= 500:
        #      return HealEvent(self)
        # else:
        #      return ScanEvent(self)
        pass