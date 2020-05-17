import SSHFunctions_UCM
from SSHFunctions_UCM import ChangeUsername
from SSHFunctions_UCM import ChangeAppPassword_interact
from SSHFunctions_UCM import ShowCommands
from SSHFunctions_UCM import ChangePlatformPw
import json
from pprint import pprint


def main():
    global data
    global pwd

    # open Json file of - passwords / pending task: encrypt this
    with open("Jsonfiles/password.json") as f:
        pwd = json.load(f)
    for password in pwd['Passwords']:
        APACPwd = pwd['Passwords'][
            'Apac']  # set the variable of the password (take note the var name as this will be used in task functions)
        TestPwd = pwd['Passwords']['TestCluster']

    # open Json file of cluster inventory/ add the other clusters here
    with open("Jsonfiles/inventory.json") as f:
        data = json.load(f)
    for clusters in data['Clusters']:
        if 'Test' in clusters:  # take note this if statement is required to capture all the data inside the Json file // clusters is the variable representing the json file
            TestClusterNodes = clusters['Test']['nodes']  # set variable of Nodes
            TestClusterPub = clusters['Test']['Publisher']  # set variable of Publisher
            TestClusterUname = clusters['Test']['Username']  # set variable of Uname
        if 'APAC' in clusters:
            APACClusterPub = clusters['APAC']['Publisher']
            APAClusterNodes = clusters['APAC']['nodes']
            APACClusterUname = clusters['APAC']['Username']

    #####################################start of program
    # Add the succedding clusters to CLuster Choice - This part is to display the cluster options
    ClusterChoice = ["1. APAC Cluster", "2. Test Cluster", "3. Argentina Cluster", "4. Houston Cluster"]
    for Cluster in ClusterChoice:  # display the clusters
        print(Cluster)
    clusterchoice = input("Please select the Cluster: ")
    counter = int(clusterchoice) - 1
    print(f"You have selected {ClusterChoice[counter]}")  # this is only for display the Selected CLuster name
    print("\n")

    # IF statement -- this will help set the correct cluster information(IP ADDRESS, USERNAME) depending on the cluster choice
    if clusterchoice == "1":  # setting the variable depending on the requested cluster
        ClusterPub = APACClusterPub
        ClusterPass = APACPwd
        CLusterUsername = APACClusterUname
        ClusterNodes = APAClusterNodes
        ClusterTasks(clusterchoice, ClusterPub, ClusterPass, CLusterUsername,
                     ClusterNodes)  # call the function for available tasks
    elif clusterchoice == "2":  # setting the variable depending on the requested cluster
        ClusterPub = TestClusterPub
        ClusterPass = TestPwd
        CLusterUsername = TestClusterUname
        ClusterNodes = TestClusterNodes
        ClusterTasks(clusterchoice, ClusterPub, ClusterPass, CLusterUsername,
                     ClusterNodes)  # call the function for available tasks


def ClusterTasks(clusterchoice, ClusterPub, ClusterPass, CLusterUsername, ClusterNodes):
    counterTest = len(ClusterNodes) - 1  # lenght of nodes in the inventory file
    counter = 0

    AvailableTasks = ['0. Cluster Information', '1. Change Admin Name', '2. Change Admin Password', '3. Show Commands',
                      '4. Change Platform Password']
    print("Available Tasks: Select the corresponding number.. Please..")

    # Display the Available Tasks
    for tasks in AvailableTasks:  # display the available tasks
        print(tasks)
    command = input("Select Action to Perform: ")

    # Display the Cluster information if '0. Cluster Information' i selected (this came from the json inventory file)
    if command == "0":
        if clusterchoice == "1":
            for clusters in data['Clusters']:
                if 'APAC' in clusters:
                    pprint(clusters['APAC'], indent=2)
                    print("\n")
                    main()  # go back to main function after the task is performed
        elif clusterchoice == "2":
            for clusters in data['Clusters']:
                if 'Test' in clusters:
                    pprint(clusters['Test'], indent=2)
                    print("\n")
                    main()

    # if '1. Change Admin Name' is selected call "ChangeUsername Function" . This function is available at SSHFunctions_UCM.py file
    elif command == "1":
        Username = input("Please Enter the New Username: ")  # enter new username
        command = "utils reset_application_ui_administrator_name"
        ChangeUsername(ClusterPub, CLusterUsername, ClusterPass, command, Username)
        print("\n")
        main()

    # if '2. Change App Password' is selected call "ChangeAppPassword_interact Function" . This function is available at SSHFunctions_UCM.py file
    elif command == "2":
        appPassword = input("Please Enter the New Password: ")
        confirmation = input("Are you sure you want to change the password: ")
        if confirmation == "yes":
            command = "utils reset_application_ui_administrator_password"
            ChangeAppPassword_interact(ClusterPub, CLusterUsername, ClusterPass, command, appPassword)
            print("\n")
            main()
        else:
            print("Returning to the Main Prompt: \n Unsuccessful attempt due to no confirmation")
            print("\n")
            main()


    elif command == "3":
        showcom = input("Please enter the show command: ")
        command = showcom
        a = ShowCommands(ClusterPub, CLusterUsername, ClusterPass, command)
        print("\n")
        main()

    # if '4. Change Platform Password' is selected call "ChangePlatformPw Function" . This function is available at SSHFunctions_UCM.py file
    elif command == "4":
        NewPlatPw = input("Please Enter the New Platform Password: ")
        confirmation = input("Are you sure you want to change the password: ")
        if confirmation == "yes":
            command = "set password user admin"
            while counter <= counterTest:  # counterTest determines the number of nodes, the while loop--loop to all nodes to perfrom the change pw
                ChangePlatformPw(ClusterNodes[counter], CLusterUsername, ClusterPass, NewPlatPw, command)
                counter = counter + 1
            print("\n")

        else:
            main()


if __name__ == "__main__":
    main()
