"""
link:
https://replit.com/@ThanhNguyen117/boilerplate-time-calculator-1#
time_calculator.py
"""


def time_calculator(strt_t, el_t, str_d=None):
    el_d = 0

    wkdays = ["Sunday",
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              ]

    strt_t = strt_t.split(" ")  # seperate start time and am/pm
    strt_t[0] = strt_t[0].split(":")  # seperate start hr and min
    strt_t[0][0] = int(strt_t[0][0])
    strt_t[0][1] = int(strt_t[0][1])

    el_t = el_t.split(":")  # seperate elapsed time hr/min
    el_t[0] = int(el_t[0])  # convert to int
    el_t[1] = int(el_t[1])

    if strt_t[1] == "PM":
        strt_t[0][0] = 12 + strt_t[0][0]

    # Convert elapsed time to elapsed mins
    el_min_tot = (el_t[0] * 60) + el_t[1]
    print(f"Total elapsed minutes: {el_min_tot}")

    # convert start time to elapsed mins
    el_min_strt = (strt_t[0][0] * 60) + strt_t[0][1]
    print(f"Elapsed minutes for start: {el_min_strt}")

    # Zero out start day if elapsed time will equal new day
    if el_min_strt + el_min_tot > 1440:
        el_min_tot = el_min_tot - (1440 - el_min_strt)
        el_d += 1
        f_min = 0

    else:
        f_min = el_min_tot + el_min_strt
        el_min_tot = 0

    print(f"Current time: {f_min}")
    print(f"Elapsed minutes left: {el_min_tot}")

    # If new elapsed time will equal new day
    if el_min_tot != 0:
        # calculate days elapsed
        days = el_min_tot // 1440
        el_min_tot = el_min_tot % 1440
        print(f"Elapsed days: {days + el_d}")
        print(f"Elapsed minutes left: {el_min_tot}")

        # calculate hours elapsed
        hrs = el_min_tot // 60
        el_min_tot = el_min_tot % 60
        print(f"Elapsed hours: {hrs}")
        print(f"Elapsed minutes left: {el_min_tot}")
    else:
        # calculate hours elapsed
        days = 0
        hrs = f_min // 60
        el_min_tot = f_min % 60
        print(f"Elapsed hours: {hrs}")
        print(f"Elapsed minutes left: {el_min_tot}")

    # converting time
    am = False
    pm = False

    if hrs == 0:  # formatting final hours
        final_hr = "12"
        am = True
    elif hrs > 12:
        if hrs == 24:
            am = True
            final_hr = str(12)
        else:
            final_hr = str(hrs - 12)
            pm = True
    elif hrs < 12:
        am = True
        final_hr = str(hrs)
    elif hrs == 12:
        pm = True
        final_hr = str(hrs)

    final_min = str(el_min_tot).zfill(2)

    if days + el_d == 1:  # formating final days elapsed
        final_day = "(next day)"
    elif days + el_d > 1:
        final_day = f"({str(days + el_d)} days later)"
    elif days + el_d < 1:
        final_day = None

    if str_d:  # finding final weekday
        wkday = str_d.title()
        if days + el_d > 7:
            wkday_el = (days + el_d) % 7  # number of elapsed weekday
            str_wkday_indx = wkdays.index(wkday)  # index of starting weekday
            if str_wkday_indx + wkday_el > 7:
                final_wkday = wkdays[(str_wkday_indx + wkday_el) - 7]
            elif str_wkday_indx + wkday_el < 7:
                final_wkday = wkdays[(str_wkday_indx + wkday_el)]
            elif str_wkday_indx + wkday_el == 7:
                final_wkday = wkdays[str_wkday_indx]
        elif days + el_d <= 7:
            str_wkday_indx = wkdays.index(wkday)
            wkday_el = days + el_d
            print(f"elapsed wkday: {wkday_el}")
            print(f"starting weekday index: {str_wkday_indx}")
            if str_wkday_indx + wkday_el < 7:
                final_wkday = wkdays[(str_wkday_indx + wkday_el)]
            elif str_wkday_indx + wkday_el == 7:
                final_wkday = wkdays[(str_wkday_indx + wkday_el) - 7]
        print(f"Final weekday: {final_wkday}")

    if str_d:
        if am:  # create final time
            final_time = f"{final_hr}:{final_min} AM, {final_wkday}"
        elif pm:
            final_time = f"{final_hr}:{final_min} PM, {final_wkday}"
    elif not str_d:
        if am:  # create final time
            final_time = f"{final_hr}:{final_min} AM"
        elif pm:
            final_time = f"{final_hr}:{final_min} PM"

    if final_day:
        final_time = f"{final_time} {final_day}"
    if not final_day:
        final_time = f"{final_time}"

    print(final_time)
    print("-----" * 5)
    return(final_time)


time_calculator("2:59 AM", "24:00", "saturDay")
