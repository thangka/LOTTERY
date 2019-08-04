#!usr/bin/env python3
# coding=utf-8
__doc__ = '''Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

import requests
import bs4
import sys


def check_Lottery(*argument):
    resp = requests.Session().get('http://ketqua.net')
    tree = bs4.BeautifulSoup(resp.text, features="html.parser")
    id_prizes = ["rs_0_0", "rs_1_0", "rs_2_0", "rs_2_1", "rs_3_0", "rs_3_1",
                 "rs_3_2", "rs_3_3", "rs_3_4", "rs_3_5", "rs_4_0", "rs_4_1",
                 "rs_4_2", "rs_4_3", "rs_5_0", "rs_5_1", "rs_5_2", "rs_5_3",
                 "rs_5_4", "rs_5_5", "rs_6_0", "rs_6_1", "rs_6_2", "rs_7_0",
                 "rs_7_1", "rs_7_2", "rs_7_3"]

    if len(sys.argv) > 1:
        for argument in sys.argv[1:]:
            for id_prize in id_prizes:
                if str(argument) == tree.find_all(attrs={'id':
                                                  id_prize})[0].text[-2:]:
                    if int(id_prize[3]) == 0:
                        print('Bạn đã trúng giải {}'.format('Đặc biệt'))
                    else:
                        print('Bạn đã trúng giải {}'.format(id_prize[3]))
        print("Mai thử lại nhé!")

    else:
        print('Bạn không trúng lô hôm nay\nDanh sách giải:')
        for i in id_prizes:
            print(tree.find_all(attrs={'id': i})[0].text[-2:])


def main():
    for argument in sys.argv[1:]:
        if len(argument) != 2:
            raise ValueError('Lô có 2 chữ số nhé!')
    check_Lottery(*sys.argv[1:])


if __name__ == '__main__':
    main()
