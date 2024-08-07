/* -*- Mode: H; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * application.h
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

#include <gtkmm/application.h>
#include "view/home.h"
#include "view/settings/settings.h"
#include "view/help/help.h"
#include "view/about/about.h"

using namespace Electux::App::View;
using namespace Electux::App::View::Settings;
using namespace Electux::App::View::Help;
using namespace Electux::App::View::About;

namespace Electux::App
{
    //////////////////////////////////////////////////////////////////////////
    /// @brief Entry point for application
    class EntryApplication : public Gtk::Application
    {
    public:
        //////////////////////////////////////////////////////////////////////
        /// @brief EntryApplication constructor
        explicit EntryApplication();

        //////////////////////////////////////////////////////////////////////
        /// @brief Creates reference pointer to EntryApplication
        static Glib::RefPtr<EntryApplication> create();

    protected:
        //////////////////////////////////////////////////////////////////////
        /// @brief Handler for the startup signal
        void on_startup() override;

    private:
        //////////////////////////////////////////////////////////////////////
        /// @brief On action settings create window for application settings
        void on_action_settings();

        //////////////////////////////////////////////////////////////////////
        /// @brief On action doc create window for help documentation
        void on_action_doc();

        //////////////////////////////////////////////////////////////////////
        /// @brief On action about create dialog for about application
        void on_action_about();

        //////////////////////////////////////////////////////////////////////
        /// @brief On action for quit
        void on_action_quit();

        //////////////////////////////////////////////////////////////////////
        /// @brief Instance of HomeView (main window)
        AppHome m_home;

        //////////////////////////////////////////////////////////////////////
        /// @brief Instance of AppSettings (settings window)
        AppSettings m_settings;

        //////////////////////////////////////////////////////////////////////
        /// @brief Instance of AppHelp (help window)
        AppHelp m_help;

        //////////////////////////////////////////////////////////////////////
        /// @brief Instance of AppAbout (about dialog)
        AppAbout m_about;
    };
};
