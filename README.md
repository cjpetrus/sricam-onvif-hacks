# sricam-onvif-hacks
for use with sricam sp012. this allows you to use ptz controls using the arrow keys on your keyboard(pygame) and soap requests with the requests module.
This specific camera doesnt even authenticate requests , the definition of insecure. 
Worst implementation of onvif ever. You can also watch the rtsp stream, in conjunction and view any sricam running their latest firmware.
no authentication needed. check out the example for more info.

## IPCAM Pwnage
---- rtsp stream looks like this
rtsp://ip-cam-address:554/onvif1

---- ptz control
http://ip-cam-address:5000/onvif/

### Demo

a = Camera('10.0.0.123','5000',user='',passwd='')
a.move_up()

Thats it!
