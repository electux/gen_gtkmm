#!/bin/bash
#
# @brief   gen_gtkmm
# @version v1.1.2
# @date    Sat Aug 11 09:58:41 2021
# @company None, free software to use 2021
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_gtkmm unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
