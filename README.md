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
5. ` git clone https://github.com/stephlage/ServoFishFeeder`
6. `cd ServoFishFeeder`
7. `pip install schedule`
8. `python feeder.py`

### Wiring
![raspberry pi wiring](/images/rpi_fish_feeder_bb.png)

**Common Servo Pin-out Wire Colors**

| Signal | + | - |
| :---: | :---: | :---: |
| Yellow | Red | Black |
| White| Red | Black |
| Yellow | Red | Brown |


### Want to run this at startup?
There's a few different ways to do this, but I prefer using PM2.
1. `sudo apt-get updates` 
2. `sudo apt-get upgrade`
3. `sudo apt-get install nodejs npm`
4. `npm install pm2 -g`
5. `cd AquaFeeder`
6. `pm2 start feeder.py`
7. `pm2 save`






# Resources:

 

 - 3D Printed Automated Fish Feeder: [https://www.thingiverse.com/thing:497637/files](https://www.thingiverse.com/thing:497637/files)
 - Install NPM: [https://www.npmjs.com/package/raspberry](https://www.npmjs.com/package/raspberry)
 - Install PM2: [https://www.npmjs.com/package/pm2](https://www.npmjs.com/package/pm2)
 - 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MTY4MDY0MzMsMTc0ODA2NTc5MCwtND
QwNjQ0NDM2LC0xOTQ5ODI2NDY4LDMxNjMzNzcwNCwtMTE5MDEw
Mjk2MSwtMjEwODE3MDg0NywyMTI1NTM5Mzc5LC01Mjc2MzgxOT
QsLTExNTU2OTQ5MTgsLTgyNDc5OTk0MCwzMzI0NTU5MSwxNDQz
Nzk1ODUyLC0xNTM2MTkzOTU1LDEyNDA1MzMyMjRdfQ==
-->