#!/bin/bash

clear
echo "----------------------------"
echo "!!!!!     WARNING     !!!!!"
echo "----------------------------"
echo ""
echo "This script will remove from your server:"
echo "     - freepbx and asterisk cdr MySQL databases"
echo "     - freepbx MySQL User"
echo "     - freepbx DB entries (freepbx, httpd-fpbx and dahdi)"
echo "     - /opt/freepbx"
echo ""
echo -n "Are you sure you want to remove FreePBX permanently ? (y/n) [n] "
read confirm
if [ "$confirm" = "y" -o "$confirm" = "Y" ]; then
	echo "Droping MySQL databases..."
	DBNAME=$(/sbin/e-smith/db configuration getprop freepbx DbName)
	CDRDBNAME=$(/sbin/e-smith/db configuration getprop freepbx CdrDbName)
	mysql -e "DROP DATABASE $DBNAME"
	mysql -e "DROP DATABASE $CDRDBNAME"
	echo "Deleting MySQL User..."
	DBUSER=$(/sbin/e-smith/db configuration getprop freepbx DbUser)
	mysql -u root -e "REVOKE ALL PRIVILEGES ON *.* FROM '$DBUSER'@'localhost';"
	mysql -u root -e "DROP USER '$DBUSER'@'localhost';" > /dev/null 2>&1
	echo "Removing SME DB entries..."
	/sbin/e-smith/db configuration delete freepbx
	/sbin/e-smith/db configuration delete httpd-fpbx
	/sbin/e-smith/db configuration delete dahdi
	echo "Removing /opt/freepbx ..."
	rm -rf /opt/freepbx
	echo "Removing this script ..."
	rm -f /root/uninstall-freepbx.sh
	echo "Done!"
fi

