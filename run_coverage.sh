#!/bin/bash
#
# @brief   gen_gtkmm
# @version 1.1.9
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_gtkmm
pylint gen_gtkmm > gen_gtkmm.report
echo "Done"
