## ServoFishFeeder
3D Printed automatic fish feeder  + servo + Raspberry Pi

### Parts List

 - Servo Motor
 - Raspberry Pi 3 B+
 - 1k &ohm; resistor
 - 3D Printed Automated Fish Feeder from [https://www.thingiverse.com/thing:497637/files](https://www.thingiverse.com/thing:497637/files)
 
 

### Setup
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
13. Proceed to Wiring steps!

### Wiring
![raspberry pi wiring](/images/rpi_fish_feeder_bb.png)

**Common Servo Pin-out Wire Colors**

| Signal | + | - |
| :---: | :---: | :---: |
| Yellow | Red | Black |
| White| Red | Black |
| Yellow | Red | Brown |

Setup Continued
1. Now that you have it wired up, let's run it once to get it to zero position.
2. We only want the servo wired up -- don't connect it to the 3D print just yet.
3. `cd ServoFishFeeder`  
4. `python feeder.py`
5. Testing will run to show Wednesday, Thursday, Friday, Saturday and Sunday positions

### Want to run this at startup?
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
 - 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1NzU2MjU0MSwtMTczMDE3MTEyMCwxNz
Q4MDY1NzkwLC00NDA2NDQ0MzYsLTE5NDk4MjY0NjgsMzE2MzM3
NzA0LC0xMTkwMTAyOTYxLC0yMTA4MTcwODQ3LDIxMjU1MzkzNz
ksLTUyNzYzODE5NCwtMTE1NTY5NDkxOCwtODI0Nzk5OTQwLDMz
MjQ1NTkxLDE0NDM3OTU4NTIsLTE1MzYxOTM5NTUsMTI0MDUzMz
IyNF19
-->