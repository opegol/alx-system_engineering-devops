# Install and configure an Nginx server using Puppet

$str = "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://google.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}"

$str2 = '> /etc/nginx/sites-available/default'


# Update package repositories
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin'],
}

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create directory and index.html file
file { '/etc/nginx/html':
  ensure => directory,
}

file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Configure Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $str,
  notify  => Service['nginx'],
}

exec { 'append':
  command => 'echo $str2 >> /etc/nginx/sites-available/default'
}

# Restart Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
