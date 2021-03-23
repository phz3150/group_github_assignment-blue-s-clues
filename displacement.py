def displacement(u_init, t, a) :
    """This function calculates the total displacement of a body
    during a time interval t, when the body has initial speed
    u_init and a constant acceleration a.
    Input: initial speed u_init (assuming m/s), time (assuming s),
    acceleration (assuming m/s^2)
    Output: displacement (assuming m)"""
    return (u_init * t) + (0.5 * a * (t ** 2))
