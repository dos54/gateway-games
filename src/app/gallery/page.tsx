import { getImageList } from "@/utils/getImageList"
import Image from "next/image"
import './gallery.css'

const imageList = getImageList()

export default function Page() {
    return (
        <ul id="gallery">
            {imageList.map((image, index) => (
                <li className={`image-container card ${image.aspectRatio}`} key={index}>
                    <Image 
                        className="image"
                        src={image.url}
                        alt={image.alt}
                        fill
                        sizes="(max-width: 300px), 100vw, 300px"
                    />
                </li>     
            ))}
        </ul>
    )
}