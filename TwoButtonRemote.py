import sys
import curses

screen = curses.initscr()
curses.raw()
curses.cbreak()
screen.keypad(1)

mode = 'volume' # volume, channel, brightness, operating mode
volume = 1
brightness = 1
channel = 1
operatingMode = 'on'
temp = ''


while True:
	print "Press a button - up arrow, down arrow, or right arrow (representing both buttons being pressed)"
	screen.refresh()
	key = screen.getch()
	screen.clear()
	screen.refresh()
	# up or down buttons pressed
	if key == curses.KEY_UP or key == curses.KEY_DOWN:
		if mode == 'operation':
			if operatingMode == 'on':
				operatingMode = 'standby'
			else:
				operatingMode = 'on'
			temp = operatingMode
		elif mode == 'volume':
			if key == curses.KEY_UP and volume < 40:
				volume+=1
			elif key == curses.KEY_DOWN and volume > 0:
				volume-=1
			temp = str(volume)
		elif mode == 'channel':
			if key == curses.KEY_DOWN:
				if channel == 5:
					channel = 1
				else:
					channel +=1
			else:
				if channel == 1:
					channel = 5
				else:
					channel -=1
			temp = str(channel)
		elif mode == 'brightness':
			if key == curses.KEY_UP and brightness < 100:
				brightness+=1
			elif key == curses.KEY_DOWN and brightness > 0:
				brightness-=1
			temp = str(brightness)+'%'
		print "Mode: " + mode + " - " + temp +"\n"
	# both buttons pressed
	elif key == curses.KEY_RIGHT:
		if mode == 'volume':
			mode = 'channel'
			temp = str(channel)
		elif mode == 'channel':
			mode = 'brightness'
			temp = str(brightness)+'%'
		elif mode == 'brightness':
			mode = 'operation'
			temp = operatingMode 
		else:
			mode = 'volume'
			temp = str(volume)
		print "Mode: "+ mode + " - " + temp+"\n"
	else:
		print "Incorrect input."+"\n"
	screen.refresh()
