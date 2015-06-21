# $Id: smeserver-freepbx.spec,v 1.2 2013/05/12 21:04:00 unnilennium Exp $
# Authority: vip-ire
# Name: Daniel Berteaud

#%define fpbxversion 2.5.0
%define version	0.1
%define release 34
%define name smeserver-freepbx

Summary: Asterisk web GUI
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System/Servers
Source: %{name}-%{version}.tar.gz


BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
URL: http://www.freepbx.org/

BuildRequires:	e-smith-devtools
BuildRequires:	tar

Requires: mysql
Requires: httpd
Requires: php-pear
Requires: /usr/sbin/asterisk
Requires: %{_libdir}/asterisk/modules/app_addon_sql_mysql.so
Requires: dahdi-tools
Requires: dahdi-linux
Requires: sox
Requires: mod_auth_tkt
Requires: e-smith-base
Requires: freepbx-src
Requires: iksemel speex spandsp asterisk asterisk-mysql asterisk-sounds-core-en-ulaw php-posix asterisk-calendar asterisk-fax asterisk-jabber asterisk-ldap asterisk-snmp asterisk-voicemail
#Buildarch: noarch
AutoReqProv: no


%description
FreePBX is a Standardised Implementation of Asterisk that gives you a GUI to manage your system. If you have looked into Asterisk, you would know that it does not come with any built in programming. You cannot plug a phone into it and make it work without editing configuration files, writing dialplans, and various messing about. FreePBX simplifies this by giving you a pre-written set of dialplans that allow you to have a fully functional PBX pretty much straight away.
This package provide the integration of FreePBX on SME Server.


%changelogi
* Sun Jun 21 2015 stephane de labrusse <stephdl@de-labrusse.fr> 0.1-34.sme
- first release to sme9
- script and credits to Hsing-Foo Wang hsingfoo@gmail.com

* Sun May 12 2013 JP Pialasse <tests@pialasse.com> 0.1-33.sme
- buildarch removed in order to find the correct %{_libdir}/asterisk/modules/app_addon_sql_mysql.so 

* Thu Oct 20 2011 Daniel B. <daniel@firewall-services.com> 0.1-32.sme
- Protect by locations (so other alias can be defined to protect with LL::NG for example)

* Mon Oct 17 2011 Daniel B. <daniel@firewall-services.com> 0.1-31.sme
- Add misdn.log to logrotate

* Thu Oct 13 2011 Daniel B. <daniel@firewall-services.com> 0.1-30.sme
- Change session path [SME: 6661]

* Wed Jan 05 2011 Daniel B. <daniel@firewall-services.com> 0.1-29.sme
- astdatadir is /var/lib/asterisk
- templates for /etc/logrotate.d/asterisk

* Mon Sep 20 2010 Daniel B. <daniel@firewall-services.com> 0.1-28.sme
- Create and populate the mysql databases in mysql.init
- Templates for /etc/asterisk/asterisk.conf

* Thu Jul 15 2010 Daniel B. <daniel@firewall-services.com> [0.1-27]
- Read ARI password from the DB (and initialize a random one)

* Mon Feb 22 2010 Daniel B. <daniel@firewall-services.com> [0.1-26]
- Remove hard-coded dependencies on asterisk and asterisk-addons14
  Depends now on asterisk binary and app_addon_sql_mysql.so files
  (so it can work with asterisk or asterisk14)

* Mon Feb 15 2010 Daniel B. <daniel@firewall-services.com> [0.1-25]
- Remove /etc/logrotate.d/asterisk which is now included in asterisk14

* Tue Feb 09 2010 Daniel B. <daniel@firewall-services.com> [0.1-24]
- Depends now on asterisk14 and asterisk-addons14

* Wed Jan 06 2010 Daniel B. <daniel@firewall-services.com> [0.1-23]
- disable dynamic hints

* Tue Oct 06 2009 Daniel B. <daniel@firewall-services.com> [0.1-22]
- include /opt/freepbx/admin/functions.inc.php in freepbx-dump-astdb
  action script for FreePBX 2.6 compatibility

* Tue May 19 2009 Daniel B. <daniel@firewall-services.com> [0.1-21]
- Add CHECKREFERER=FALSE in amportal.conf to repvent error message in some 
  modules (due to the ProxyPass configuration)

* Tue Apr 28 2009 Daniel B. <daniel@firewall-services.com> [0.1-20]
- Fix CDR db password in cdr_mysql.conf template
- Use a separate service in SME db for FOP

* Thu Apr 16 2009 Daniel B. <daniel@firewall-services.com> [0.1-19]
- remove scoreboard directive from httpd-fpbx config
- remove some modules (mod_ssl, mod_proxy)

