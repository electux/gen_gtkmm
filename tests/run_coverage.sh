#!/bin/bash
#
# @brief   gen_gtkmm
# @version v1.1.5
# @date    Sat Aug 11 09:58:41 2021
# @company None, free software to use 2021
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_gtkmm_coverage.xml gen_gtkmm_coverage.json .coverage
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/ fresh_new/
ats_coverage_run.py -n gen_gtkmm -p ../README.md
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/ fresh_new/
python3 -m coverage run -m --source=../gen_gtkmm unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_gtkmm_coverage.xml 
python3 -m coverage json -o gen_gtkmm_coverage.json
python3 -m coverage report --format=markdown -m
