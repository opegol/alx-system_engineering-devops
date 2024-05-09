# Using puppet to automate the the process of fixing the
# issue with why Apache is returning a 500 error.

exec { 'fix-wordpress':
  command =>'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    =>'/usr/local/bin/:/usr/sbin/:/bin/'
}
