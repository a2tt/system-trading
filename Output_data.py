# 17.09.14

import collections
from datetime import datetime

def thr_output(output_file, processed_data):
    print("Output _ for _ thr")

    with open(output_file, "wt") as fp:
        for item in processed_data:
            fp.write(str(item) + ",")
        fp.write("\n")
    fp.close()

def thr_data_gathering(output_file, real_data, quote_list):
    print("Data_Gathering")
    with open(output_file, 'at') as fp:

        fp.write("time" + "," + "now" + ",")
        for q in quote_list:
            fp.write(str(q) + ",")  # 주문 가격
        fp.write("\n")

        fp.write(str(real_data['time']) + "," + str(real_data['now']) + ",")
        for q in quote_list:
            fp.write(str(real_data[q][0]) + ",")  # 주문 잔량
        fp.write("\n,,")

        for q in quote_list:
            fp.write(str(real_data[q][1]) + ",")  # 추가 주문량
        fp.write("\n")
        fp.close()


def dict_output_batch_new(output_file, data, order, data_bat, order_bat, bat_size, quote_list):
    print("NEW OUTPUT BATCH FUNCTION")
    d = collections.OrderedDict(data)
    data_bat.append(d)
    o = collections.OrderedDict(order)
    order_bat.append(o)

    for i in order:
        order[i] = 0  # 주문 가능 호가가 변경되는 경우, 주문 불가능 호가에 주문량이 저장되는 것을 방지

    if len(data_bat) >= bat_size:  # bat_size 개 정보가 들어 있으면
        with open(output_file, "at") as fp:
            for i in range(0, len(data_bat)):
                fp.write("time" + "," + "now" + ",")
                for j in range(0, len(quote_list)):
                    fp.write(str(quote_list[j]) + ",")
                fp.write("\n")

                fp.write(str(data_bat[i]['time']) + ',' + str(data_bat[i]["now"]) + ',')
                for q in quote_list:
                    fp.write(str(data_bat[i][q]) + ',')
                fp.write("\n,,")

                for q in quote_list:
                    fp.write(str(order_bat[i][q]) + ',')
                fp.write("\n")

            fp.close()
        print(" ** NEW DICT 출력 완료 ** ")
        del data_bat[:]
        del order_bat[:]

def dict_output_batch(output_file, data, order, data_bat, order_bat, bat_size):
    d = collections.OrderedDict(data)
    data_bat.append(d)
    o = collections.OrderedDict(order)
    order_bat.append(o)

    for i in order:
        order[i] = 0  # 주문 가능 호가가 변경되는 경우, 주문 불가능 호가에 주문량이 저장되는 것을 방지

    if len(data_bat) >= bat_size:  # bat_size 개 정보가 들어 있으면
        with open(output_file, "at") as fp:
            for i in range(0, len(data_bat)):
                for key in data_bat[i].keys():
                    fp.write(str(key) + ",")  # 호가
                fp.write("\n")
                for key in data_bat[i].keys():
                    fp.write(str(data_bat[i][key]) + ",")  # 시간, 현재가, 주문 잔량
                fp.write("\n,,")
                for key in order_bat[i].keys():
                    fp.write(str(order_bat[i][key]) + ",")  # 추가 주문량
                fp.write("\n")
            fp.close()
        print(" ** DICT 출력 완료 ** ")
        del data_bat[:]
        del order_bat[:]

""" ======================================================================================== """
def output_batch(output_file, data, data_bat, bat_size):
    data_seq = [58, 52, 46, 40, 34, 28, 22, 16, 10, 4, 1, 7, 13, 19, 25, 31, 37, 43, 49, 55]
    # +0 : 호가 오름차순, +1 : 잔량, +2 : 추가주문량
    data_bat.append(data)

    try:
        if len(data_bat) >= bat_size:  # bat_size 개 정보가 들어 있으면
            with open(output_file, "at") as fp:
                for i in range(0, len(data_bat)):
                    fp.write((str(data_bat[i][0]) + ","))
                    for k in data_seq:
                        fp.write((str(data_bat[i][k]) + ","))
                    fp.write("\n,")
                    for k in data_seq:
                        fp.write((str(data_bat[i][k + 1]) + ","))  # 주문 잔량
                    fp.write("\n,")
                    for k in data_seq:
                        fp.write((str(data_bat[i][k + 2]) + ","))  # 추가 주문량
                    fp.write("\n")
                fp.close()
            del data_bat[:]
    except:
        # with open(output_file+"error.csv", "at") as fp:
        #    fp.write(str(datetime.now())+"\n")
        #    fp.close()
        print("Permissoin Error - {}".format(datetime.now()))
        with open(output_file + "err.csv", "at") as fp:
            for i in range(0, len(data_bat)):
                fp.write((str(data_bat[i][0]) + ","))
                for k in data_seq:
                    fp.write((str(data_bat[i][k]) + ","))
                fp.write("\n,")
                for k in data_seq:
                    fp.write((str(data_bat[i][k + 1]) + ","))  # 주문 잔량
                fp.write("\n,")
                for k in data_seq:
                    fp.write((str(data_bat[i][k + 2]) + ","))  # 추가 주문량
                fp.write("\n")
            fp.close()
        del data_bat[:]
    print("* 베치 데이터 출력 완료")

def output_result(output_file, data):
    """
    입력된 데이터를 바로 출력
    """
    data_seq = [58, 52, 46, 40, 34, 28, 22, 16, 10, 4, 1, 7, 13, 19, 25, 31, 37, 43, 49,
                55]  # 호가 오름차순 +1 : 잔량, +2 : 추가주문량
    try:
        with open(output_file, "at") as fp:
            fp.write(str(data[0]) + ",")
            for i in data_seq:
                fp.write(str(data[i]) + ",")  # 주문 가격
            fp.write("\n,")
            for i in data_seq:
                fp.write(str(data[i + 1]) + ",")  # 주문 잔량
            fp.write("\n,")
            for i in data_seq:
                fp.write(str(data[i + 2]) + ",")  # 추가 주문량
            fp.write("\n")
            fp.close()

    except PermissionError:
        print("************ PermissionError ************")
        with open(output_file + "_error.csv", "at") as fp:
            fp.write(str(data[0]) + ",")
            for i in data_seq:
                fp.write(str(data[i]) + ",")
            fp.write("\n,")
            for i in data_seq:
                fp.write(str(data[i + 1]) + ",")
            fp.write("\n,")
            for i in data_seq:
                fp.write(str(data[i + 2]) + ",")
            fp.write("\n")
            fp.close()
    print("* 실시간 데이터 출력 완료")
