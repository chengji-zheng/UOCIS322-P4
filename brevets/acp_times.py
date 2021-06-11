"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
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
    
    max_speeds = [34, 32, 30, 28, 28]                           # A list of max_speeds by different distances
    step = 200                                                  # Chunk every max_speed by a step of 200km distaces
    time = 0

    # Handling distance that longer than 200 km first
    if control_dist_km > step:
        #Iterating through every 200 km step with corresponding speed in the list above
        for i in range(max_speeds):
            # Adding time in minutes and store the time in time
            time += round(((step / max_speeds[i]) * 60), 0)
    # Else branch - handling distance that less or equal to 200 km (in this project, which is exact 200).
    time += round(((step / max_speeds[0]) * 60), 0)
    
    # Do everything in 1 line and return it
    return  brevet_start_time.shift(minutes=time).isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
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
  
    min_speeds = [15, 15, 15, 11.428, 11.428]
    step = 200                                                  # Chunk every min_speed by a step of 200km distaces
    time = 0                                                    # Still in minutes
    
    # First Case - if any control_point(s) set less than 60 km, the closing_time + 1 hour.
    if control_dist_km < 60:
        time += 60 
    # The rest of logic seems similar to the start_time
    else:
        if control_dist_km > step:
            for j in range(min_speeds):
                time += round(((step / min_speeds[j]) * 60), 0)
        time += round(((step / min_speeds[0]) * 60), 0)    
    
    return brevet_start_time.shift(minutes=time).isoformat()
