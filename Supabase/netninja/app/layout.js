import Link from "next/link"
import "./globals.css"

export const metadata = {
  title: "Supa Smoothies",
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <nav>
          <h1>Supa Smoothies</h1>
          <Link href="/">Home</Link>
          <Link href="/create">Create New Smoothie</Link>
        </nav>
        {children}
      </body>
    </html>
  )
}