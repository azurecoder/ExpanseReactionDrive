# Expanse Reaction Drive
## Summary
An AI model to help determine spacecraft and orbits in the Expanse Universe

## Features
- orbital map of the solar system in code
- orbital mechanics calculator for planets, moons, and near earth objects
- ability to configure planets and orbits as needed in a JSON file
- can be used to calculate the distance between any two planets and the closest approach date

## To Install
Install the following libraries:

```
pip install requests
```

Currently yields test output that can be checked. I used this site to understand and validate perihelion distances https://whenthecurveslineup.com/2024/04/21/2024-may-8-mars-at-perihelion and get the initial values that I need.
```
Details for Earth: ---->
Closest approach to Sol: (3.0, 2024, 0.9833) and in km:  147,099,594 km
Farthest approach from Sol: (185.5, 2024, 1.0167) and in km:  152,096,164 km
Orbital distance in km on 5th of Feb:  147,480,063 km
Details for Mars: ---->
Closest approach to Sol: (129.0, 2024, 1.3816584) and in km:  206,693,166 km
Farthest approach from Sol: (107.5, 2025, 1.6663416) and in km:  249,281,169 km
Orbital distance in km on 5th of Feb:  244,093,361 km
Details for Jupiter: ---->
Closest approach to Sol: (17.0, 2024, 4.9495244) and in km:  740,438,352 km
Farthest approach from Sol: (358.0, 2029, 5.4584756) and in km:  816,576,372 km
Orbital distance in km on 5th of Feb:  745,692,400 km
```