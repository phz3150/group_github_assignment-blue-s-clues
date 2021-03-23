def acceleration(u1, u2, t1, t2):
    """Calculates the acceleration of a body using the ratio of the change of a body's 
    speed (u2-u1) over a time span (t2-t1); a = (u2-u1)/(t2-t1) using the body's different 
    speeds u2 and u1 at times t1 and t2"""
    
    a = ( u2 - u1 ) / ( t2 - t1 )
    return a
