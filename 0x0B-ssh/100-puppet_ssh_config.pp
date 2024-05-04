#setting up my client config file

file_line { 'Disable passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentification no',
  match => '^@PasswordAuthentification',
}

file_line { 'Identity File':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^@IdentityFile',
}
