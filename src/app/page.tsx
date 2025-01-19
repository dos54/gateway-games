import Image from "next/image";
import Socials from "@/components/socials/Socials";
import './home.css'

export default function Home() {
  return (
    <>
    <Image 
      src='images/logo/logo-white.svg'
      alt="Gateway Games Ketchikan Logo"
      width={800}
      height={800}
      className="hero"
    />
    <div className="call-to-action">
      <h1 
        className="centered call-to-action"
      >
        Upcoming Events
      </h1>
      <h2>No upcoming events at this time. Check back later!</h2>
      <Socials />
    </div>
    <section>
      <h2 className="centered">About Us</h2>
      <p>
        Welcome to Gateway Games! We are the First City&apos;s first game store. Gateway Games was first opened in 1997
        on the south end of Creek Street in Ketchikan, Alaska. In 1999 we moved to the basement of the Marine View building.
        In September of 2021 we moved out of the basement (about time for a 24 year old!) and into the Mason Building
        in downtown historic Ketchikan, near the tunnel, across from the eagle statue. In 2024 we once again moved
        a few storefronts down the street, right next to the city hall.
      </p>
      <p>
        In addition to being a store that&apos;s locally owned and staffed, we are open year round for locals to
        participate in the local nerd/geek/gamer community. We also sell items made by locals such as
        dice bags, dice trays, dice, custom shirts, and more! These are perfect as mementos of your trips,
        and make great gifts for any nerdlings you may have at home.
      </p>
    </section>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d392.51092292302053!2d-131.6485698405744!3d55.34247259528447!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x540c25a51aa326bf%3A0x594f67a97a043709!2sGateway%20Games!5e1!3m2!1ses-419!2sus!4v1737281840730!5m2!1ses-419!2sus" 
      width="300" 
      height="250" 
      loading="lazy" 
      referrerPolicy="no-referrer-when-downgrade" 
      className="google-maps-map">
    </iframe>
    </>
  );
}
