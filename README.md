--
Nav to ssh folder
cd ~/.ssh

to create key
first cretae a key using keygen
ssh-keygen -t rsa

first copy id to the host machine
ssh-copy-id osboxes@192.168.8.101

then try to ping your targets
ansible target -m ping -i inventory.txt

variable passing
in inventory file value=5
inline -e "value=5"
using var-files array
and you can use vars_prompt

use COPY, FILE
