import Image from "next/image";
import './logo.css'
const logo = '/images/logo/logo-no-respawn-white.svg'

export default function Logo() {
    return (
        <Image 
            src={logo}
            alt="Gateway Games Logo"
            width={96}
            height={96}
            className="logo"
        />
    )
}