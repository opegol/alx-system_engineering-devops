# Make it possible to login with 'holberton' user and open a file without any error message.

exec { 'up_hard_file_limit':
  command =>'sed -i "/holberton hard/s/5/55000/" /etc/security/limits.conf',
  path    =>'/usr/local/bin/:/usr/sbin/:/bin/'
}

exec { 'up_soft_file_limit':
  command =>'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    =>'/usr/local/bin/:/usr/sbin/:/bin/'
}
