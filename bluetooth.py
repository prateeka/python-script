import subprocess


def exec(cmd, msg):
    retval = subprocess.run(cmd, shell=True)
    assert retval.returncode == 0, msg


start = "sudo -S systemctl start bluetooth"
exec(start, "error starting bluetooth")
