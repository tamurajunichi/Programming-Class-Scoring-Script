import csv,os,re
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




csv_name = "out.csv"
cmd = "gcc"
target_file ="kadai02.c"

def search(pattern):
    full_list = []
    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            index = re.search(pattern, file)
            if index:
                append_list = [os.path.join(path, file),path,file]
                full_list.append(append_list)
    return full_list


def can_compile(commands):
    try:
        out = subprocess.run(commands, stdout=subprocess.PIPE ,stderr=subprocess.PIPE, shell=True)
        out.check_returncode()
        print(out.stdout.decode())
        print(out.stderr.decode())
        return True
    except subprocess.CalledProcessError as exc:
        print("return code:\"{}\"\noutput:\"{}\"".format(exc.returncode, exc.output,))
        return False


def create_csv(name):
    with open(name, 'w') as f:
        init_str = "New " + name + " file was created by CreateCSV function"
        print(str, csv_name)
        writer = csv.writer(f)
        writer.writerow([init_str])


def write_csv(name, out_list):
    with open(name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(out_list)

csv_path = "./" + csv_name

search_lists = search(target_file)
for child_list in search_lists:
    for child in child_list:
        print(child)

    cmd_list = [cmd, child_list[0]]
    result_compile = can_compile(commands=cmd_list)

    if not os.path.isfile(csv_path):
        create_csv(name=csv_name)

    out_list = [result_compile, child_list[1]]
    write_csv(name=csv_name, out_list=out_list)

