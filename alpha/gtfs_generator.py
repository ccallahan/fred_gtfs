from datetime import date
import holidays
import transitfeed




schedule = transitfeed.Schedule()

schedule.AddAgency("Fredericksburg Regional Transit", "https://www.ridefred.com", "America/New_York")

service_period = schedule.GetDefaultServicePeriod()
service_period.SetStartDate("20190913") # Arbitrary Start Date
service_period.SetEndDate("20200913") # Probably should review this a year from now, if not sooner.
service_period.SetWeekdayService(has_service=True)

# Now we set holidays.
    #This needs some work, end goal is to add auto-holiday fill using the Python 'holidays' Libs.  -wertyy102
service_period.SetDateHasService("20200101", has_service=False) # New Years Day
service_period.SetDateHasService("20200525", has_service=False) # Memorial Day
service_period.SetDateHasService("20200704", has_service=False) # National High Explosives Day
service_period.SetDateHasService("20200907", has_service=False) # Labor Day
service_period.SetDateHasService("20191128", has_service=False) # Turkey Day
service_period.SetDateHasService("20191224", has_service=False) # Christmas Eve
service_period.SetDateHasService("20191225", has_service=False) # Christmas Day


    # Holidays psuedo-code followed by possible functioning holidays code.
#
#           using holiday name, set holiday date to closed.  
#
#    service_period.SetDateHasService("20200101", has_service=False) # New Years Day
#    service_period.SetDateHasService("20200525", has_service=False) # Memorial Day
#    service_period.SetDateHasService("20200704", has_service=False) # National High Explosives Day
#    service_period.SetDateHasService("20200907", has_service=False) # Labor Day
#    service_period.SetDateHasService("20191128", has_service=False) # Turkey Day
#    service_period.SetDateHasService("20191224", has_service=False) # Christmas Eve
#    service_period.SetDateHasService("20191225", has_service=False) # Christmas Day



# Add the routes.

# Stafford County Runs

route_d1 = schedule.AddRoute(short_name="D1", long_name="Train Station to Olde Forge", route_type="Bus", route_id="D1")
route_d2 = schedule.AddRoute(short_name="D2", long_name="FRED Central, Olde Forge, England Run, GEICO", route_type="Bus", route_id="D2")
route_d3 = schedule.AddRoute(short_name="D3", long_name="Stafford Shopping Loop", route_type="Bus", route_id="D3")
route_d4 = schedule.AddRoute(short_name="D4", long_name="Stafford Marketplace to Northampton Blvd.", route_type="Bus", route_id="D4")
route_d5 = schedule.AddRoute(short_name="D5", long_name="FRED Central to Stafford Courthouse", route_type="Bus", route_id="D5")
route_d6 = schedule.AddRoute(short_name="D6", long_name="Stafford County EXPRESS", route_type="Bus", route_id="D6")

# Bus Stops

stop_6 = schedule.AddStop(lat="38.298318", lng="-77.456132", name="Train Station (Caroline St.)", stop_id="6")
stop_67 = schedule.AddStop(lat="38.29797", lng="-77.457208", name="Train Station (Princess Anne St.)", stop_id="67")
stop_109 = schedule.AddStop(stop_id="109", name="Dixon and Charles St.", lat="38.294347", lng="-77.456577")
stop_401 = schedule.AddStop(stop_id="401", name="Walmart (Washington Sq.)", lat="38.28375", lng="-77.43654")
stop_418 = schedule.AddStop(stop_id="418", name="Ferry Farm Shopping Center", lat="38.297955", lng="-77.446622")
stop_291 = schedule.AddStop(stop_id="291", name="Rappahannock Optical", lat="38.305928", lng="-77.452731")
stop_501 = schedule.AddStop(stop_id="501", name="Earl's True Value Hardware", lat="38.310067", lng="-77.448175")
stop_432 = schedule.AddStop(stop_id="432", name="Chatham Heights and Marion Rd", lat="38.313291", lng="-77.450801")
stop_450 = schedule.AddStop(stop_id="450", name="Old Forge Dr. and Warrenton Rd.", lat="38.337279", lng="-77.485423")
stop_451 = schedule.AddStop(stop_id="451", name="Old Forge Dr. and Warrenton Rd.", lat="38.337167", lng="-77.485917")
stop_449 = schedule.AddStop(stop_id="449", name="Warrenton and Quarels Rd", lat="38.33553", lng="-77.482431")
stop_437 = schedule.AddStop(stop_id="437", name="Bulter Rd and YMCA", lat="38.317363", lng="-77.456062")
stop_436 = schedule.AddStop(stop_id="436", name="Deacon Rd. @ Woodland Shopping Cntr.", lat="38.327251", lng="-77.439217")
stop_435 = schedule.AddStop(stop_id="435", name="Culpeper St. and Greenwood Dr.", lat="38.32585", lng="-77.432881")
stop_433 = schedule.AddStop(stop_id="433", name="Sherwood Dr. and Culpeper St.", lat="38.31813", lng="-77.432036")
stop_431 = schedule.AddStop(stop_id="431", name="Sherwood Dr. and Adam Ct.", lat="38.317954", lng="-77.430227")
stop_429 = schedule.AddStop(stop_id="429", name="Sherwood and Edwards Dr.", lat="38.317365", lng="-77.425359")