import paramiko

# Define a list of dictionaries containing SSH credentials for each client
clients = [
    {'hostname': '192.168.1.1', 'port': 22, 'username': 'user1', 'password': 'password1'},
    {'hostname': '192.168.1.2', 'port': 22, 'username': 'user2', 'password': 'password2'},
    # Add more clients as needed
]

# Iterate over the list of clients
for client in clients:
    try:
        # Establish SSH connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(client['hostname'], client['port'], client['username'], client['password'])

        # Execute commands or perform actions here
        # For example:
        stdin, stdout, stderr = ssh_client.exec_command('ls -l')
        print(f"Output for {client['hostname']}:")
        print(stdout.read().decode())

    except Exception as e:
        print(f"Error connecting to {client['hostname']}: {e}")

    finally:
        # Close the SSH connection
        ssh_client.close()
