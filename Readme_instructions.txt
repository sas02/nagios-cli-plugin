Step1 ) Install nagios 
	server and client respectively.

Install NRPE on client servers
	comand:"apt-get install -y python nagios-nrpe-server"

Step 2) Clone the files from the git and mov them to /usr/lib/nagios/plugins/

step3) Both files are Executables 

note :
	The entire Nagios NRPE plugin boils down to using exit codes to trigger alerts (whether it is OK, WARNING, CRITICAL, or UNKNOWN).

Exit Code 	Status
	0 	OK
	1 	WARNING
	2 	CRITICAL
	3 	UNKNOWN





