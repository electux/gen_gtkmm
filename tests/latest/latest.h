/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * latest.h
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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

#pragma once

#include <gtkmm/button.h>
#include <gtkmm/window.h>

class Latest : public Gtk::Window
{

public:
  Latest();
  virtual ~Latest();

protected:
  void on_message_button_clicked();
  Gtk::Button message_button;
};
