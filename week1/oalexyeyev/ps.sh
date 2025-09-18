sudo apt update
sudo apt install postgresql
sudo -i -u postgres psql -f /opt/init.sql

sudo sed -i "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/14/main/postgresql.conf
sudo sed -i '$a host    all             all             192.168.56.0/24         md5' /etc/postgresql/14/main/pg_hba.conf
sudo systemctl restart postgresql