* Sat Apr 11 2009 Daniel B. <daniel@firewall-services.com> [0.1-18]
- templatize cdr_mysql.conf [SME: 5153]
- templatize manager.conf
- remove freepbx-cron-scheduler.php from root crontab so only
  asterisk user runs it (prevent email error sent from cron)

* Fri Mar 27 2009 Daniel B. <daniel@firewall-services.com> [0.1-17]
- Remove obsolete /admin Alias from apache
- Run the security script on bootsrape-console-save event

* Mon Mar 23 2009 Daniel B. <daniel@firewall-services.com> [0.1-16]
- Security Fixe: put a random password for ARI admin (this should be documented)

* Thu Mar 19 2009 Daniel B. <daniel@firewall-services.com> [0.1-15]
- Check if /opt/freepbx/admin exists (retry the install if a first one failed)
- Remove tabs from spec

* Wed Mar 18 2009 Daniel B. <daniel@firewall-services.com> [0.1-14]
- Remove speex from dependencies

* Thu Mar 12 2009 Daniel B. <daniel@firewall-services.com> [0.1-13]
- Remove zaptel dependency, replaced with dahdi-tools and dahdi-linux

* Mon Feb 23 2009 Daniel B. <daniel@firewall-services.com> [0.1-12]
- Fix logrotate issue (send a sigusr1 signal to httpd-fpbx)

* Thu Feb 12 2009 Daniel B. <daniel@firewall-services.com> [0.1-11]
- Full support for the new DAHDI driver, droping zaptel

* Mon Feb 09 2009 Daniel B. <daniel@firewall-services.com> [0.1-10]
- add support for DAHDI channel

* Mon Dec 08 2008 Daniel B. <daniel@firewall-services.com> [0.1-9]
- move expand-templates from post-upgrade event to bootstrap-console-save

* Thu Nov 27 2008 Daniel B. <daniel@firewall-services.com> [0.1-8]
- Add support for trunk name in mail alerts

* Wed Nov 26 2008 Daniel B. <daniel@firewall-services.com> [0.1-7]
- Add a simple script to alert admin by mail on trunk errors

* Thu Nov 20 2008 Daniel B. <daniel@firewall-services.com> [0.1-6]
- Use AdminPanels props so access can be configured using 
  smeserver-userpanels contrib. AdminUsers and FopUsers 
  props aren't used anymore

* Wed Nov 19 2008 Daniel B. <daniel@firewall-services.com> [0.1-5]
- add logrotate default config file for asterisk's logs
- spec cleanup

* Thu Nov 13 2008 Daniel B. <daniel@firewall-services.com> [0.1-4]
- fix logrotate issue

* Wed Nov 05 2008 Daniel B. <daniel@firewall-services.com> [0.1-3]
- split freepbx sources in a separate package (freepbx-src)
- alternative genzaptelconf

* Mon Oct 13 2008 Daniel B. <daniel@firewall-services.com> [0.1-2]
- Fix fop not being displayed in admin page

* Sat Sep 20 2008 Daniel B. <daniel@firewall-services.com> [0.1-1]
- updated to 2.5.0 final
- spec cleaning
- templates cleaning
- templates to update mysql informations

* Mon Aug 04 2008 daniel B. <daniel@firewall-services.com> [0.1-0]
- initial release

%prep

%setup -q -n %{name}-%{version}

%build
# Build symlinks
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT/var/lib/php/fpbx-session

(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	--file /usr/share/freepbx/scripts/uninstall.sh 'attr(0750,root,root)' \
	--file /usr/share/freepbx/scripts/restore-astdb.php 'attr(0750,root,root)' \
	--dir /var/service/httpd-fpbx 'attr(01755,root,root)' \
	--dir /var/service/httpd-fpbx/supervise 'attr(0700,root,root)' \
	--dir /var/service/httpd-fpbx/log 'attr(0755,root,root)' \
	--file /var/service/httpd-fpbx/log/run 'attr(0755,root,root)' \
	--dir /var/service/httpd-fpbx/log/supervise 'attr(0700,root,root)' \
	--dir /var/log/httpd-fpbx 'attr(0750,smelog,smelog)' \
	--file /var/lib/asterisk/bin/genzaptelconf 'attr(0750,root,root)' \
	--file /var/lib/asterisk/agi-bin/trunk_alert_mail.agi 'attr(0750,asterisk,asterisk)' \
	--file /etc/logrotate.d/asterisk 'config(noreplace)' \
        --dir /var/lib/php/fpbx-session 'attr(0770,root,asterisk)' \
	 > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)


