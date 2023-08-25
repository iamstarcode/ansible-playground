--
to create key
first cretae a key using keygen
ssh-keygen -t rsa

create a .pem file from the private key generated
cp -p id_rsa key.pem

and copy to the host machine
ssh-copy-id -i id_rsa.pub osboxes@192.168.8.103
[will prompt for password]

first copy id
ssh-copy-id osboxes@192.168.8.101
to copy files
scp -r ./ osboxes@192.168.8.101:helloworld
