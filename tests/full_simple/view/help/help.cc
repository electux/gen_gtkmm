/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * help.cc
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
#include "help.h"

using namespace Electux::App::View::Help;

AppHelp::AppHelp()
{
    set_title("full_simple");
    set_default_size(600, 400);
    set_resizable(false);

    //////////////////////////////////////////////////////////////////////////
    /// Connect the signal handler for delete event (replace close with hide)
    signal_delete_event().connect(
        sigc::mem_fun(*this, &AppHelp::on_delete_event)
    );
}

bool AppHelp::on_delete_event(GdkEventAny* any_event)
{
    hide();
    return true;
}
