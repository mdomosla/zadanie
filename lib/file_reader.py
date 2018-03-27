import paramiko


class FileReader:

    @staticmethod
    def readfile(server_addres):
        client = paramiko.SSHClient().open_sftp()
        file = client.open(server_addres + '/root/users.txt')
        user_names = []
        for line in file:
            user_names.append(line)
        file.close()
        return user_names
