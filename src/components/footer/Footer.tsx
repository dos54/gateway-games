import './footer.css'
import Socials from '../socials/Socials'
const currentYear = new Date().getFullYear()


export default function Footer() {

    return (
        <footer>
            <div id="copyright">
                &copy; {currentYear} {' '}
                <span> 
                    Gateway Games Alaska
                </span>

            </div>
            <div id="social-media">
                <p>Social Media Links</p>
                <Socials />
            </div>
            <div id="links">
                <a href="https://icons8.com/icons">Facebook Icon from Icons8.com</a>
            </div>
        </footer>
    )
}