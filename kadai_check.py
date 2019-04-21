import os
import subprocess

'''
class Command():
    def __init__(self, command):
        self.arg = command.split()

    def proc(self):
        with subprocess.Popen(self.arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:
            message = proc.stdout.read()
            if(os.name == "nt"):
                print(message.decode("cp932"))
            elif(os.name == "posix"):
                print(message.decode("utf-8"))
            else:
                print("this program doesnt support your os \"%s\". \n good bye.", os.name)
                exit()
                print(message.decode("utf-8"))
'''

def IsCompile(commands):
    try:
        out = subprocess.check_output(commands, stderr=subprocess.STDOUT, shell=True)
        print(out)
        return True
    except subprocess.CalledProcessError as exc:
        print("return code:\"{}\"\noutput:\"{}\"".format(exc.returncode, exc.output,))
        return False

print(IsCompile("gcc test.c"))
