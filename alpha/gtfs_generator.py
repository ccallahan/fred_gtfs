import transitfeed

schedule = transitfeed.Schedule()

schedule.AddAgency("Fredericksburg Regional Transit", "https://www.ridefred.com", "America/New_York")

service_period = schedule.GetDefaultServicePeriod()
service_period.SetStartDate("20190913")
service_period.SetEndDate("20200913")
