# Bringing server traffic limit higher 

# Increase ULIMIT of the default file from 15 to 3000
exec { 'up_traffic':
  command =>'sed -i "s/15/3000/" /etc/default/nginx',
  path    =>'/usr/local/bin/:/usr/sbin/:/bin/'
}

-> exec { 'restart-nginx':
  command =>'nginx restart',
  path    =>'/etc/init.d/'
}
