import csv, os, re
import subprocess

"""
csv_name: (string)csv形式でコンパイルできるかの結果を出力するためのファイル名
cmd: (string)subprocessで実行するコマンド
target_dir: (string)コマンドのターゲットファイルが入っているディレクトリを検索する用
excute_file: (string)コンパイル後の実行ファイル名を指定
I,O: (list)実行ファイルを実行した後に求められる標準入力の変数を格納
I_decimal,O_decimal: (list)I,Oに格納されている値の小数点以下桁数を格納
"""
csv_name = "out.csv"
cmd = "gcc"
# target_file = "kadai01.c"
target_dir = "201*"
execute_file = "a.exe"
I = []
O = []
I_decimal = []
O_decimal = []


def stdio(execute_path):
    """
    標準入出力を操作する関数
    :param execute_path:(string)標準出力の結果
    :return:標準出力結果と標準入力の値を格納したリスト
    """
    input = ('\n'.join(map(str, I)) + '\n').encode()
    proc = subprocess.Popen(execute_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    out, err = proc.communicate(input)
    out = out.decode("utf-8", "backslashreplace")
    print("\n")
    print(out)
    print("\n")
    return [out, I]


def extract_out(out, a=0):
    """
    out引数から必要な数字を抽出する関数
    :param out: (string)標準出力結果
    :param a: (int)正規表現の切り替え用変数
    :return: outから抽出した数字
    """
    # 一つの正規表現だと対応できない

    if a == 0:  # \nの手前に単位がついていた場合の数値
        return re.findall(r"[^亜-熙ぁ-んァ-ヶ\.\d-]+(-?\d+\.?\d*)[\n\t\s点%％]+", out, re.M)
    else:  # \nで終わってる数値
        return re.findall(r"(-?\d+\.?\d*)\s*$", out, re.MULTILINE)



def fomula():
    """
    標準入出力で使用される値と個数、桁数を入力させる関数
    :return:
    """
    global I,O
    input_num = int(input("入力個数："))
    output_num = int(input("出力個数："))

    for i in range(input_num):
        I.append(input(str(i+1)+"番目の入力値:"))
        if isfloat(I[i]) is True:
            I[i] = float(I[i])
        else:
            I[i] = int(I[i])


    for i in range(output_num):
        O.append(input(str(i+1)+"番目の出力値:"))
        if isfloat(O[i]) is True:
            O[i] = float(O[i])
        else:
            O[i] = int(O[i])

    # exec(str(input("評価式を入力。(例：I.append[10]; I.append[10.0]; O.append[I[0]+I[1]]):")))
    # exec("I.append(55.8);I.append(168.3);O.append(19.7);O.append(62.3);O.append(-10.5)")
    # exec("I.append(123.456789);I.append(987.654321);O.append(1111.111110);O.append(-864.197532);O.append(121932.631113);O.append(0.125000)")
    for i in I:
        I_decimal.append(int(input(str(i) + "の少数点以下桁数を入力:")))
        # I_decimal.append(6)
    for o in O:
        O_decimal.append(int(input(str(o) + "の小数点以下桁数を入力:")))
        # O_decimal.append(6)


def eval_number(a, b):
    return len(a) == len(b)


def eval_type(a, b):
    return type(a) == type(b)


def isfloat(a):
    """
    引数で受け取った変数がintかfloatか判定関数
    :param a:
    :return:
    """
    try:
        a = int(a)
        return False
    except ValueError:
        return True


def eval_decimal_point(a, b):
    """
    aの小数点以下桁数とbが一致するか判定関数
    :param a: (string)評価する数字
    :param b: (int)aを評価するための桁数
    :return: ブール値を返す
    """
    c = str(a).split('.')
    try:
        d = len(c[1]) == b
        return len(c[1]) == b
    except IndexError:
        return 0 == b


def eval_value(a, b):
    a = float(a)
    d = a == b
    return float(a) == b


def eval(stdio_list):
    """
    標準入出力の結果とI,Oの個数、型、桁数、値が一致するか判定する関数
    :param stdio_list: (list)標準入出力の値が格納されたリスト
    :return:
    """
    out = extract_out(stdio_list[0])
    input = stdio_list[1]

    if eval_number(input, I) is True:
        print("入力個数\t\t〇")
        if eval_type(input, I) is True:
            print("入力値の型\t〇")
            for i, num in enumerate(input):
                if isfloat(num) is True:
                    print("入力値は実数")
                else:
                    print("入力値は整数")
        else:
            print("入力値の型\t\t×")
    else:
        print("入力個数\t\t×")

    print("\n")

    if eval_number(out, O) is True:
        print("出力個数\t〇")
        if eval_type(out, O) is True:
            print("出力値の型\t〇")
            for i, num in enumerate(out):
                if eval_decimal_point(num, O_decimal[i]) is True:
                    print("出力値の桁数\t〇")
                    if eval_value(num, O[i]) is True:
                        print("出力値\t\t〇")
                    else:
                        print("出力値\t\t×")
                else:
                    print("出力値の桁数\t×")
        else:
            print("出力値の型\t\t×")

    elif eval_number(extract_out(stdio_list[0], a=1), O) is True:
        out = extract_out(stdio_list[0], a=1)
        print("出力個数\t〇")
        if eval_type(out, O) is True:
            print("出力値の型\t〇")
            for i, num in enumerate(out):
                if eval_decimal_point(num, O_decimal[i]) is True:
                    print("出力値の桁数\t〇")
                    if eval_value(num, O[i]) is True:
                        print("出力値\t\t〇")
                    else:
                        print("出力値\t\t×")
                else:
                    print("出力値の桁数\t×")
        else:
            print("出力値の型\t\t×")
    else:
        print("出力個数\t\t×")


def rename_dir(pattern):
    """
    ディレクトリの名前をgccが認識できるようにリネームする関数
    :param pattern: (string)reモジュールで使用する正規表現が入った文字列
    :return:
    """
    full_list = []
    for path, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            index = re.search(pattern, dir)
            if index:
                rename_path = path + "\\" + dir
                os.rename(rename_path, path + "\\" + re.search("\d*", dir).group(0))


def search(pattern):
    """
    カレントディレクトリ以降の階層のディレクトリ、ファイルのなかから目的のファイル、パスを返す関数
    :param pattern: (string)reモジュールのsearch関数で使用するための正規表現が入った文字列
    :return: full_list: (list)目的のファイル名、そこまでのディレクトリパス、ファイルまでのパスが格納されているリスト
    """
    full_list = []
    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            index = re.search(pattern, file)
            if index:
                full_list.append([os.path.join(path, file), path, file])
    return full_list


def can_compile(commands):
    """
    commandsを実行してコンパイルできるかチェックする関数
    :param commands: (string)オプションまで含めた実行するコマンドの文字列
    :return: ブール値を返す
    """
    print(commands)
    try:
        out = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(out.stdout.decode())
        out.check_returncode()
        return True
    except subprocess.CalledProcessError as exc:
        print("return code:\"{}\"\noutput:\"{}\"".format(exc.returncode, exc.stderr.decode(), ))
        return False


def create_csv(name):
    """
    csvファイルをカレントディレクトリに作る関数
    :param name: (string)作成するcsvの名前
    :return:
    """
    with open(name, 'w') as f:
        init_str = "New " + name + " file was created by CreateCSV function"
        print(str, csv_name)
        writer = csv.writer(f)
        writer.writerow([init_str])


def write_csv(name, out_list):
    """
    csvに行を追加して書き込む関数
    :param name: (string)書き込むcsvファイルの名前
    :param out_list: (string)書き込む文字列
    :return:
    """
    with open(name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(out_list)


rename_dir(target_dir)
csv_path = "./" + csv_name
target_file = input("target_fileを指定：")
fomula()
search_lists = search(target_file)

for path_info in search_lists:

    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    excute_path = os.path.join(path_info[1], execute_file)
    cmd_list = cmd + " " + path_info[0] + " -o " + excute_path
    result_compile = can_compile(commands=cmd_list)

    if not os.path.isfile(csv_path):
        create_csv(name=csv_name)

    out_list = [result_compile, path_info[1]]
    write_csv(name=csv_name, out_list=out_list)

    if result_compile is True:
        stdio_list = stdio(excute_path)
        eval(stdio_list)
input("終了する場合はEnter")