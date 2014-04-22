import serial, time,re,sys
light = ['#00FF00', '#00FF00', '#00FF00', '#00FF00'];
ser = serial.Serial()

#serial port used to get data from Adruino kit
#depending on the which serial port is used for communication, the user needs to change it's value
#the serial port can be seen from  AdruinoIDE using Tools->Serial port  
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes

ser.open()

pre=[0,0,0,0];

#Change the web page depending on the data read from serial port
def write2HTML (fp, light) :
	contents= "<!DOCTYPE html> <html><head> <meta http-equiv=\"refresh\" content=\"2\"> </head> <body>";
	contents += "<img src=\"Simple.png\">";
	contents += "<div style=\"background-color:"+light[0]+";\">"
	contents += "<p>ZONE 1.</p>"
	contents += "</div>"
	contents += "<div style=\"background-color:"+light[1]+";\">";
	contents += "<h3>ZONE 2</h3>";
	contents += "</div>";
	contents += "<div style=\"background-color:"+light[2]+";\">";
	contents += "<p>ZONE 3</p>";
	contents += "</div>";
	contents += "<div style=\"background-color:"+light[3]+";\">";
	contents += "<p>ZONE 4</p>";
	contents += "</div>";
	contents += "</body>";
	contents += "</html>";

	fp.write(contents);

#The while loop continously reads data from the serial port
while True:
	response = str(ser.readline())
	words=response.split()
		
	#From serial output extract the status zone number whether on or off and compare with previous status
	if (sum (map( (lambda x,y: int(x)^int(y)), pre,words[0:4] )) != 0 ) :
		pre=words;
		for i in range(4):
			if ( int(words[i]) == 1 ) :
				light[i] = '#FF0000';
			else :
				light[i] = '#00FF00';
		fp=open("myhtml.html","w");
		write2HTML(fp, light);
		fp.close();



	
		

	


