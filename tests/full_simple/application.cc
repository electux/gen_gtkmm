/* -*- Mode: CC; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * application.cc
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
#include "application.h"
#include <glibmm/miscutils.h>
#include <glibmm/refptr.h>

using namespace Electux::App;

EntryApplication::EntryApplication():
    Gtk::Application("electux.io.full_simple"),
    m_home{AppHome()},
    m_settings{AppSettings()},
    m_help{AppHelp()}
{
    Glib::set_application_name("electux.io.full_simple");
}

Glib::RefPtr<EntryApplication> EntryApplication::create()
{
    return Glib::RefPtr<EntryApplication>(new EntryApplication());
}

void EntryApplication::on_startup()
{
    Gtk::Application::on_startup();

    //////////////////////////////////////////////////////////////////////////
    /// Sets application menubar
    auto menu = Gio::Menu::create();
    auto submenu_file = Gio::Menu::create();
    submenu_file->append("_Quit", "app.quit");
    menu->append_submenu("File", submenu_file);
    auto submenu_option = Gio::Menu::create();
    submenu_option->append("_Settings", "app.setting");
    menu->append_submenu("Option", submenu_option);
    auto submenu_help = Gio::Menu::create();
    submenu_help->append("_Documentation", "app.doc");
    submenu_help->append("_About", "app.about");
    menu->append_submenu("Help", submenu_help);
    set_menubar(menu);

    //////////////////////////////////////////////////////////////////////////
    /// Sets a keyboard accelerator that will trigger application quit
    set_accel_for_action("app.quit", "<Primary>q");

    //////////////////////////////////////////////////////////////////////////
    /// Sets application actions
    add_action(
        "quit", sigc::mem_fun(*this, &EntryApplication::on_action_quit)
    );
    add_action(
        "setting", sigc::mem_fun(*this, &EntryApplication::on_action_settings)
    );
    add_action(
        "doc", sigc::mem_fun(*this, &EntryApplication::on_action_doc)
    );
    add_action(
        "about", sigc::mem_fun(*this, &EntryApplication::on_action_about)
    );

    //////////////////////////////////////////////////////////////////////////
    /// Sets AppHome as toplevel window, add to the application window
    add_window(m_home);

    //////////////////////////////////////////////////////////////////////////
    /// Sets visability for AppHome window
    m_home.set_visible(true);
}

void EntryApplication::on_action_quit()
{
    m_home.set_visible(false);
    remove_window(m_home);
    quit();
}

void EntryApplication::on_action_settings()
{
    m_settings.show();
}

void EntryApplication::on_action_doc()
{
    m_help.show();
}

void EntryApplication::on_action_about()
{
    m_about.show();
}
