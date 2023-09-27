from Booking.booking import Booking
import time
with Booking() as bot:
    bot.first_page()
    bot.change_currency("USD")
    bot.destination("Goa")
    bot.checkDate("2023-09-27","2023-09-30")
    bot.adult(10)
    bot.searchEle()
    time.sleep(5)