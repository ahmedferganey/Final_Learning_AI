import type { Metadata } from "next";
import "./globals.css";
import { ReactQueryProvider } from "@/providers/query-provider";

export const metadata: Metadata = {
  title: "GymOS",
  description: "Adaptive training intelligence platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ReactQueryProvider>{children}</ReactQueryProvider>
      </body>
    </html>
  );
}
