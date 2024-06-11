/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * full_simple.cc
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * full_simple is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * full_simple is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "full_simple.h"
#include <iostream>

Full_simple::Full_simple()
: message_button("Hello World")
{
  set_border_width(10);
  message_button.signal_clicked().connect(
    sigc::mem_fun(*this, &Full_simple::on_message_button_clicked)
  );
  add(message_button);
  message_button.show();
  std::cout << "Hello from full_simple" << std::endl;
}

Full_simple::~Full_simple()
{
  std::cout << "Good buy from full_simple" << std::endl;
}

void Full_simple::on_message_button_clicked()
{
  std::cout << "Hello again from full_simple" << std::endl;
}
