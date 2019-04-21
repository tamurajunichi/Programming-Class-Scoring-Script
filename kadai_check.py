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


def search_files(pattern):
    search_list = []
    for pathname, dir_names, file_names in os.walk(os.getcwd()):
        for file_name in file_names:
            index = re.search(pattern, file_name)
            if index:
                search_list.append(file_name)
        for dir_name in dir_names:
            index = re.search(pattern, dir_name)
            if index:
                search_list.append(dir_name)
    return search_list


def can_compile(commands):
    try:
        out = subprocess.check_output(commands, stderr=subprocess.STDOUT, shell=True)
        print(out)
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

search_names = search_files("2016*")
for search_name in search_names:
    cmd_list = [cmd, search_name]
    result_compile = can_compile(commands=cmd_list)

    if not os.path.isfile(csv_path):
        create_csv(name=csv_name)

    out_list = [result_compile, search_name]
    write_csv(name=csv_name, out_list=out_list)

