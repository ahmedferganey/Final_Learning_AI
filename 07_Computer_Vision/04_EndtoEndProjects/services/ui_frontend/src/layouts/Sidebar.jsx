import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Eye,
  BarChart2,
  Settings,
  Video,
  Home as HomeIcon,
  Menu as MenuIcon,
  X as XIcon,
} from "lucide-react";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    { name: "Home", icon: HomeIcon, path: "/Home" },
    { name: "Streaming", icon: Video, path: "/Streaming" },
    { name: "Dashboard", icon: LayoutDashboard, path: "/dashboard" },
    { name: "Detection", icon: Eye, path: "/detection" },
    { name: "Reports", icon: BarChart2, path: "/reports" },
    { name: "Settings", icon: Settings, path: "/settings" },
  ];

  return (
    <>
      {/* Mobile hamburger button */}
      <button
        className="md:hidden fixed top-4 left-4 z-50 p-2 rounded-md bg-blue-600 text-white shadow-lg"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle sidebar"
      >
        {isOpen ? <XIcon size={24} /> : <MenuIcon size={24} />}
      </button>

      {/* Sidebar */}
      <aside
        className={`
          fixed top-0 left-0 h-full bg-white dark:bg-gray-900 shadow-md border-r
          transform transition-transform duration-300 ease-in-out
          w-64
          overflow-y-auto
          z-40

          ${isOpen ? "translate-x-0" : "-translate-x-full"}  /* Mobile slide */
          md:translate-x-0 md:static md:flex md:flex-col
        `}
      >
        <div className="p-6 font-bold text-xl text-blue-600 dark:text-white">
          Vision App
        </div>
        <nav className="flex flex-col gap-2 px-4">
          {menuItems.map(({ name, icon: Icon, path }) => (
            <NavLink
              key={name}
              to={path}
              className={({ isActive }) =>
                `flex items-center gap-3 p-3 rounded-lg transition-all hover:bg-blue-50 dark:hover:bg-gray-800 ${
                  isActive
                    ? "bg-blue-100 text-blue-600 font-semibold dark:bg-blue-800 dark:text-white"
                    : "text-gray-700 dark:text-gray-300"
                }`
              }
              onClick={() => setIsOpen(false)} // Close sidebar on mobile after click
            >
              <Icon size={20} />
              <span>{name}</span>
            </NavLink>
          ))}
        </nav>
      </aside>

      {/* Overlay behind sidebar on mobile when open */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-25 z-30 md:hidden"
          onClick={() => setIsOpen(false)}
          aria-hidden="true"
        />
      )}
    </>
  );
};

export default Sidebar;

