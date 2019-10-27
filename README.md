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
2. `cd ServoFishFeeder` 
3. `python feeder.py`

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
eyJoaXN0b3J5IjpbNDI3OTIzNzM5LC0xNzMwMTcxMTIwLDE3ND
gwNjU3OTAsLTQ0MDY0NDQzNiwtMTk0OTgyNjQ2OCwzMTYzMzc3
MDQsLTExOTAxMDI5NjEsLTIxMDgxNzA4NDcsMjEyNTUzOTM3OS
wtNTI3NjM4MTk0LC0xMTU1Njk0OTE4LC04MjQ3OTk5NDAsMzMy
NDU1OTEsMTQ0Mzc5NTg1MiwtMTUzNjE5Mzk1NSwxMjQwNTMzMj
I0XX0=
-->