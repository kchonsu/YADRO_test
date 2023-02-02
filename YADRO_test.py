import csv


def op_res(data):
    if "+" in data:
        return "+"
    if "-" in data:
        return "-"
    if "*" in data:
        return "*"
    if "/" in data:
        return "/"


def calc(data, arg1, arg2):
    try:
        if data == "+":
            return int(arg1) + int(arg2)
        if data == "-":
            return int(arg1) - int(arg2)
        if data == "*":
            return int(arg1) * int(arg2)
        if data == "/":
            return int(arg1) / int(arg2)
    except ZeroDivisionError:
        return "denominator is 0"
    except ValueError:
        return "incorrect cell"


def cell_count(rows, columns, cell, reader):
    op = op_res(cell)
    tmp_list = cell.split(op)
    res = []
    for tmp_cell in tmp_list:
        c = 0
        tmp_row = 0
        tmp_column = 0
        for row in rows:
            if row in tmp_cell:
                tmp_row = rows.index(row) + 1
                c += 1
        for column in columns:
            if column in tmp_cell:
                tmp_column = columns.index(column) + 1
                c += 1
        if c == 2:
            res.append(reader[tmp_column][tmp_row])
        else:
            res.append(tmp_cell)
    try:
        arg2 = res.pop()
        arg1 = res.pop()
        print(calc(op, arg1, arg2), end=',')
    except IndexError:
        print("too few arguments", end=',')


try:
    with open(input()) as f:
        tmp_reader = list(csv.reader(f))
        reader = []
        rows = tmp_reader[0]
        columns = []
        length = len(rows)
        for i in tmp_reader:
            assert length == len(i) and len(tmp_reader) > 1, 'wrong format of CSV file'
            columns.append(i[0])
            reader.append(i)
            length = len(i)
        del rows[0]
        del columns[0]
        for i in reader:
            for j in i:
                if "=" in j:
                    tmp_str = j.replace('=', '')
                    cell_count(rows, columns, tmp_str, reader)
                    continue
                print(j, end=',')
            print()
except FileNotFoundError:
    print("wrong name file")
