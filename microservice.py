import json
import time


def get_mats(file, item, mat):
    with open(file) as json_file:
        data = json.load(json_file)
        mat_list = data[item][0][mat]
    return mat_list


if __name__ == '__main__':
    print("running microservice.py ...")
    while True:
        time.sleep(1)
        f = open("./text_files/list.txt", "r")
        text = f.readlines()
        f.close()

        if text[0].strip() == '1':
            print("getting " + text[3] + "...")
            mat_list = get_mats(text[1].strip(), text[2].strip(), text[3])
            f = open("./text_files/list.txt", "w")
            for i in range(len(mat_list) - 1):
                f.write(str(mat_list[i]) + ",")
            f.write(str(mat_list[len(mat_list) - 1]))
            f.close()
