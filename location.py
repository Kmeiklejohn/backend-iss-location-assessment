# -*- coding: utf-8 -*-
"""
This program will give the current location of the
internation space station.
"""

__author__ = "kmeiklejohn"
__version__ = "0.1.0"

import turtle
import requests
import time
from pprint import pprint


def astronauts_request():
    resp = requests.get('http://api.open-notify.org/astros.json')
    data = resp.json()
    print("Number of Astronauts {}".format(data['number']))
    for people in data['people']:
        pprint(
            "Astronaut: {}, Craft: {}".format(
                people['name'],
                people['craft']))
    return


def iss_location():
    resp = requests.get('http://api.open-notify.org/iss-now.json')
    data = resp.json()
    data_iss = resp.json()['iss_position']
    data_long = data_iss['longitude']
    data_lat = data_iss['latitude']
    timestamp = data['timestamp']
    pprint(
        "iss_position: longitude: {}, latitude: {}, timestamp: {} ".format(
            data_long,
            data_lat,
            timestamp))

    return data_long, data_lat


def location_map():
    data = iss_location()
    longitude = float(data[0])
    latitude = float(data[1])
    screen = turtle.Screen()
    screen.register_shape("iss.gif")
    screen.setup(720, 365)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.goto(longitude, latitude)
    indy = turtle.Turtle()
    indy.shape('circle')
    indy.color("yellow")
    indy.goto(-86.1581, 39.768403)
    indy_times = iss_indianapolis()
    indy_time_loc = turtle.Turtle()
    indy_time_loc.penup()
    indy_time_loc.goto(-86.1581, 39.768403)
    indy_time_loc.write(indy_times)
    turtle.mainloop()
    return


def iss_indianapolis():
    coords = {'lat': 39.768403, 'lon': -86.1581}
    resp = requests.get(
        'http://api.open-notify.org/iss-pass.json',
        params=coords)

    indy_time = time.ctime(resp.json()['request']['datetime'])
    print "{} is the next time it will pass over Indianapolis".format(
        indy_time)
    return indy_time


def main():
    """ Main entry point of the app """
    astronauts_request()
    iss_indianapolis()
    iss_location()
    location_map()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
