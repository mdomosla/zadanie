import paramiko


class FileReader:

    @staticmethod
    def readfile(server_addres):
        client = paramiko.SSHClient().open_sftp()
        file = client.open(server_addres + '/root/users.txt')
        lines = file.readlines()
        file.close()
        result = []
        for i in lines:
            i = i.replace('\n', '')
            result.append(i)
        return result
