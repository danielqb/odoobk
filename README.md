# odoobk
Script to make odoo zip backups (includes filestore) in console

#you need copy the file in you prefer location
cp odoobk.py /usr/bin/

#change permissions to execute
chmod +x /usr/bin/odoobk.py

#and program cron task
0 23 * * 1 python /usr/bin/odoobk.py >> /var/log/odoo/odoo-bkup.log
