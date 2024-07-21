/* -*- Mode: H; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * home.h
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

#include <gtkmm/applicationwindow.h>
#include <gtkmm/box.h>

namespace Electux::App::View
{
    //////////////////////////////////////////////////////////////////////////
    /// @brief Home view window definition
    class AppHome : public Gtk::ApplicationWindow
    {
    public:
        //////////////////////////////////////////////////////////////////////
        /// @brief AppHome constructor
        explicit AppHome();

    private:
        //////////////////////////////////////////////////////////////////////
        /// @brief Container for packing widgets
        Gtk::Box m_box;
    };
};
