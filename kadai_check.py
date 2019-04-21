import subprocess


class Command():
    def __init__(self, command):
        self.arg = command.split()

    def proc(self):
        with subprocess.Popen(self.arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:
            message = proc.stdout.read()
            print(message.decode("utf-8"))


gccv = Command("gcc -v")
gccv.proc()
