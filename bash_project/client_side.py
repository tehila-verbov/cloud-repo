from SshToServer import SshToServer

my_ssh = SshToServer(r"C:\Users\Tehila\Desktop\Easy High-Tech\טכנולוגיות ענן\linux\my-key-pair.pem", "13.53.131.237", "ubuntu")

file_name = input("Please enter the name of the file: ")
seconds = input("How many second to wait? ")

command = "bash /home/ubuntu/final_project_bash/server_side_bash_pro.sh " + file_name + " " + seconds

result = my_ssh.runRemoteCommand(command)
print(result[0])