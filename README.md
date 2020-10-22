# Squirrel Tracker: a visulization web-application of tracking squirrels

## Introduction
We used Django, a web-application tools in python which can manage import, modify data, to construct a **Squirrel Tracker** with the  visualization of sightings of squirrels found in Central Park, Manhattan, New York.

## Data
We use squirrel data [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which can be download [**here**](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).

## Management Commands
A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.
```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## Views

### Map
A view that shows a map that displays the location of the squirrel sightings on an [**OpenStreets map**](https://www.openstreetmap.org/about/) by [**leafletjs**](https://leafletjs.com/) library for plotting.

Methods Supported: GET
>Located at: /map

### Sightings
A view that lists all squirrel sightings with links to view each sighting, and also have a single link to the “add” sighting view.

Methods Supported: GET
>Located at: /sightings

### Update
A view to update a particular sighting.

Methods Supported: GET & POST
> Located at: /sightings/<<unique-squirrel-id>unique-squirrel-id>

### Add
A view to create a new sighting.

Methods Supported: GET & POST
> Located at: /sightings/add

### Stats

Method: GET
>Located at: /sightings/stats

## Contributors

Group Name: **Woody & Heather**

Section: 1

Contributors: Yue Zou, Zongqian Wu

UNIs: [yz3936, zw2679]
