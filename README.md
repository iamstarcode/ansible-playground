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

to copy files
scp -r ./ osboxes@192.168.8.101:helloworld
