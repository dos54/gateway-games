import Image from "next/image"
import './socials.css'

interface SocialsProps {
    className?: string
}

export default function Socials ({ className }: SocialsProps) {
    return (
        <div className={`socials-media-links ${className || ""}`}>
            <a href="https://www.facebook.com/gatewaygamesak/" title="Gateway Games Alaska Facebook" className="social-icon">
                <Image 
                    src={"images/icons/facebook-icon.svg"}
                    alt="Gateway Games Alaska Facebook"
                    width={64}
                    height={64}
        
                />
            </a>
        </div>
    )
}