# measurement_server

A Simple JSON REST API for a database of scientific measurements taken at various locations.

## Execution

1. Install dependencies

```bash
pip install Flask Flask-Jsonpify Flask-RESTful SQLAlchemy
```

2. Start server

```bash
python measurement_server.py
# Server now running on port 9000
```

## API reference

### `/area` - List all areas

Returns an array of every Area in the database.

#### Example usage

```json
// GET /area
[
  {"area_id": 1, "name": "Grand Canyon", "lat": 30, "long": 20},
  {"area_id": 2, "name": "Boca Raton", "lat": 50, "long": 40},
  {"area_id": 3, "name": "Kennesaw", "lat": 70, "long": 60},
  {"area_id": 4, "name": "Mount Hood", "lat": 90, "long": 80},
  {"area_id": 5, "name": "Mount Rainer", "lat": 121.5, "long": 46.5},
  {"area_id": 6, "name": "Saint Olaf", "lat": 93, "long": 44},
  {"area_id": 7, "name": "Mount St. Helens", "lat": 122, "long": 46}
]
```

#### Area object

| Property  | Type    | Value                                   |
| --------- | ------- | --------------------------------------- |
| `area_id` | integer | Id                                      |
| `name`    | string  | The name of the area                    |
| `lat`     | number  | The latitude (in degrees) of this area  |
| `long`    | number  | The longitude (in degrees) of this area |

### `/area/<area_id>/location` - List locations in area

Returns an array of Locations which match the given `area_id`.

#### Example usage

```json
// GET /area/1/location
[
  {"loc_id": 11, "name": "South rim", "alt": 200, "area_id": 1},
  {"loc_id": 12, "name": "North rim", "alt": 300, "area_id": 1},
  {"loc_id": 13, "name": "Phantom Ranch", "alt": 100, "area_id": 1}
]
```

#### Location object


| Property  | Type    | Value                                 |
| --------- | ------- | ------------------------------------- |
| `loc_id`  | integer | Unique ID                             |
| `name`    | string  | Name of the location                  |
| `alt`     | number  | Altitude (in feet??)                  |
| `area_id` | integer | The ID of the area the location is in |

### `/location/<loc_id>/measurement` - List measurements for location

Returns an array of Measurements taken in the given location.

#### Example usage

```json
// GET /location/11/measurement
[
  {"m_id": 1100, "loc_id": 11, "val": 44.82004560587978},
  {"m_id": 1101, "loc_id": 11, "val": 38.91602608079564},
  {"m_id": 1102, "loc_id": 11, "val": 44.178163488614025},
  {"m_id": 1103, "loc_id": 11, "val": 46.41919904550956},
  {"m_id": 1104, "loc_id": 11, "val": 46.345502885760894},
  {"m_id": 1105, "loc_id": 11, "val": 43.1501772579135},
  {"m_id": 1106, "loc_id": 11, "val": 44.31037965295677},
  {"m_id": 1107, "loc_id": 11, "val": 41.692298340629186},
  {"m_id": 1108, "loc_id": 11, "val": 43.28018622019225},
  {"m_id": 1109, "loc_id": 11, "val": 39.07856683302732}
]
```

#### Measurement object

| Property | Type    | Value                                                  |
| -------- | ------- | ------------------------------------------------------ |
| `m_id`   | integer | A unique ID for the measurement                        |
| `loc_id` | integer | The ID of the location where the measurement was taken |
| `val`    | number  | The value of the measurement                           |

### `/area/AREA_ID/category` - Get categories for area

#### Example usage

```json
// GET /area/4/category
[
  {"cat_id": 31, "name": "Volcanos", "description": "Areas that are on volcanoes"},
  {"cat_id": 33, "name": "West", "description": "Areas that are in the west"}
]
```

#### Category object

| Property     | Type    | Value                          |
| ------------ | ------- | ------------------------------ |
| `cat_id`     | integer | A unique ID for this category  |
| `name`       | string  | The name of this category      |
| `descripton` | string  | A description of that category |

### `/area/AREA_ID/average_measurement` - Get the average measurement for area

#### Example usage

```json
// GET /area/1/average_measurement
46.26524716693247
```

### `/area/AREA_ID/number_locations` Get the number of locations for area

#### Example usage

```json
// GET /area/1/number_locations
3
```