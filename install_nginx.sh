#!/bin/bash

sudo apt update -y
sudo apt install nginx -y

if systemctl is-active nginx;
then 
	echo " "
else
	systemctl start nginx
fi


cd /var/www/html
sudo wget -O bird.jpg "https://www.pennington.com/-/media/Project/OneWeb/Pennington/Images/headers/secondary-category/About_WildBird-mobile.jpg?h=330&iar=0&w=480&hash=85A6611B4C76F416ED8CF1BE1FC2BA0E"

sudo cat > index.nginx-debian.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<img src="bird.jpg" alt="Bird">
<p> Lviv, Ukraine </p>
</body>
</html>
EOF
