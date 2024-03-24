# Editing ssh config file using puppet

file_line { 'id_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'no_psw':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^#\s*PasswordAuthentication\s[a-z]*'
}
