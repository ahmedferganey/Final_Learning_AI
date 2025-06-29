import React from "react";
import { LayoutDashboard, Eye, BarChart2, Settings } from "lucide-react";

const Sidebar = () => {
  const menuItems = [
    { name: "Dashboard", icon: <LayoutDashboard size={20} />, active: true },
    { name: "Detection", icon: <Eye size={20} /> },
    { name: "Reports", icon: <BarChart2 size={20} /> },
    { name: "Settings", icon: <Settings size={20} /> },
  ];

  return (
    <aside className="w-64 bg-white shadow-md border-r h-full">
      <div className="p-6 font-bold text-xl text-blue-600">Vision App</div>
      <nav className="flex flex-col gap-2 px-4">
        {menuItems.map((item, index) => (
          <div
            key={index}
            className={`flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all hover:bg-blue-50 hover:text-blue-600 ${
              item.active ? "bg-blue-100 text-blue-600 font-semibold" : "text-gray-700"
            }`}
          >
            {item.icon}
            <span>{item.name}</span>
          </div>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;

