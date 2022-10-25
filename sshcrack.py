#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

ssh.load_system_host_keys()

try:
	ssh.connect(hostname = '172.16.1.5', username='root', password='root')

except paramiko.ssh_exception.AuthenticationException:
	print('Testando a senha root')

else:
	print('[+] Acesso Garantido => root')
