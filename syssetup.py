# Imports.
import os

try:# clear CLI.
    os.system("clear")
    # Program.
    print("Now running requirements installer:\n")
    os.system("pip install -r requirements.txt")
    print("\nNow running update and packages installer:\n")
    os.system("sudo apt-get install update -y && sudo apt-get install upgrade -y")
    os.system("sudo apt-get install htop ncdu neofetch libimage-exiftool-perl samba neofetch git steghide -y")
    os.system("sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y")
    os.system("sudo apt-get install cockpit cockpit-machines cockpit-networkmanager -y")
    os.system("sudo apt-get install tor tripwire nmap -y")
    os.system("sudo apt install hashcat -y")
    os.system("sudo apt install hashcat-utils -y ")
    os.system("sudo apt install hashcat-nvidia -y")
    os.system("sudo apt-get install airmon-ng airodump-ng aireplay-ng airdecap-ng aircrack-ng -y ")
    print("\n[!] THIS IS NOW A HEADLESS INSTALLATION\n")
    os.system("git clone https://github.com/Nyr/openvpn-install.git")
    os.system("git clone https://github.com/KuroLabs/stegcloak.git")
    os.system("git clone https://github.com/SSGorg/Cryptex.git")
    os.system("git clone https://github.com/ItsJustShepherd/LOKI.git")
    os.system("git clone https://github.com/sherlock-project/sherlock.git")
    os.system("git clone https://github.com/AzizKpln/Moriarty-Project")
    os.system("git clone https://github.com/laramies/theHarvester")
    os.system("git clone https://github.com/lanmaster53/recon-ng.git")
    print("\nSetting up ufw:\n")
    os.system("sudo apt install ufw")
    os.system('sudo ufw allow 245 comment "SSH" && sudo ufw deny 4444 comment "Revshell" && sudo ufw allow 81 comment "NPM" && sudo ufw allow 23045 comment "OVPN" && sudo ufw allow 9090 comment "Cockpit" && sudo ufw allow 9000 comment "Portainer" && sudo ufw allow 20450 comment "askerheim"  && sudo ufw allow 19823 comment "45k3rh31m"  && sudo ufw allow 12750 comment "Nextcloud" && sudo ufw allow 62584 comment "SearXNG" && sudo ufw allow samba comment "SMB"')
    os.system("sudo ufw enable")
    print("\nInstalling fail2ban and clamAV:\n")
    os.system("sudo apt install fail2ban clamav clamav-daemon -y")
    print("\nSetting hostname:\n")
    os.system("sudo hostnamectl set-hostname bfx2")
    print("\nSetting user and quotas:\n")
    os.system("sudo apt-get install quota -y")
    os.system("sudo useradd -m shepherd")
    print("\n")
    print("\nStill needing configuration after reboot:\n[!] 'shepherd' user requires password setting.\n[!] fail2ban needs configuration.\n[!] quota needs setting.\n[!] SSH default port needs setting.\n[!] .bashrc needs configuration.\n[!] cronjob needs configuration.")
    option = input("Would you like to restart now [Y/n]: ")
    if option == "y" or option == "Y":
        os.system("reboot")
    if option == "n" or option == "N":
        print("\n [!] Reboot expected before full operation!\n")
except KeyboardInterrupt:
    print("\n") # Gaps the print.
    print("Exited successfully but system may not be fully set up.") # States the script ended.
    print("\n") # Gaps the print.
    print('[>>] You interrupted the program.') # States it was interrupted.
    print("\n") # Gaps the print.
    try:
        sys.exit(0) # Attempts to exit.
    except SystemExit:
        os._exit(0) # Attempts to exit.