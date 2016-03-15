Example Cuisine  / Fabric file 

This is a simple example for a Cuisine & Fabric script. Make sure the user has sudo rights on the target system. This script is used through fabric.

!! Do not use on production system, because a security step on the apache configuration was ommited. !!

System-Requirements:
	installed python2 package fabric
	installed cuisine 
		( was installed using pip2 )

Command Line call was:

	fab -i cuisine_id -u matze -H <IP> setup_os setup_dokuwiki

	You can also add multiple IPs to configure different hosts at one run.


More reading-foo:

	https://www.dokuwiki.org/installer
	https://www.dokuwiki.org/security
	https://github.com/sebastien/cuisine
	

Another helpful example with direct script execution via cuising and fabric implicit:
  https://bitbucket.org/locative/invisibleislands-devices


DISCLAMER:
	I'm no Python guru, it is only to demonstrate the usecase

