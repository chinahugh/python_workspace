# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
# Beware the Ides of March.
# """)
# server.quit()
# ------------------
# dates are easily constructed and formatted
# import datetime
# now = datetime.date.today()
# print(now)
# datetime.date(2003, 12, 2)
# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# age.days