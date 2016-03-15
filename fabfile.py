import cuisine

PACKAGE_ENSURE = (
	'apache2',
	'libapache2-mod-php5',
	'php5-gd'
)

http_user='www-data'

www_folder="/var/www/html"

def setup_os():
	with cuisine.mode_sudo():
		cuisine.ssh_authorize( "matze" , cuisine.file_local_read("./cuisine_id.pub"))
		for _ in PACKAGE_ENSURE: cuisine.package_ensure(_)
		cuisine.run("a2enmod rewrite")
		# TODO enable   AllowOverride none => all for /var/www
		cuisine.run("service apache2 restart")

def setup_dokuwiki():
	if not cuisine.file_exists('/tmp/dokuwiki-stable.tgz'):
		cuisine.cd("/tmp")
		cuisine.run( " wget -c http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz")
	if not cuisine.dir_exists('/tmp/dokuwiki-20*'):
		cuisine.cd( "/tmp" )   
		cuisine.run("tar xvzf dokuwiki-stable.tgz"); 
	
	## Improve for update purpose
	#if not cuisine.dir_exists( www_folder + "/dokuwiki" ):
	if True:
		cuisine.log_message("Installing")
		with cuisine.mode_sudo():
			cuisine.dir_ensure( www_folder + "/dokuwiki" )
			cuisine.run("cp -rv /tmp/dokuwiki-20*/* " + www_folder + "/dokuwiki" )
			for _ in ( 'data', 'conf' , 'bin' , 'inc'):
				cuisine.file_write( www_folder + "/dokuwiki" + "/" +  _ + "/.htaccess" , cuisine.file_local_read("./htaccess_template") , owner=http_user , group=http_user)
			cuisine.dir_ensure( www_folder + "/dokuwiki", owner=http_user , group=http_user , recursive=True  )

	print "now visit <IP>/dokuwiki/install.php"	
