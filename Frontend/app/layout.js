import "./globals.css";

export const metadata = {
  title: "TrekDesk",
  description: "Internal booking tracker for treks",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}