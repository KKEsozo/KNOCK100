# coding=utf-8
"""
created on 2016/10/04
@author onishi
"""

import time


def reverse_string(input_string=""):
    """
    文字列を逆に並べる
    :param input_string:
    :return output_string:
    """

    string_list = list(input_string)
    string_list.reverse()
    output_string = "".join(string_list)
    return output_string


def main():
    """
    main
    """

    # Start
    start_time = time.time()

    # Question
    input_string = "stressed"
    question = "文字列の逆順文字列%sの文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．" % input_string
    print ("Question 00 : %s" % question)

    # Solver
    output = reverse_string(input_string=input_string)

    # Answer
    answer = output
    print ("Answer 00 : %s" % answer)

    # Finish
    end_time = time.time()
    print("Total Time : " + str(end_time - start_time) + " sec")

if __name__ == '__main__':
    main()
