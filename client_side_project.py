from SshToServer import SshToServer
import pandas as pd
import os
import ast

def appendToCsv(file_path, data): #ייצוא מילון לcsv
    df_new = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_csv(file_path, index=False)
    print("The data was saved successfully in " + file_path)


my_ssh = SshToServer(r"C:\Users\Tehila\Desktop\Easy High-Tech\טכנולוגיות ענן\linux\my-key-pair.pem", "13.53.131.237", "ubuntu")
stdout, stderr = my_ssh.runRemoteCommand("python3 /home/ubuntu/final_project/server_side_project.py") #dict
stdout_dict = ast.literal_eval(stdout)
# print(stdout_dict) 
# print(type(stdout_dict))
appendToCsv(r"C:\Users\Tehila\Desktop\Easy High-Tech\טכנולוגיות ענן\linux\severity_statistic.csv", stdout_dict)