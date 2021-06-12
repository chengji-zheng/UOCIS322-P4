"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import logging


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, dist, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    max_speeds = [34, 32, 30, 28, 28, 26]           # A list of max_speeds by different distances
    step = 200                                      # Chunk every max_speed by a step of 200km distaces
    time = 0                                        # Time stored in minutes
    if control_dist_km < 0:
        return "Error"
    if control_dist_km >= dist:                     # Handles the bad control points that set outside the brevets, it will return an error message on the client side
        control_dist_km = dist
    for i in range(len(max_speeds)):                
        if control_dist_km > step:                  # Handles the control points that set between 2 chunks.
            time += round(((step / max_speeds[i]) * 60), 0)
            control_dist_km -= step
        else:
            time += round(((control_dist_km / max_speeds[i]) * 60), 0)
            return  brevet_start_time.shift(minutes=time)


def close_time(control_dist_km, dist, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    min_speeds = [15, 15, 15, 11.428, 11.428, 13.333]
    step = 200                                                  # Chunk every min_speed by a step of 200km distaces
    time = 0                                                    # Still in minutes               
    
    if control_dist_km < 0:
        return "Error"
    if control_dist_km >= dist:                     # Handles the bad control points that set outside the brevets, it will return an error message on the client side
        control_dist_km = dist
    for j in range(len(min_speeds)):
        if control_dist_km > step:
            time += round(((step / min_speeds[j]) * 60), 0)
            control_dist_km -= step
        else:
            # Be careful the special rule that when control points located at less than 60 km.
            if control_dist_km < 60:
                time += round((((control_dist_km / 20) + 1) * 60), 0)
            else:
                time += round(((control_dist_km / min_speeds[j]) * 60), 0)
            return  brevet_start_time.shift(minutes=time)