install:
	@sudo apt update && sudo apt install --yes ansible
	ansible-playbook --connection=local --inventory 127.0.0.1, install.yml
	@echo -n "Tor address: "; sudo cat /var/lib/tor/server/hostname
	@echo
