'use client'

import Link from "next/link"
import Logo from '@/components/logo/Logo'
import { usePathname } from "next/navigation"

import { Pirata_One } from "next/font/google"
import './header.css'
import './header-medium.css'
import './header-large.css'

const links = [
    {
        title: 'Home',
        url: '/'
    },
    {
        title: 'Gallery',
        url: '/gallery'
    },
]

const pirataOne = Pirata_One({
    subsets: ['latin'],
    weight: '400',
})

export default function Header() {
    const pathname = usePathname()

    return (
        <div className="header-wrapper">
            <header className={`${pirataOne.className} antialiased`}>
                <Link href='/'>
                    <Logo />
                </Link>
                <h1>
                    Gateway Games Ketchikan
                </h1>
            </header>
            <nav>
                <ul>
                    {links.map((link) => 
                        <li 
                            key={link.url}
                            className={pathname === link.url ? 'active': ''}    
                        >
                            <Link href={link.url}>{link.title}</Link>
                        </li>
                    )}
                </ul>
            </nav>
        </div>
    )
}