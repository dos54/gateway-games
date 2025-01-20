import { getEventsList } from "@/utils/getEventsList"
import { dateFormatter } from "@/utils/dateFormatter"
import './events.css'

const eventsList = getEventsList()

const upcomingEventsSorted = eventsList
    .filter(event => new Date(event.event_date) > new Date())
    .sort((a, b) => new Date(a.event_date).getTime() - new Date(b.event_date).getTime())



export default function Events() {
    return (
        <>
        <h1 className="centered">Upcoming Events</h1>
        <ol className="events-container">
            {upcomingEventsSorted.map(event => (
                <li key={event.event_id}
                className="card">
                    <h2>{event.title}</h2>
                    <p>Published by: {event.author_name}</p>
                    <p>Event Date: {dateFormatter(new Date(event.event_date))}</p>
                    {event.details}
                </li>
            ))
            }
        </ol>
        </>
    )
}