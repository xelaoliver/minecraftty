# MinecrafTTY

'Play' Minecraft in the terminal with python.

![Minecraft title screen, shown using MinecrafTTY](https://github.com/xelaoliver/minecraftty/blob/main/screenshot.png)

# Setting up

In your Minecraft Launcher, set the game window height and width to 640 by 480 or any configurable size (this must be put into the code aswell as: ```screen["captureWidth"]``` and ```screen["captureHeight"]```). When Minecraft is running, run the script and if your terminal is adjusted to the correct aspect ratio/resolution, you should be able to play Minecraft. Please note, any obstructing windows that overlap/cover Minecraft would interfere with gameplay. It's reccomended to run MinecrafTTY on a second monitor.

# How it works

This program uses ```ImageGrab``` to grab the colour of pixels that are within the Minecraft game window. It then prints them collectively with ASCII characters and ANSI escape sequences. This project is aimed to run ar 30FPS to limit the amount of recources this project takes up.
