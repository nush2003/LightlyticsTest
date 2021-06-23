
import json
import os.path


class Test:
   # def __init__(self):

    def parseData(self):
        prev_line = "";
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "exercise.log")
        names_list = list(filter(None, open(path, "r").read().splitlines()))

        for index1,line in enumerate(names_list):
            if line.split(' ')[5] in "create delete add remove modify hard-modify".split():

                ##create dictionary structure
                struct_name = line.split(' ')[5]
                structure = {struct_name: {"date": [], "time": [], "event_type": [], "event_resource": [], "event_attr": [], "aws_event_name": [], "scan": []}}

                structure[struct_name]["date"].append(line.split()[0])
                structure[struct_name]["time"].append(line.split()[1])
                structure[struct_name]["event_type"].append(line.split()[5])
                structure[struct_name]["event_resource"].append(line.split()[6])
                if (line.split().__len__() >9):
                    if (len(line.split('['))>1):
                        json_data = line.split('[')[1].split(']')[0]
                        json_data = json.loads(json.dumps(json_data))
                        structure[struct_name]["event_attr"].append(json_data)

                ##first bonus question
                if (prev_line != ""):
                    prev_arr = prev_line.split()
                    for index2,i in enumerate(prev_arr):
                        if (i == 'performed'):
                            structure[struct_name]["aws_event_name"].append(prev_arr[index2+1])

                ##second bonus question
                if (index1<len(names_list) -1):
                    arr = names_list[index1+1].split(' ')
                    if arr.__contains__("Scanning"):
                        structure[struct_name]["scan"].append("true")
                    else:
                        structure[struct_name]["scan"].append("false")
                print(structure)
            prev_line=line


if __name__ == '__main__':

    my_test = Test()
    my_test.parseData()