%post
	echo "Get the additional sound files, unpack and symlink to /var/lib/asterisk/sounds/en. Then remove the tgz archive"
	wget -P /usr/share/asterisk/sounds http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz
	tar zxvf /usr/share/asterisk/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz -C /usr/share/asterisk/sounds
	rm -f /usr/share/asterisk/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz
	#
	# create a symbolic link to the sounds directory, still need to find out why /etc/asterisk/asterisk.conf astdatadir is not working
	# changed the template so astdatadir is now set to /usr.share/asterisk. What's the difference if any?
	ln -sfn /usr/share/asterisk/sounds/ /var/lib/asterisk/sounds/en
#
# Done with the easy bit...
#
echo "Download and install FreePBX (The hugely hacky way for the time being)"
#Create the install directory, and make sure there is no old version for the script will stop
FREEPBX_VERSION="2.11.0.38"
mkdir -p /usr/share/freepbx/sources
rm -f /usr/share/freepbx/sources/freepbx-$FREEPBX_VERSION.tgz

# Change FreePBX database settings that should have come from /etc/amportal.conf, but that needs a new e-smith template for FreePBX > 1.9
FPBX_SETTING_PATH="/var/lib/asterisk/bin/freepbx_setting"
$FPBX_SETTING_PATH DISABLE_CSS_AUTOGEN 1
$FPBX_SETTING_PATH CHECKREFERER 0
$FPBX_SETTING_PATH AUTHTYPE none
$FPBX_SETTING_PATH AMPEXTENSIONS deviceanduser
$FPBX_SETTING_PATH AMPWEBROOT /opt/freepbx
$FPBX_SETTING_PATH MODULEADMINWGET 1
$FPBX_SETTING_PATH DYNAMICHINTS 1
$FPBX_SETTING_PATH ARI_ADMIN_PASSWORD $(/sbin/e-smith/db configuration getprop freepbx AriPassword)
$FPBX_SETTING_PATH AMPMGRPASS $(/sbin/e-smith/db configuration getprop freepbx ManagerPassword)
#
#remove the default asterisk config files and replace them with symbolic links to FreePBX's own config files
CONF_FILES=(features.conf iax.conf logger.conf sip.conf sip_notify.conf ccss.conf extensions.conf confbridge.conf)
for symlink in "${CONF_FILES[@]}"
do
	rm -f /etc/asterisk/$symlink
	ln -s /opt/freepbx/admin/modules/core/etc/$symlink /etc/asterisk/$symlink 
done
ln -sfn /opt/freepbx/admin/modules/cdr/etc/cel.conf /etc/asterisk/cel.conf
ln -sfn /opt/freepbx/admin/modules/cdr/etc/cel_odbc.conf /etc/asterisk/cel_odbc.conf
touch /etc/asterisk/cel_general_additional.conf
touch /etc/asterisk/cel_general_custom.conf
touch /etc/asterisk/cel_custom_post.conf
#
echo "Download and install most of the FreePBX modules."
# -f forces modules to install ignoring dependencies. There are dependencies, but all are satisfied with this list."
ALL_MODULES=(recordings framework findmefollow directory donotdisturb parking queues ringgroups setcid timeconditions vmblast printextensions weakpasswords fax iaxsettings outroutemsg pinsets manager customappsreg userman daynight pbdirectory phonebook dictate disa miscapps miscdests phpinfo queueprio speeddial contactdir customcontexts extensionsettings languages paging restart ivr backup accountcodepreserve presencestate announcement bulkdids bulkextensions callback callforward callwaiting conferences asteriskinfo campon hotelwakeup asterisk-cli blacklist cidlookup endpointman)
for fpbx_module in "${ALL_MODULES[@]}"
do
	sudo -u asterisk /var/lib/asterisk/bin/module_admin -f --repos standard,extended,unsupported upgrade $fpbx_module
done
sudo -u asterisk /var/lib/asterisk/bin/retrieve_conf
sudo -u asterisk /var/lib/asterisk/bin/module_admin reload
#Fix chattr issue
# /var/lib/asterisk/bin/freepbx_engine line 296 (about). change from chattr -i $AMPWEBROOT/*  2>&1 >/dev/null to chattr -i $AMPWEBROOT/* 2>/dev/null   !!!!Not working from the script but does work from the command line. WHY??
sed -i 's/2>&1/2/g' /var/lib/asterisk/bin/freepbx_engine


%preun
if [ $1 = 0 ] ; then
  /etc/rc.d/init.d/freepbx stop >& /dev/null || :
fi

true

