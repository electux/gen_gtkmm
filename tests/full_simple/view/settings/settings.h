/* -*- Mode: H; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * settings.h
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
#pragma once

#include <gtkmm/window.h>
#include <gtkmm/box.h>
#include <gtkmm/grid.h>
#include <gtkmm/button.h>

namespace Electux::App::View::Settings
{
    class AppSettings : public Gtk::Window
    {
    public:
        //////////////////////////////////////////////////////////////////////
        /// @brief AppSettings constructor
        explicit AppSettings();

    protected:
        //////////////////////////////////////////////////////////////////////
        /// @brief On delete even handler (planned for hide operation)
        bool on_delete_event(GdkEventAny* any_event);

    private:
        //////////////////////////////////////////////////////////////////////
        /// @brief On action OK button
        void on_button_ok_clicked();

        //////////////////////////////////////////////////////////////////////
        /// @brief On action Cancel button
        void on_button_cancel_clicked();

        //////////////////////////////////////////////////////////////////////
        /// @brief Vertiacl box as root container
        Gtk::Box m_vbox;

        //////////////////////////////////////////////////////////////////////
        /// @brief Grid box as content container
        Gtk::Grid m_content_box;

        //////////////////////////////////////////////////////////////////////
        /// @brief Horizontal box as button container
        Gtk::Grid m_button_box;

        //////////////////////////////////////////////////////////////////////
        /// @brief Ok button
        Gtk::Button m_button_ok;

        //////////////////////////////////////////////////////////////////////
        /// @brief Cancel button
        Gtk::Button m_button_cancel;
    };
};
