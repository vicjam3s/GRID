src
│
├── api
│   └── api.js
│
├── components
│   ├── layout
│   ├── learning
│   ├── flight
│   └── ui
│
├── pages
│   ├── Home.jsx
│   │
│   ├── learning
│   │   ├── Dashboard.jsx
│   │   ├── Subjects.jsx
│   │   ├── SubjectDetail.jsx
│   │   ├── Notes.jsx
│   │   ├── Quiz.jsx
│   │   └── Exam.jsx
│   │
│   └── flight
│       ├── FlightPlanner.jsx
│       ├── RouteBuilder.jsx
│       ├── NavLog.jsx
│       └── WeightBalance.jsx
│
├── hooks
│
├── layouts
│   └── MainLayout.jsx
│
├── router
│   └── router.jsx
│
├── App.jsx
└── main.jsx

GRID
│
├── E-Learning
│   ├── Subjects
│   ├── Notes
│   ├── Practice MCQs
│   └── Mock Exams
│
└──Flight Planner
    │
    ├── Aviation Map
    ├── Aerodrome Database
    ├── Route Planning
    ├── Live Flight Tracking
    ├── Navigation Mode
    └── Saved Routes





 -----------------------------------------------------
|                                                     |
|                    GRID                             |
|                                                     |
|   ┌────────────────┐  ┌──────────────────────────┐  |
|   │                │  │                          │  |
|   │   E-Learning   │  │     Flight Planning      │  |
|   │                │  │                          │  |
|   │ Study modules  │  │ Route builder            │  |
|   │ Practice MCQs  │  │ Aviation map             │  |
|   │ Mock exams     │  │ Live tracking            │  |
|   │                │  │                          │  |
|   │    ENTER →     │  │        ENTER →           │  |
|   │                │  │                          │  |
|   └────────────────┘  └──────────────────────────┘  |
|                                                     |
 -----------------------------------------------------   



|------------------|------------------|
|                  |                  |
|    E-Learning    |  Flight Planning |
|                  |                  |
|  Study modules   |  Interactive map |
|  MCQs            |  Route builder   |
|  Notes           |  Weather layers  |
|                  |                  |
|  [Enter]         |  [Enter]         |
|                  |                  |
|------------------|------------------|

Subjects
│
├── Air Law
├── Meteorology
├── Navigation
├── Radio Navigation
├── Human Performance
├── Mass & Balance


 --------------------
| METEOROLOGY       |
| 48 Topics         |
| 120 Questions     |
|                   |
|   Start Studying  |
 --------------------


  --------------------------------------------------
| Question 12 of 40                     Timer 18:21 |
|--------------------------------------------------|
|                                                  |
| What is the tropopause?                          |
|                                                  |
|  A  Boundary between troposphere and stratosphere|
|  B  Boundary between mesosphere and thermosphere |
|  C  Boundary between ionosphere and exosphere    |
|  D  Boundary between troposphere and mesosphere  |
|                                                  |
|--------------------------------------------------|
| Flag | Previous | Next                           |
 --------------------------------------------------


 -----------------------------------------------------
| Sidebar |                 MAP                      |
|         |                                          |
| Route   |      ✈ Map (Leaflet / Mapbox)            |
| NavLog  |                                          |
| Weather |                                          |
| W&B     |                                          |
|         |                                          |
 -----------------------------------------------------


 ---------------------------------------------------
| Search Bar                                       |
|--------------------------------------------------|
| Sidebar |                MAP                     |
|         |                                        |
| Routes  |                                        |
| Layers  |                                        |
| Nav Log |                                        |
|         |                                        |
 ---------------------------------------------------



User clicks airports.

Example:

HKJK → HKEL → HKML

System generates:

Course
Distance
Wind correction
ETA
Fuel burn


src
│
├── components
│   ├── layout
│   │     Navbar.jsx
│   │     Sidebar.jsx
│   │
│   ├── learning
│   │     SubjectCard.jsx
│   │     QuizCard.jsx
│   │
│   ├── flight
│   │     MapView.jsx
│   │     RoutePanel.jsx
│   │     NavLog.jsx
│
├── pages
│   ├── Home.jsx
│   ├── Learning.jsx
│   ├── FlightPlanner.jsx
│
├── styles


To make GRID look seriously modern, use:

glassmorphism
soft shadows
rounded corners
minimal text




Map must support layers like:

Airspaces
Control zones
Aerodromes
Navigation aids
Cities
Terrain
Flight routes
Weather
Aircraft position



Best react libraries:

Mapbox GL
or
Leaflet(Simpler)



When clicking an airport on the map:

Panel opens:

HKJK – Jomo Kenyatta Intl

Elevation: 5330 ft

Runways
---------
06/24 – 4117m

Frequencies
-----------
Tower: 118.7
Ground: 121.9
ATIS: 127.2

Airspace
--------
Class C CTR


-Data sources later could include:

Kenya Civil Aviation Authority

OpenStreetMap

OpenAIP


User should be able to search:

HKJK
Nairobi
Mount Kenya
Lake Victoria
Malindi


Search categories:

Aerodromes
Cities
Towns
Physical features
Navaids
Waypoints

User should be able to save routes like:

Training Flight
HKJK → HKEL

or

Coastal Route
HKJK → HKMO → HKML

Database stores:

route_name
waypoints
distance
created_by


Live Flight Tracking
This requires ADS-B data.
Possible sources:

Flightradar24

OpenSky Network




Aircraft position updates:

Latitude
Longitude
Altitude
Heading
Groundspeed

Display aircraft icon moving on map.





Navigation Mode (In-Flight)

When flying:

Aircraft GPS position
Route line
Distance to waypoint
Groundspeed
ETA

Example display:

Distance to next waypoint: 24 NM
Groundspeed: 115 KT
ETA: 13:42


Map Layers

You will want toggles:

✔ Aerodromes
✔ Control Zones
✔ Airspaces
✔ Cities
✔ Terrain
✔ Waypoints



--Important Warning

Your project will eventually need real aviation datasets. Thes come from AIPS.

For Kenya you will likely need:

Aerodrome coordinates
Runways
Frequencies
Airspaces
Waypoints




Frontend Usage for PDF loading...
Option 1 — Open PDF directly
window.open(file_url)

Option 2 — Embed into a tile or card..
<iframe src="PDF_URL" width="100%" height="600px"></iframe>


POST /api/progress/submit/

{
  "course_id": 1,
  "subject_id": 3,
  "answers": [
    {"question_id": 10, "selected_option": "A"},
    {"question_id": 11, "selected_option": "C"}
  ]
}

GRID_BACKEND/
├── core/                  # Main settings and wsgi
├── api/                   # The entry point for your React frontend
│   ├── serializers.py     # Converts PostGIS objects to GeoJSON
│   └── views.py           # Handles requests like "Get airports near me"
├── aeronautical/          # The "World" data (Static)
│   ├── models.py          # Airport, Runway, Airspace models
│   └── management/        # Scripts to import KCAA data from CSV/PDF
├── operations/            # User-specific data (Dynamic)
│   ├── models.py          # FlightPlan, Aircraft, Logbook models
│   └── calculations.py    # Logic for Heading, Wind Correction, Fuel
└── static_assets/         # For "Charts" (PDFs, Diagrams)