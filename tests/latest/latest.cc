/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * latest.cc
 * Copyright (C) 2023 Vladimir Roncevic <elektron.ronca@gmail.com>
 * 
 * latest is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * latest is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "latest.h"
#include <iostream>

Latest::Latest()
: message_button("Hello World")
{
  set_border_width(10);
  message_button.signal_clicked().connect(
    sigc::mem_fun(*this, &Latest::on_message_button_clicked)
  );
  add(message_button);
  message_button.show();
  std::cout << "Hello from latest" << std::endl;
}

Latest::~Latest()
{
  std::cout << "Good buy from latest" << std::endl;
}

void Latest::on_message_button_clicked()
{
  std::cout << "Hello again from latest" << std::endl;
}
