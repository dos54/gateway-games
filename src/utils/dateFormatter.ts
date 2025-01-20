export function dateFormatter(date: Date) {
    return new Intl.DateTimeFormat('en-US', {
        dateStyle: 'full',
        timeStyle: 'short'
    }).format(date)
}