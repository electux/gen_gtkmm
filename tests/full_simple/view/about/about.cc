/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * about.cc
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
#include "about.h"

using namespace Electux::App::View::About;

AppAbout::AppAbout()
{
    set_program_name("full_simple");
    set_version("1.0.0");
    set_copyright("Vladimir Roncevic <elektron.ronca@gmail.com>");
    set_comments("This is full_simple application.");
    set_license("GPLv3");
    set_website("https://electux.github.io/full_simple");
    set_website_label("electux.github.io/full_simple");
    std::vector<Glib::ustring> list_authors;
    list_authors.push_back("Vladimir Roncevic");
    set_authors(list_authors);

    //////////////////////////////////////////////////////////////////////////
    /// Connect the signal handler for delete event (replace close with hide)
    signal_delete_event().connect(
        sigc::mem_fun(*this, &AppAbout::on_delete_event)
    );
}

bool AppAbout::on_delete_event(GdkEventAny* any_event)
{
    hide();
    return true;
}
