/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * settings.cc
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
#include "settings.h"

using namespace Electux::App::View::Settings;

AppSettings::AppSettings()
{
    set_title("full_simple");
    set_default_size(600, 300);
    set_resizable(false);
    add(m_vbox);
    m_content_box.set_size_request(380, 240);
    m_vbox.add(m_content_box);
    m_button_box.set_size_request(220, 60);
    m_button_ok.set_label("Ok");
    m_button_ok.set_size_request(100, 50);
    m_button_cancel.set_label("Cancel");
    m_button_cancel.set_size_request(100, 50);
    m_button_box.attach(m_button_ok, 0, 0, 1, 1);
    m_button_box.attach(m_button_cancel, 1, 0, 1, 1);
    m_button_box.set_hexpand(false);
    m_button_box.set_vexpand(false);
    m_button_box.set_row_spacing(5);
    m_button_box.set_column_spacing(5);
    m_vbox.add(m_button_box);
    show_all_children();

    //////////////////////////////////////////////////////////////////////////
    /// Connect the signal handlers to the buttons
    m_button_ok.signal_clicked().connect(
        sigc::mem_fun(*this, &AppSettings::on_button_ok_clicked)
    );
    m_button_cancel.signal_clicked().connect(
        sigc::mem_fun(*this, &AppSettings::on_button_cancel_clicked)
    );

    //////////////////////////////////////////////////////////////////////////
    /// Connect the signal handler for delete event (replace close with hide)
    signal_delete_event().connect(
        sigc::mem_fun(*this, &AppSettings::on_delete_event)
    );
}

bool AppSettings::on_delete_event(GdkEventAny* any_event)
{
    hide();
    return true;
}

void AppSettings::on_button_ok_clicked()
{
    //////////////////////////////////////////////////////////////////////////
    /// Perform action on OK button
    hide();
}

void AppSettings::on_button_cancel_clicked()
{
    //////////////////////////////////////////////////////////////////////////
    /// Perform action on Cancel button
    hide();
}
