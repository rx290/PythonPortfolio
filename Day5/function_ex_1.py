import  math
def can_counter(wall_height, wall_width):
    coverage = 5
    num_of_cans = (wall_height * wall_width)/coverage
    print("you'll need", math.ceil(num_of_cans), "cans of paint.")
    

can_counter(3,9)