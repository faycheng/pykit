# coding=utf-8
import tablib


def json2csv(data, out="./out.csv"):
    headers = data[0].keys()
    data_set = tablib.Dataset(headers=headers)
    for item in data:
        values = []
        for key in headers:
            values.append(item[key])
        data_set.append(values)
    bytes = data_set.export('csv')
    with open(out, "w+") as fd:
        fd.write(str(bytes))
