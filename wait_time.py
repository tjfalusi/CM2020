from microbit import*

wait_time = (1.5)
    #set the wait time

display.show(Image.HAPPY)
    #display image on LED array
sleep(wait_time*1000)
    #wait for n milliseconds
display.show(Image.CONFUSED)
sleep(wait_time*1000)
display.show(Image.ANGRY)
sleep(wait_time*1000)
display.clear()
    #clear display