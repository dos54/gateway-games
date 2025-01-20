import data from '@/data/events.json'

export function getEventsList() {
    return data
}

export function getUpcomingEventsSorted() {
    return data
        .filter(event => new Date(event.event_date) > new Date())
        .sort((a, b) => new Date(a.event_date).getTime() - new Date(b.event_date).getTime())

}
