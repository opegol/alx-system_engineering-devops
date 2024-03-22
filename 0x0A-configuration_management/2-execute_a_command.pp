# This manifest kills a process named killmenow

exec { 'exc pkill':
  command => 'pkill -f killmenow',
  path    => [ '/bin/usr/', '/usr/local/bin/', '/bin/']
}
