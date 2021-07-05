import turtle as tr
from datetime import datetime

# a file that contains history inputs in the program
a = open("history_inputs.txt", "a")

# variable declaration
fd = tr.forward
rt = tr.right
lt = tr.left
bk = tr.back
gt = tr.goto
title = tr.title
screen = tr.getscreen

# big variable
title_name = 'ROBOT BUILDER'
background_color = input("Enter the color of background you want to choose: ")
upper_rectangle_color = input("Enter the color of head you want to choose: ")
color_of_eye = input("Enter the color of eye box you want to choose: ")
color_of_mouth = input("Enter the color of mouth you want to choose: ")
black = input("Enter the color of eyes you want to choose: ")
color_for_neck = input("Enter the color of neck you want to choose: ")
down_rectangle_color = input("Enter the color of body you want to choose: ")
left_hand_color = input("Enter the color of left hand you want to choose: ")
right_hand_color = input("Enter the color of right hand you want to choose: ")
left_leg_color = input("Enter the color of left leg you want to choose: ")
right_leg_color = input("Enter the color of right leg you want to choose: ")

a.write(f'***************************** date and time: {datetime.now()} *****************************\n')
a.write(f'background_color: {background_color}\n')
a.write(f'upper_rectangle_color: {upper_rectangle_color}\n')
a.write(f'color_of_eye: {color_of_eye}\n')
a.write(f'color_of_mouth: {color_of_mouth}\n')
a.write(f'black: {black}\n')
a.write(f'color_for_neck: {color_for_neck}\n')
a.write(f'down_rectangle_color: {down_rectangle_color}\n')
a.write(f'left_hand_color: {left_hand_color}\n')
a.write(f'right_hand_color: {right_hand_color}\n')
a.write(f'left_leg_color: {left_leg_color}\n')
a.write(f'right_leg_color: {right_leg_color}\n\n')


# shape builder head of robot


def head_of_robot(upper_rectangle_color):

    # fill color
    tr.color(upper_rectangle_color)
    tr.fillcolor(upper_rectangle_color)
    tr.begin_fill()
    # controlling pen turtle
    tr.penup()
    tr.goto(0, 90)
    tr.pendown()
    # Make shape
    fd(100)
    lt(90)
    fd(90)
    lt(90)
    fd(200)
    lt(90)
    fd(90)
    lt(90)
    fd(100)
    # end with filling color
    tr.end_fill()

# eye box maker


def making_eye(color_of_eye):

    tr.color(color_of_eye)
    tr.fillcolor(color_of_eye)
    tr.begin_fill()

    tr.penup()
    tr.goto(45, 140)
    bk(90)
    lt(90)
    fd(30)
    rt(90)
    fd(90)
    rt(90)
    fd(30)

    tr.end_fill()

    tr.penup()
    tr.goto(10, 137)
    tr.pendown()

# makes dot in robot


def dot_maker(black):

    tr.color(black)
    tr.fillcolor(black)
    tr.begin_fill()
    tr.penup()

    bk(20)
    tr.circle(10)
    tr.end_fill()
    tr.color(black)
    tr.fillcolor(black)
    tr.begin_fill()
    tr.goto(-34, 158)

    tr.pendown()
    tr.circle(10)
    tr.end_fill()

# handles the mouth making


def mouth_maker(color_of_mouth):
    tr.color(color_of_mouth)
    tr.fillcolor(color_of_mouth)
    tr.begin_fill()

    tr.penup()
    tr.goto(40, 130)
    tr.pendown()
    fd(10)
    rt(90)
    fd(80)
    rt(90)
    fd(10)
    rt(90)
    fd(80)
    tr.end_fill()

# it selects the color for neck


def neck_of_robot(color_for_neck):
    tr.color(color_for_neck)
    tr.fillcolor(color_for_neck)
    tr.begin_fill()

    tr.penup()
    tr.goto(10, 90)
    rt(90)
    tr.pendown()
    fd(10)
    rt(90)
    fd(20)
    rt(90)
    fd(10)
    rt(90)
    fd(20)
    tr.end_fill()

# makes the middle body of the robot


def body(down_rectangle_color):

    tr.color(down_rectangle_color)
    tr.fillcolor(down_rectangle_color)
    tr.begin_fill()

    tr.penup()
    tr.goto(10, 80)
    tr.pendown()
    fd(100)
    rt(90)
    fd(200)
    rt(90)
    fd(220)
    rt(90)
    fd(200)
    rt(90)
    fd(120.100)

    tr.end_fill()

# this function makes right hand of robot and color it


def making_hands(right_hand_color):

    tr.color(right_hand_color)
    tr.fillcolor(right_hand_color)
    tr.begin_fill()

    tr.penup()
    tr.goto(111, 60)
    tr.pendown()
    fd(90)
    rt(90)
    fd(90)
    rt(90)
    fd(20)
    rt(90)
    fd(72)
    lt(90)
    fd(70)
    rt(90)
    fd(18)
    tr.end_fill()

# this function makes the left hand of robot and color it


def left_hand(left_hand_color):
    tr.color(left_hand_color)
    tr.fillcolor(left_hand_color)
    tr.begin_fill()

    tr.penup()
    tr.goto(-111, 60)
    tr.pendown()
    lt(90)
    fd(90)
    lt(90)
    fd(90)
    lt(90)
    fd(20)
    lt(90)
    fd(70)
    rt(90)
    fd(70)
    lt(90)
    fd(20)

    tr.end_fill()

# this make left legs of the robot


def making_robot_left_leg(left_leg_color):
    tr.color(left_leg_color)
    tr.fillcolor(left_leg_color)
    tr.begin_fill()

    tr.penup()
    tr.goto(-80, -120)
    tr.pendown()
    rt(90)
    fd(30)
    rt(90)
    fd(90)
    rt(90)
    fd(70)
    rt(90)
    fd(20)
    rt(90)
    fd(40)
    lt(90)
    fd(70)

    tr.end_fill()

# this make right leg of the robot


def making_robot_right_leg(right_leg_color):
    tr.color(right_leg_color)
    tr.fillcolor(right_leg_color)
    tr.begin_fill()

    tr.penup()
    tr.goto(60, -120)
    tr.pendown()
    rt(90)
    fd(30)
    rt(90)
    fd(90)
    rt(90)
    fd(70)
    rt(90)
    fd(20)
    rt(90)
    fd(40)
    lt(90)
    fd(70)

    tr.end_fill()

# function robot builder


def robot_builder(title_name,
                  background_color,
                  upper_rectangle_color,
                  down_rectangle_color,
                  color_of_eye,
                  black,
                  color_of_mouth,
                  color_for_neck,
                  right_hand_color,
                  left_hand_color,
                  left_leg_color,
                  right_leg_color):

    screen()
    t = tr.Turtle()
    tr.bgcolor(background_color)
    title(title_name)
    head_of_robot(upper_rectangle_color)
    making_eye(color_of_eye)
    dot_maker(black)
    mouth_maker(color_of_mouth)
    neck_of_robot(color_for_neck)
    body(down_rectangle_color)
    making_hands(right_hand_color)
    left_hand(left_hand_color)
    making_robot_left_leg(left_leg_color)
    making_robot_right_leg(right_leg_color)
    tr.done()


robot_builder(title_name, background_color,
              upper_rectangle_color, down_rectangle_color,
              color_of_eye, black, color_of_mouth, color_for_neck,
              right_hand_color, left_hand_color, left_leg_color, right_leg_color)
