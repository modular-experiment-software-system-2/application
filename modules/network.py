
from paramiko import SSHClient, AutoAddPolicy
import platform
from scp import SCPClient
import subprocess
import os
import signal


class SSH():
    """
    Manages SSH connections to clients on a static network.
    """
    def __init__(self):
        """
        Initializes the SSH client and load's the system host keys.
        """
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())

        self.status_ssh: bool = False

    
    def __del__(self):
        """
        Safely closes the SSH connection when the SSH class instance is destroyed.
        """
        self.disconnect()


    def connect(self, hostname: str, username: str, password: str, port: int = -1):
        """
        Establishes an SSH connection with a remote host.

        @return: True if SSH connection established, False otherwise.
        """
        try:
            if port == -1:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password
                )
            else:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password,
                    port=port
                )
            return True
        except Exception as e:
            return False


    def disconnect(self):
        """
        Closes an SSH connection with a remote host.

        @return: True if closed SSH connection, False otherwise.
        """
        try:
            if self.ssh:
                self.ssh.close()
                return True
            else:
                return False
        except Exception as e:
            return False
    

    def status(self):
        """
        Checks if the SSH connection is active.
        """
        try:
            if self.ssh.get_transport() == None:
                return False
            return True
        except Exception as e:
            return False


class SCP(SSH):
    """
    Manages SCP file transfers with a client on a static network.
    """
    def __init__(self):
        """
        """
        SSH.__init__(self)


    def upload(self, local_path: str, remote_path: str):
        """
        Uploads a file or directory from a local path to a client at a remote path.
        """
        try:
            if not self.status():
                self.ssh.connect()
            scp = SCPClient(self.ssh.get_transport())
            scp.put(
                files=local_path,
                remote_path=remote_path,
                recursive=True
            )
            scp.close()
            return True
        except Exception as e:
            return False
    

    def download(self, local_path: str, remote_path: str):
        """
        Downloads a file or directory to a local path from a client at a remote path.
        """
        try:
            if not self.status():
                self.ssh.connect()
            scp = SCPClient(self.ssh.get_transport())
            scp.get(
                remote_path=remote_path,
                local_path=local_path,
                recursive=True
            )
            scp.close()
            return True
        except Exception as e:
            return False


class ROS2Local():
    """
    Manages ROS2 command launching and shutdown on a local device. 
    """
    def start(self, device):
        """
        Launches the command processes on the local device.
        """
        for command in device.commands:
            command_ = command.split()
            process = subprocess.Popen(command_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)
            device.logger.log(f"started pid {process.pid} on {device.name} \"{command}\"")
            device.processes.append(process)



    def stop(self, device):
        """
        Shuts down the command processes on the local device.
        """
        removable = []
        for process in device.processes:
            os.killpg(process.pid, signal.SIGTERM)
            device.logger.log(f"stopped pid {process.pid} on {device.name}")
            removable.append(process)
        for process in removable:
            device.processes.remove(process)


class ROS2Remote():
    """
    Manages ROS2 command launching and shutdown on a remote device. 
    """
    def start(self, device):
        """
        Launches the command processes on the remote device.
        """
        if not device.network.status():
            device.logger.log(f"unable to execute commands on {device.name}")
            return
        for command in device.commands:
            stdin, stdout, stderr = device.network.ssh.exec_command(f"nohup zsh -c 'source ~/.zshrc && {command} > /dev/null 2>&1' & echo $!", get_pty=False)
            pid = stdout.read().decode().strip()
            device.logger.log(f"started pid {pid} on {device.name}\"{command} \"")
            device.pids.append(pid)


    def stop(self, device):
        """
        Shuts down the command processes on the remote device.
        """
        if not device.network.status():
            device.logger.log(f"unable to execute commands on {device.name}")
            return
        removable = []
        for pid in device.pids:
            device.network.ssh.exec_command(f"pgrep -P {pid} | xargs kill -9")
            device.logger.log(f"stopped pid {pid} on {device.name}")
            removable.append(pid)
        for pid in removable:
            device.pids.remove(pid)


class NetworkFunctions(SCP):
    """
    Manages method's and attributes relating to network protocols.
    """
    def __init__(self):
        """
        Initializes the network functions.
        """
        SCP.__init__(self)
        self.status_network: bool = None
        self.local = ROS2Local()
        self.remote = ROS2Remote()


    def ping(self, ip: str, timeout: float = 3):
        """
        Pings a static IP address on a local network to determine whether the device with that IP is online.
        """
        if ip != None:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            try:
                response = subprocess.run(
                    ["ping", param, "1", ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=3
                )
                if response.returncode == 0:
                    return True
                else:
                    return False
            except Exception as e:
                return False
