import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SocialBot AI — Create. Schedule. Grow.",
  description: "Create AI-powered reels and manage your social publishing from one workspace.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
