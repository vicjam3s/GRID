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
└── Flight Planning
    ├── Map
    ├── Route Builder
    ├── Weather
    ├── Weight & Balance
    └── Navigation Log





 -----------------------------------------------------
|                                                     |
|              GRID Aviation Platform                 |
|                                                     |
|   [ E-Learning ]            [ Flight Planning ]     |
|                                                     |
|  Study for aviation exams     Plan real flights     |
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