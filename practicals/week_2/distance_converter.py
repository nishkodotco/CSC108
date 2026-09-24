def feet_to_meter(f: float) -> float:
    '''Return the number of meters equivalent to f feet.
    >>> feet_to_meter(10.0)
    3.048
    '''
    return f * 0.3048

def meter_to_feet(m: float) -> float:
    '''Return the number of feet equivalent to m meters.
    >>> meter_to_feet(16.0)
    52.4934
    '''
    return m * 3.28084

print(feet_to_meter(10.0))