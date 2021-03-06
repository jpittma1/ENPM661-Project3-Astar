#!/usr/bin/env python3

#ENPM661 Spring 2022
#Section 0101
#Jerry Pittman, Jr. UID: 117707120
#Maitreya Ravindra Kulkarni, UID: 117506075
#jpittma1@umd.edu and mkulk98@umd.edu 
#Project #3 Phase 2

class Obstacle:
    def __init__(self, clearance):
        self.x = 10
        self.y = 10
        self.clearance = clearance
        self.robot_radius = 0.354 / 2
        self.clearance = self.robot_radius + self.clearance

        self.circle1_radius = 0.5
        self.circle2_radius = 1
        self.circle1_x_offset = 2
        self.circle1_y_offset = 2
        self.circle2_x_offset = 2
        self.circle2_y_offset = 8

        self.square1_corner1_x = 0.25
        self.square1_corner1_y = 4.25
        self.square_side = 1.5

        self.rect1_corner1_x = 3.75
        self.rect1_corner1_y = 4.25
        self.rect1_length = 2.5
        self.rect1_width = 1.5

        self.rect2_corner1_x = 7.25
        self.rect2_corner1_y = 2
        self.rect2_length = 1.5
        self.rect2_width = 2

    def isInObstacleSpace(self, x, y):

        if (x < 0 or x >= 10 or y < 0 or y >= 10):
          print('Out of boundary -- Chup chap aat ye !')
          return 1
        # circle1 obstacle
        x_offset = self.circle1_x_offset
        y_offset = self.circle1_y_offset
        radius = self.circle1_radius + self.clearance
        if ((x-x_offset)**2 + (y-y_offset)**2 <= radius):
          print('Inside circle 1; avoid')
          return 1

        # circle2 obstacle
        x_offset = self.circle2_x_offset
        y_offset = self.circle2_y_offset
        radius = self.circle2_radius + self.clearance
        if ((x-x_offset)**2 + (y-y_offset)**2 <= radius):
          print('Inside circle 2; avoid')
          return 1

        # square obstacle
        x1 = self.square1_corner1_x - self.clearance
        x2 = x1 + self.square_side + 2*self.clearance
        y1 = self.square1_corner1_y - self.clearance
        y2 = y1 + self.square_side  + 2*self.clearance
        if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
            print('Inside square, avoid')
            return 1

        #rectangle obstacle 1
        x1 = self.rect1_corner1_x - self.clearance
        x2 = x1 + self.rect1_length + 2*self.clearance
        y1 = self.rect1_corner1_y - self.clearance
        y2 = y1 + self.rect1_width  + 2*self.clearance
        if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
            print('Inside rectangle 1, avoid')
            return 1

        #rectangle obstacle 2
        x1 = self.rect2_corner1_x - self.clearance
        x2 = x1 + self.rect2_length + 2*self.clearance
        y1 = self.rect2_corner1_y - self.clearance
        y2 = y1 + self.rect2_width  + 2*self.clearance
        if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
            print('Inside rectangle 1, avoid')
            return 1

        return 0
