import paramiko

class SSH:
    """SSHԶ������"""

    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def shell_cmd(self, cmd):
        """ִ��shell����"""
        try:
            # ����SSH����
            ssh = paramiko.SSHClient()
            # ��Զ�̷����������ӽ�������         �Զ���Ӳ���
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            # ��������
            ssh.connect(
                self.ip,
                self.port,
                self.username,
                self.password,
                timeout=5
            )
            # ִ��shall����
            # ��׼���� ��׼��� ������
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # ��ȡ������
            content = stdout.read().decode('utf-8')
            # ���صĽ�����л��з���ͨ��\n���зָ�
            res = content.split(r'\n')
            # �ر�����
            ssh.close()
            return res
        except Exception as e:
            print('Զ��ִ��shell����ʧ��')
            return False


    def shell_upload(self, localpath, remotepath):
        """�ϴ��ļ�"""
        try:
            # 1.ʵ����һ��transport����      ��Ҫ��һ��Ԫ����� ip�Ͷ˿ں�
            transport = paramiko.Transport((self.ip, self.port))
            # 2.��Զ�˵ķ���������һ��SSH����
            # �����û�������
            transport.connect(username=self.username, password=self.password)
            # 3.�ϴ��ļ�
            # ʹ��paramiko�е�SFTPClient������е�from_transport����
            # ����һ��������� ��������ʵ������transport����
            # �᷵��һ��SFTP����
            sftp = paramiko.SFTPClient.from_transport(transport)
            # ����PUT����ʵ���ϴ�
            # ���������� ��һ���Ǳ��������ļ�·�����ڶ����Ƿ��������ļ�·��
            sftp.put(localpath, remotepath)
            # 4.�ر�����
            transport.close()
            print('�ļ��ϴ��ɹ����ϴ�����{}'.format(remotepath))
            return True
        except Exception as e:
            print('�ļ��ϴ�ʧ��')
            return False

    def shell_download(self, localpath, remotepath):
        """�����ļ�"""
        try:
            # 1.ʵ����һ��transport����      ��Ҫ��һ��Ԫ����� ip�Ͷ˿ں�
            transport = paramiko.Transport((self.ip, self.port))
            # 2.��Զ�˵ķ���������һ��SSH����
            # �����û�������
            transport.connect(username=self.username, password=self.password)
            # 3.�ϴ��ļ�
            # ʹ��paramiko�е�SFTPClient������е�from_transport����
            # ����һ��������� ��������ʵ������transport����
            # �᷵��һ��SFTP����
            sftp = paramiko.SFTPClient.from_transport(transport)
            # ����PUT����ʵ���ϴ�
            # ���������� ��һ���Ǳ��������ļ�·�����ڶ����Ƿ��������ļ�·��
            sftp.get(remotepath, localpath)
            # 4.�ر�����
            transport.close()
            print('�ļ����سɹ�����������{}'.format(localpath))
            return True
        except Exception as e:
            print('�ļ����� ʧ��')
            return False


