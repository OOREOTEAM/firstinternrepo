#!/bin/bash



echo "
upstream backend {
        server 192.168.0.21;
        server 192.168.0.22;
    }

    server {
        listen      80;
        server_name 192.168.0.20;

        location / {
	        proxy_redirect      off;
	        proxy_set_header    X-Real-IP $remote_addr;
	        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
	        proxy_set_header    Host $http_host;
		proxy_pass http://backend;
	}
}


" >> /etc/nginx/conf.d/loadbalancer.conf


