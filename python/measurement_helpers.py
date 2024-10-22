import math

def abs_humidity(temp, rel_humidity):
    # temp: Temperature in Celsius
    # rel_humidity: Relative humidity % (range 0-100)
    # => absolute humidity in g/m^3
    return vapor_pressure(temp) * rel_humidity * 0.021674 / (273.15 + temp)

def dew_point(temp, rel_humidity):
    # temp: Temperature in Celsius
    # rel_humidity: Relative humidity % (range 0-100)
    # => dew point in Celsius
    v = math.log(rel_humidity / 100 * vapor_pressure(temp) / 611.2)
    return -243.5 * v / (v - 17.67)

def vapor_pressure(temp):
    # temp: Temperature in Celsius
    # => vapor pressure in Pascal
    return 611.2 * math.exp(17.67 * temp / (243.5 + temp))

def air_density(temp, rel_humidity, pressure):
    # temp: Temperature in Celsius
    # rel_humidity: Relative humidity % (range 0-100)
    # pressure: Pressure in Pascal
    # => air density in kg/m^3
    return 1.2929 * 273.15 / (temp + 273.15) * (pressure - 0.3783 * rel_humidity / 100 * vapor_pressure(temp)) / 101300

def calc(temp, rel_humidity, pressure):
    return {"humidity": abs_humidity(temp, rel_humidity),
            "dew": dew_point(temp, rel_humidity),
            "vapor": vapor_pressure(temp),
            "density": air_density(temp, rel_humidity, pressure)}

