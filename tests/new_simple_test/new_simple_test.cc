/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * new_simple_test.cc
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * new_simple_test is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * new_simple_test is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "new_simple_test.h"
#include <iostream>

New_simple_test::New_simple_test()
: message_button("Hello World")
{
  set_border_width(10);
  message_button.signal_clicked().connect(
    sigc::mem_fun(*this, &New_simple_test::on_message_button_clicked)
  );
  add(message_button);
  message_button.show();
  std::cout << "Hello from new_simple_test" << std::endl;
}

New_simple_test::~New_simple_test()
{
  std::cout << "Good buy from new_simple_test" << std::endl;
}

void New_simple_test::on_message_button_clicked()
{
  std::cout << "Hello again from new_simple_test" << std::endl;
}
