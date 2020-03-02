# "Stopwatch: The Game"
import simplegui

# defining global variables
t = 0
WIDTH = 200
HEIGHT = 200
click_stop = 0
click_stop_whole = 0
time = "A:BC.D"
start = True

# defining helper function format that converts time
def format(t):
    '''function that correctly formats input from global variable t into stopwatch format'''
    
    #formats input from global variable t into the corresponding number of minutes (A), seconds (B), tens of seconds (C), and tenths of seconds (D) (eg, A:BC.D)
    # accomplishes this using integer division, modular arithmetic, and string processing.
    A = str(t // 600) 
    x = str(t % 600)
    if len(x) == 2:
        #adding one leading zero
        B,C,D = ("0" +  x)[0],("0" +  x)[1],("0" +  x)[2]
    elif len(x) == 1:
        #adding two leading zeros
        B,C,D = ("00" + x)[0],("00" + x)[1],("00" + x)[2]
    else:
        B,C,D = x[0],x[1],x[2]
    global time
    time =  A + ":" + B + C + "." + D
    return time


        
# defining event handlers for buttons; "Start", "Stop", "Reset"
def start():
    '''event handler for start button'''
    
    #starts timer and sets the boolean global variable start to true
    timer.start()
    global start
    start = True

def stop():
    '''event handler for stop button'''
    
    #stops the timer and sets the boolean global variable to false
    timer.stop()
    global click_stop
    global start
    if start:
        click_stop += 1
        global click_stop_whole
        if (t % 10) == 0:
            click_stop_whole += 1
    start = False

    
def reset():
    '''event handler for reset button'''
    
    #resets the timer and the score to zero
    timer.stop()
    global t
    t = 0
    global click_stop_whole
    click_stop_whole = 0
    global click_stop
    click_stop = 0
    


# defining event handler for timer with 0.1 sec interval
def timer_handler():
    '''event handler for the timer'''
    
    #incrementing the global variable t by 1 every time this function is called by the timer.
    global t
    t += 1
    return t


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t),[WIDTH/4,HEIGHT/2], 40, "White")
    canvas.draw_text(str(click_stop_whole) + "/" + str(click_stop), [160, 20], 20, "Green")


simplegui.create_timer(100, timer_handler)

# create frame
frame = simplegui.create_frame('Stopwatch', WIDTH, HEIGHT)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start = frame.add_button('Start', start)
stop = frame.add_button('Stop', stop)
reset = frame.add_button('Reset', reset)

# start frame
frame.start()


