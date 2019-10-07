monthDictonary = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

selected_month = input("Please enter a short form month")

print("The long form version of your input is " + monthDictonary.get(selected_month, "cannot be found"))