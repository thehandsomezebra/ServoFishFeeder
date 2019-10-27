# ServoFishFeeder
3D Printed automatic fish feeder  + servo + Raspberry Pi

#### 5 Day Automatic Fish Feeder
This Automatic Fish Feeder is perfect for long weekend vacations. It's currently set up for Wednesday thru Sunday, but feel free to fork this and adjust as you'd like. 

🤖🐟

## Parts List

 - Servo Motor
 - Raspberry Pi 3 B+
 - 1k &ohm; resistor
 - Breadboard
 - 3D Printed Automated Fish Feeder from [https://www.thingiverse.com/thing:497637/files](https://www.thingiverse.com/thing:497637/files)
 
 

## Setup
1. Get your raspberry pi running with your preferred OS.  I use [https://www.raspbian.org/](https://www.raspbian.org/)
2. SSH or open the terminal to your pi.
3. `sudo apt-get updates` (updates the list of available packages and their versions)
4. `sudo apt-get upgrade` (installs the newer versions of the packages you have)
5. `git clone https://github.com/stephlage/ServoFishFeeder`
6. `cd ServoFishFeeder`
7. `pip install schedule`
8. `nano feeder.py`
9. Ensure that `test=False`
10. Hit `ctrl + x`
11. Hit `y`
12. Don't change the file name. Hit Enter.
13. Proceed to Wiring.

## Wiring
**Breadboard:**
![raspberry pi wiring with breadboard](/images/rpi_fish_feeder_bb1.png)
**Directly wired:**
![raspberry pi wiring](/images/rpi_fish_feeder_bb.png)

**Common Servo Pin-out Wire Colors**

| Signal | + | - |
| :---: | :---: | :---: |
| Yellow | Red | Black |
| White| Red | Black |
| Yellow | Red | Brown |

## Setup Continued

1. Now that you have it wired up, let's run it once to get it to the startposition.
2. We only want the servo wired up -- don't connect it to the 3D print just yet.
3. `cd ServoFishFeeder`  
4. `python feeder.py`
5. Testing will run Wednesday, Thursday, Friday, Saturday and Sunday positions...then walk itself back to start.
6. When `FEEDER READY TO BE FILLED` is displayed - you can connect this to your 3D print.  ![servo attached to feeder](/images/feeder1.png)
7. You may run the feeder test again. `python feeder.py`
8. If everything looks good, lets turn the test procedures off and set up the times.
9. `nano feeder.py`
10. Adjust the location of the `#` to turn testing off. `test=False`
11. Set the `whattime` variable in 24 hour format.  You can see an example of 10pm and 9am in the code.  `whattime = "09:00"`
12. Hit `ctrl + x`
13. Hit `y`
14. Don't change the file name. Hit Enter.
15. This is now ready to run! `python feeder.py`

## Want to run this at startup...and keep it running all the time?
There's a few different ways to do this, but I prefer using PM2.
1. `sudo apt-get updates` 
2. `sudo apt-get upgrade`
3. `sudo apt-get install nodejs npm`
4. `npm install pm2 -g`
5. `cd ServoFishFeeder` 
6. `pm2 start feeder.py`
7. `pm2 save`






# Resources:

 

 - 3D Printed Automated Fish Feeder: [https://www.thingiverse.com/thing:497637/files](https://www.thingiverse.com/thing:497637/files)
 - Install NPM: [https://www.npmjs.com/package/raspberry](https://www.npmjs.com/package/raspberry)
 - Install PM2: [https://www.npmjs.com/package/pm2](https://www.npmjs.com/package/pm2)
 - Python Job Scheduling: [https://pypi.org/project/schedule/](https://pypi.org/project/schedule/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMzM4OTIyMjcsMTA3NjQ4NzQ5MCwtNz
E2MTY0NjIyLDg5NTk3NDE5NCwxNDY5NzUyMzkwLC0yMDI0NzQ3
NTUxLC03NTY2OTE2MywtMTk4OTA0Mzc5OCwtNTY2OTE2MTYwLC
0xNzMwMTcxMTIwLDE3NDgwNjU3OTAsLTQ0MDY0NDQzNiwtMTk0
OTgyNjQ2OCwzMTYzMzc3MDQsLTExOTAxMDI5NjEsLTIxMDgxNz
A4NDcsMjEyNTUzOTM3OSwtNTI3NjM4MTk0LC0xMTU1Njk0OTE4
LC04MjQ3OTk5NDBdfQ==
-->