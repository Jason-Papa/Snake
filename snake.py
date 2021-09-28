from time import sleep
import keyboard
import msvcrt

refresh_rate = 0.5


class snake:    

    def __init__(self, dir, size, positions , tail):
        self.dir = dir
        self.size = size
        self.positions = positions
        self.tail = tail
    
    def set_direction (self, newdir):
        self.dir = newdir
    
    def head(self):
        return self.positions[-1]

    def move(self):
        self.tail = self.positions[0]
        for i in range (len(self.positions)):
            if i > 0:
                self.positions[i-1] = self.positions[i]
        if self.dir == "up":
            temp_list = list(self.positions[-1])
            temp_list[1] += 1
            self.positions[-1] = tuple(temp_list)
        if self.dir == "down":
            temp_list = list(self.positions[-1])
            temp_list[1] -= 1
            self.positions[-1] = tuple(temp_list)
        if self.dir == "left":
            temp_list = list(self.positions[-1])
            temp_list[0] -= 1
            self.positions[-1] = tuple(temp_list)
        if self.dir == "right":
            temp_list = list(self.positions[-1])
            temp_list[0] += 1
            self.positions[-1] = tuple(temp_list)

    def increment_size(self):
        self.size += 1
        self.positons = self.tail + self.positions
        
class food:
    def __init__(self, position):
        self.position = position
    def reset(self, illegal_positions):
        



def print_map(snake, food):
    for i in range (0, 20):
        for j in range (0,20):
            if (i,j) in snake.positions:
                print ("*", end = '')
            elif (i,j) == food.position:
                print("Q", end = '')
            else:
                print(" ", end ='')
        print("")

    




s = snake("up",3,[(1,2),(2,3),(3,3)], (1,2))
print(s.head())
s.move()
print(s.head())
f = food((3,5))
print_map(s, f)

while(True):
    sleep(refresh_rate)
    print_map(s, f)

    while(True):
        try:  
            print("trying")
            if keyboard.is_pressed('a'): 
                s.set_direction("down")
            if keyboard.is_pressed('d'): 
                s.set_direction("up")
            if keyboard.is_pressed('w'): 
                s.set_direction("left")
            if keyboard.is_pressed('s'): 
                s.set_direction("right")
            break
        except:
            break
          
    s.move()
    if s.head() == food.position:
        s.increment_size()
        food.reset()

    

    
