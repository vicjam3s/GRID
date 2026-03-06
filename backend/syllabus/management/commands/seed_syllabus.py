from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject, Topic, Subtopic


PPL_SYLLABUS = {
    "Air Law": {
        "01 International Agreements & Organizations": [
            "Chicago Convention",
            "ICAO Structure",
            "National Aviation Law (Kenya)",
        ],
        "02 Personnel Licensing (ICAO Annex 1)": [
            "PPL Privileges & Limitations",
            "Medical Certification",
        ],
        "03 Rules of the Air (ICAO Annex 2)": [
            "General Rules",
            "Avoidance of Collisions",
            "VFR Weather Minima",
        ],
        "04 Air Traffic Services (ICAO Annex 11)": [
            "Airspace Classification",
            "ATS Services",
        ],
        "05 Aerodromes (ICAO Annex 14)": [
            "Markings & Lighting",
            "Aerodrome Signals",
        ],
    },

    "Operational Procedures": {
        "01 General Requirements": [
            "ICAO Annex 6 (Operation of Aircraft)",
            "Operator Responsibilities (Safe conduct of flight)",
            "Documents to be Carried (The \"Checklist\" of certificates)",
        ],

        "02 Special Environments and Hazards": [
            "Wake Turbulence (Vortices, separation times)",
            "Windshear and Microburst (Recognition and recovery)",
            "Contaminated Runways (Hydroplaning, braking action)",
            "Bird Strike Hazards",
        ],

        "03 Emergency Procedures": [
            "Engine Failure (Standard restart and forced landing)",
            "Fires (Engine, Cabin, Electrical, Wing)",
            "Ditching (Water landing techniques)",
            "Depressurization (Oxygen requirements)",
        ],

        "04 Search and Rescue (SAR)": [
            "The Three Phases (INCERFA, ALERFA, DETRESFA)",
            "Visual Signals (Ground-to-Air codes)",
            "Emergency Locators (ELT frequencies and usage)",
        ],
    },

    "Human Performance": {
        "01 Basic Physiology": [
            "The Atmosphere and Gases (Composition: 78% Nitrogen, 21% Oxygen)",
            "Gas Laws (Dalton’s: Partial pressure; Boyle’s: Gas expansion)",
            "Pressure Changes (Trapped gas in ears, sinuses, and gut)",
            "Respiratory System (Lungs, Alveoli, Hemoglobin transport)",
            "Hypoxia Types (Hypoxic, Stagnant, Hypemic, Histotoxic)",
            "Hyperventilation (Loss of CO₂, alkalosis)",
            "Carbon Monoxide (Symptoms and disposal time – up to 48 hours)",
            "Circulatory System (Blood pressure, G-forces, G-LOC)",
            "Health Factors (Smoking, Obesity, Exercise)",
        ],

        "02 Sensory Systems": [
            "Vision – Functional Anatomy (Cones for day/color, Rods for night)",
            "Night Vision (Dark adaptation: 30 minutes; Empty field myopia)",
            "Scanning Techniques (Short eye movements, 10° sectors)",
            "The Ear (Outer, Middle, Inner, Cochlea)",
            "Balance (Vestibular system: Semicircular canals and Otoliths)",
            "Vestibular Illusions (The Leans, Coriolis illusion, Graveyard spin)",
            "Visual Illusions (Autokinesis, False horizons, Black hole approach)",
        ],

        "03 Health and Hygiene": [
            "Medication (Side effects of common drugs e.g. Aspirin, Antihistamines)",
            "Alcohol (8-hour rule vs KCAA 12-hour preference; 0.02% limit)",
            "Blood Donation (Wait 24–48 hours before flying)",
            "Circadian Dysrhythmia (Jet lag)",
            "Sleep and Fatigue (Acute vs Chronic fatigue)",
            "IMSAFE Checklist (Illness, Medication, Stress, Alcohol, Fatigue, Emotion/Eating)",
        ],

        "04 Basic Psychology": [
            "Information Processing (Perception and Memory)",
            "Memory Types (Short-term / Working vs Long-term)",
            "Attention (Selective vs Divided attention)",
            "Human Error Models (SHEL Model)",
            "Swiss Cheese Model (James Reason)",
            "Decision Making (Risk assessment and judgment)",
            "Hazardous Attitudes (Anti-authority, Impulsivity, Invulnerability, Macho, Resignation)",
            "Stress Management (Arousal levels and performance)",
        ],
    },

    "Principles of Flight": {
        "01 Subsonic Aerodynamics": [
            "Laws of Motion (Newton’s 1st, 2nd, and 3rd Laws)",
            "Bernoulli’s Principle (Static vs Dynamic pressure)",
            "Venturi Effect (Velocity increase, Pressure decrease)",
            "Air Properties (Density, Pressure, Temperature, Humidity)",
            "Airfoil Geometry (Chord line, Camber, Leading/Trailing edge)",
            "Angle of Attack (Alpha – α) vs Angle of Incidence",
            "Stagnation Point (Flow separation points)",
            "Center of Pressure (CP movement with Alpha)",
            "Lift (Coefficient of Lift CL, Surface area, Velocity squared)",
            "Weight (Gravity, Centre of Gravity location)",
            "Thrust (Propeller wash, Slipstream effect)",
            "Drag (Drag equation, CD vs CL curves)",
        ],

        "02 Drag Phenomena": [
            "Parasite Drag – Form Drag (Shape/Profile of the object)",
            "Parasite Drag – Skin Friction (Boundary layer: Laminar vs Turbulent)",
            "Parasite Drag – Interference Drag (Wing-to-fuselage intersections)",
            "Induced Drag (Wingtip vortices and downwash)",
            "Aspect Ratio (High AR vs Low AR efficiency)",
            "Ground Effect (Reduction of induced drag within one wingspan)",
        ],

        "03 Stability and Control": [
            "Static Stability (Positive, Neutral, Negative)",
            "Longitudinal Stability (Pitch – Stabilizer and Elevator)",
            "Lateral Stability (Roll – Dihedral, High-wing vs Low-wing)",
            "Directional Stability (Yaw – Vertical fin and Rudder)",
            "Dynamic Stability (Damped vs Divergent oscillations)",
            "Spiral Instability vs Dutch Roll",
            "Aerodynamic Balance (Horns, Inset hinges)",
            "Mass Balance (Weights to prevent control flutter)",
            "Adverse Yaw (Differential and Frise ailerons)",
        ],

        "04 Stalling and Spinning": [
            "Critical Angle of Attack (Typically 15°–18°)",
            "Boundary Layer Separation (Turbulent wake)",
            "Stall Warnings (Buffeting, Reed horns)",
            "Wing Drop (Asymmetric stalling)",
            "Spin Requirements (Stalled wing with yaw and autorotation)",
            "Spin Phases (Incipient, Developed, Recovery)",
            "Standard Spin Recovery (PARE: Power, Ailerons, Rudder, Elevator)",
        ],

        "05 Flight Mechanics and Loading": [
            "Turns (Centripetal force and horizontal component of lift)",
            "Load Factor (G-load in turns: n = 1 / cos θ)",
            "Climbing and Descending Flight (Forces in non-level flight)",
            "V–n Diagram (Structural limits and flight envelope)",
            "Limit Load vs Ultimate Load",
            "Va – Maneuvering Speed (Definition and calculation)",
            "Vne – Never Exceed Speed (Structural failure limit)",
        ],
    },

    "Airframe and Structures": {
        "01 Structural Design": [
            "Stress Types (Tension, Compression, Torsion, Shear, Bending)",
            "Construction Methods (Monocoque, Semi-monocoque, Truss/Pruss)",
            "Major Components (Fuselage, Wings, Empennage, Undercarriage)",
        ],

        "02 Materials": [
            "Alloys (Aluminum-copper / Duralumin)",
            "Composites (Glass fiber, Carbon fiber, resins)",
            "Corrosion (Stress corrosion, Galvanic / Dissimilar metal)",
        ],

        "03 Primary and Secondary Controls": [
            "Control Surfaces (Ailerons, Elevator, Rudder)",
            "Trim Systems (Fixed tab, Adjustable tab, Anti-servo)",
            "Flaps (Plain, Split, Slotted, Fowler)",
        ],

        "04 Landing Gear and Braking": [
            "Configurations (Taildragger vs Tricycle)",
            "Shock Absorption (Oleo struts, Bungee, Spring steel)",
            "Braking Systems (Hydraulic disc brakes, Master cylinders)",
        ],
    },

    "Powerplant (Piston Engines)": {
        "01 Engine Architecture": [
            "Components (Cylinders, Pistons, Connecting rods, Crankshaft, Camshaft)",
            "The 4-Stroke Cycle (Otto Cycle: Suck, Squeeze, Bang, Blow)",
            "Valve Operation (Timing, Overlap, Tappet clearances)",
        ],

        "02 Fuel and Induction": [
            "Carburetion (Venturi principle, Mixture control)",
            "Carb Icing (Impact ice, Throttle ice, Fuel evaporation ice)",
            "Fuel Injection (Advantages vs carbureted engines)",
        ],

        "03 Ignition and Electrical Power": [
            "Dual Magnetos (Independent from aircraft electrical system)",
            "Spark Plugs (Fouling, Heat ranges)",
            "Ignition Timing (Advance/Retard, Detonation, Pre-ignition)",
        ],

        "04 Lubrication and Cooling": [
            "Oil System (Wet vs Dry sump, Pressure relief valves, Viscosity)",
            "Air Cooling (Baffles, Cooling fins, Cowl flaps)",
        ],

        "05 Propellers": [
            "Propeller Principles (Blade angle, Angle of Attack, Blade twist)",
            "Constant Speed Propellers (Governor, Flyweights, Oil pressure control)",
        ],
    },

    "DC Electrical Systems": {
        "01 Fundamentals and Generation": [
            "Basic Units (Voltage, Amperage, Resistance, Ohms Law)",
            "Alternators vs Generators (AC vs DC production)",
            "Voltage Regulation (Maintaining ~28V in a 24V system)",
        ],

        "02 Storage and Batteries": [
            "Lead-Acid vs Nickel-Cadmium (Ni-Cad)",
            "Battery Capacity (Amp-hours)",
            "Thermal Runaway (Specifically for Ni-Cad batteries)",
        ],

        "03 Distribution and Protection": [
            "Busbars (Primary, Avionics, Essential)",
            "Circuit Breakers vs Fuses (Resetting vs Replacing)",
            "Master Switch (Single vs Split / Double rocker)",
        ],

        "04 Monitoring and Faults": [
            "Ammeter vs Loadmeter (Charging indication vs Total load)",
            "Over-voltage Sensors",
            "Electrical Fire Procedures (Isolate the source)",
        ],
    },

    "Instrumentation": {
        "01 The Pitot-Static System": [
            "Pitot Probe (Total / Stagnation pressure)",
            "Static Port (Ambient / Atmospheric pressure)",
            "Altimeter (Aneroid wafers, Sub-scale settings, Hysteresis)",
            "Airspeed Indicator (Diaphragm, Differential pressure, Color arcs)",
            "Vertical Speed Indicator (VSI) (Calibrated leak, Lag error)",
        ],

        "02 Gyroscopic Instruments": [
            "Gyro Principles (Rigidity in space, Precession)",
            "Power Sources (Engine-driven vacuum pump vs Electrical)",
            "Attitude Indicator (Artificial horizon / Earth gyro)",
            "Heading Indicator (Directional gyro, Apparent drift)",
            "Turn Coordinator / Turn Indicator (Rate of turn, Slip / Skid ball)",
        ],

        "03 Magnetism and the Compass": [
            "Earth’s Magnetic Field (Dip, Variation)",
            "Compass Construction (Pivot, Liquid damping, Expansion bellows)",
            "Compass Errors (Deviation, Acceleration / Deceleration, Turning)",
        ],
    },

    "Mass and Balance": {
        "01 Fundamentals and Terminology": [
            "Mass Definitions (BEM, DOM, ZFM, MTOM, MLM)",
            "The Datum and Arms (Reference line and distance from datum)",
            "Moments (Weight × Arm)",
        ],

        "02 Loading and Calculations": [
            "Floor Loading Limits (PSI / kg per square meter)",
            "Baggage Compartment Limits",
            "CG Calculation (Total moment ÷ Total mass)",
        ],

        "03 CG Limits and Shifting": [
            "Forward and Aft Limits (Stability vs Controllability)",
            "Mass Addition and Removal (Effect on new CG)",
            "Mass Shifting Formula",
        ],
    },

    "Aircraft Performance": {
        "01 Takeoff and Landing Theory": [
            "Distances (TORA, TODA, ASDA, LDA)",
            "Balanced Field Concept (Clearway / Stopway)",
            "Ground Effect (Reduced induced drag during rotation)",
        ],

        "02 Performance Charts (The Graphs)": [
            "Reading Nomograms (Start at Temperature → Pressure Altitude → Weight)",
            "Wind Correction (Headwind vs Tailwind components)",
            "Surface Correction (Grass, Slope, Contamination)",
        ],

        "03 Climb and Cruise Performance": [
            "Vx (Best angle) vs Vy (Best rate)",
            "Service Ceiling vs Absolute Ceiling",
            "Fuel Flow vs Power Settings (RPM / Mixture)",
        ],
    },

    "Flight Planning": {
        "01 VFR Navigation Planning": [
            "Chart Work (Plotting tracks, measuring distances)",
            "Magnetic Variation (True vs Magnetic tracks)",
            "Wind Correction (Using CRP-1 for Heading and Groundspeed)",
        ],

        "02 Fuel Planning and Policy": [
            "Fuel Components (Taxi, Trip, Contingency, Reserve)",
            "Endurance Calculations (Safe time in the air)",
            "Fuel Density and Weights (Avgas vs Jet A1)",
        ],

        "03 The Operational Flight Plan (OFP)": [
            "The Nav Log (Step-by-step waypoint recording)",
            "Point of Equal Time (PET) and Point of No Return (PNR)",
            "Safety Altitudes (Minimum Safe Altitude – MSA)",
        ],

        "04 ICAO Flight Plan (CA-48)": [
            "Form Submission Procedures (Filing, Opening, Closing)",
            "Item Codes (Equipment, Wake Turbulence, Endurance)",
        ],
    },

    "General Navigation": {
        "01 Earth and Geometry": [
            "Coordinate System (Latitude/Longitude, Great Circles, Rhumb Lines)",
            "Distance Units (Nautical Miles vs Statute Miles vs Kilometers)",
            "Directions (True, Magnetic, Compass, and Grid North)",
        ],

        "02 Aviation Charts": [
            "Projections (Lambert’s Conformal vs Mercator)",
            "Topography (Relief, Spot heights, Contours)",
            "Map Scale (1:500,000 Sectional vs 1:1,000,000)",
        ],

        "03 Time and Astronomy": [
            "UTC (Zulu) vs Local Time (LMT)",
            "Arc to Time Conversion (15° equals 1 hour)",
            "Sunrise and Sunset (Civil twilight definitions)",
        ],

        "04 The Dead Reckoning (DR) Triangle": [
            "Triangle of Velocities (Heading, Track, Wind)",
            "Vector Math (Wind side of the CRP-1)",
            "Circular Slide Rule (Calculator side of the CRP-1)",
        ],

        "05 The 1-in-60 Rule": [
            "Track Error Calculations (Angle off vs Angle to regain)",
            "Estimating ETAs (Groundspeed corrections)",
        ],
    },

    "Radio Navigation": {
        "01 Basic Radio Theory": [
            "Properties of Radio Waves (Frequency, Wavelength, Phase)",
            "Wave Propagation (Ground, Sky, and Space waves)",
            "Frequency Bands (LF, MF, VHF, UHF)",
        ],

        "02 Point-to-Point Navigation": [
            "VDF (Direction Finding: QDM, QDR, QTE)",
            "NDB / ADF (Non-Directional Beacon: Relative vs Magnetic bearings)",
            "VOR (VHF Omnidirectional Range: Radials and Phase comparison)",
        ],

        "03 Distance and Precision Aids": [
            "DME (Distance Measuring Equipment: Slant range)",
            "ILS (Instrument Landing System: Localizer and Glide path)",
            "Marker Beacons (Outer, Middle, Inner)",
        ],

        "04 Satellite and Radar": [
            "GNSS / GPS (Segments, RAIM, Errors)",
            "SSR (Secondary Surveillance Radar: Transponder codes)",
            "TCAS (Traffic Collision Avoidance System basics)",
        ],
    },

    "Meteorology": {
        "01 The Atmosphere": [
            "Atmospheric Layers",
            "Temperature Lapse Rates",
            "ISA Standard Atmosphere",
            "Pressure Systems",
            "Atmospheric Features",
            "Isobars",
        ],

        "02 Wind and Air Motion": [
            "Pressure Gradient Force",
            "Coriolis Force",
            "Surface Friction",
            "Sea and Land Breezes",
            "Anabatic and Katabatic Winds",
            "Mountain Waves",
            "Wind Shear",
        ],

        "03 Thermodynamics and Moisture": [
            "Humidity and Dew Point",
            "Latent Heat",
            "Adiabatic Processes",
            "Stable Air",
            "Unstable Air",
        ],

        "04 Clouds and Precipitation": [
            "High-Level Clouds",
            "Medium-Level Clouds",
            "Low-Level Clouds",
            "Vertical Development Clouds",
            "Precipitation Types",
        ],

        "05 Visibility and Icing": [
            "Radiation Fog",
            "Advection Fog",
            "Mist, Haze, and Smoke",
            "Rime Ice",
            "Clear Ice",
            "Hoar Frost",
        ],

        "06 Fronts and Air Masses": [
            "Air Mass Types",
            "Warm Fronts",
            "Cold Fronts",
            "Occluded and Stationary Fronts",
        ],

        "07 Weather Documentation and Coding": [
            "METAR",
            "TAF",
            "SPECI",
            "Significant Weather Charts",
            "Upper Wind and Temperature Charts",
            "Satellite and Radar Imagery",
        ],
    },

    "Communications (Radiotelephony)": {
        "01 VHF Propagation and Theory": [
            "Radio Wave Properties",
            "VHF Frequency Spectrum",
            "Radio Wave Propagation",
            "Factors Affecting Range",
        ],

        "02 General Operating Procedures": [
            "Microphone Technique",
            "Transmission Structure",
            "Standard Prowords",
            "Phonetic Alphabet",
            "Numbers Pronunciation",
            "Time and Frequency Use",
        ],

        "03 VFR Phraseology and Standard Calls": [
            "Aerodrome Control Procedures",
            "Circuit Calls",
            "En-Route Position Reporting",
            "Flight Information Service (FIS)",
            "Arrival and Landing Procedures",
        ],

        "04 Emergency and Urgency Procedures": [
            "Distress Calls (MAYDAY)",
            "Urgency Calls (PAN-PAN)",
            "Loss of Communication Procedures",
            "Emergency Frequencies",
            "Visual ATC Signals",
        ],

        "05 Radionavigation and Surveillance": [
            "Navigation Aid Identification",
            "Radar Services",
            "SSR Transponder Modes",
        ],
    },

}


CPL_SYLLABUS = {
    "Air Law": {
      "01 International Agreements and Organizations": [
            "Chicago Convention (Articles and Annexes)",
            "International Civil Aviation Organization (ICAO)",
            "Tokyo, Hague and Montreal Conventions",
            "Freedoms of the Air",
        ],

        "02 Airworthiness and Registration": [
            "Aircraft Nationality and Registration",
            "Certificate of Airworthiness",
            "Maintenance Documentation and Logbooks",
        ],

        "03 Personnel Licensing": [
            "CPL Privileges and Limitations",
            "Medical Requirements (Class 1)",
            "Recent Experience Requirements",
        ],

        "04 Rules of the Air (Annex 2)": [
            "General Rules and Right-of-Way",
            "Visual Flight Rules (VFR)",
            "Instrument Flight Rules (IFR)",
            "Signals and Interception Procedures",
        ],

        "05 Air Traffic Services and Airspace": [
            "Airspace Classification (A–G)",
            "Air Traffic Services (ATC, FIS, Alerting)",
            "Altimeter Setting Procedures",
            "Separation Minima",
        ],

        "06 Aerodromes (Annex 14)": [
            "Aerodrome Data and Declared Distances",
            "Visual Aids and Lighting",
            "Rescue and Fire Fighting Services",
        ],

        "07 Accident Investigation and Search and Rescue": [
            "Accident Notification and Reporting",
            "Search and Rescue Phases",
        ],
    },
    
    "Operational Procedures": {
        "01 General Requirements": [
            "ICAO Annex 6 Overview",
            "Operational Certification (AOC and Operations Manual)",
            "Operator Supervision and Safety Management Systems (SMS)",
        ],

        "02 Special Operational Procedures and Hazards": [
            "Icing Conditions (Ground and In-Flight)",
            "Wake Turbulence",
            "Windshear and Microburst",
            "Bird Strike",
            "Volcanic Ash Operations",
        ],

        "03 Emergency Procedures": [
            "Fire and Smoke Procedures",
            "Emergency Evacuation",
            "Ditching Procedures",
            "Decompression and Emergency Descent",
        ],

        "04 All-Weather Operations": [
            "Low Visibility Operations (LVO)",
            "Aerodrome Operating Minima",
            "Required Visual References",
        ],

        "05 Long Range and Polar Operations": [
            "MNPS and RVSM",
            "ETOPS / EDTO",
        ],

        "06 Security and Dangerous Goods": [
            "Aviation Security Procedures",
            "Dangerous Goods Regulations",
        ],
    },
    
    "Human Performance and Limitations": {
        "01 Human Factors Basic Concepts": [
            "Human Factors in Aviation (SHEL Model)",
            "Accident Statistics and Human Error",
            "Flight Safety Concepts (Swiss Cheese Model)",
        ],

        "02 Aviation Physiology and Health Maintenance": [
            "Respiratory System (Hypoxia, Hyperventilation)",
            "Circulatory System (G-forces, G-LOC, Blackout)",
            "Health and Hygiene (Diet, Exercise, Alcohol, Drugs)",
            "Tropical Medicine Considerations",
            "Toxic Hazards (Carbon monoxide, Fuel vapors, De-icing fluids)",
        ],

        "03 Man and Environment": [
            "Vision (Rods, Cones, Night vision)",
            "Hearing and Balance (Vestibular system)",
            "Spatial Disorientation (Leans, Coriolis, Graveyard spin)",
            "Visual Illusions",
        ],

        "04 Aviation Psychology": [
            "Information Processing (Perception, Attention, Memory)",
            "Human Error and Reliability",
            "Decision Making Models (DODAR)",
            "Stress and Fatigue Management",
        ],

        "05 Crew Resource Management (CRM)": [
            "Communication and Assertiveness",
            "Leadership and Followership",
            "Situational Awareness",
        ],

        "06 Threat and Error Management (TEM)": [
            "Threat Identification",
            "Error Management Strategies",
        ],
    },

    "Principles of Flight": {
        "01 Subsonic Aerodynamics": [
            "Basic Laws (Newton’s Laws, Continuity, Bernoulli)",
            "Airflow and Boundary Layer",
            "Lift Generation (Angle of Attack, CL, Stall)",
            "Drag Forces (Induced and Parasite drag)",
        ],

        "02 High-Speed Aerodynamics": [
            "Speed of Sound and Mach Number",
            "Compressibility and Critical Mach",
            "Shock Waves and Mach Effects",
            "High-Speed Design Features (Sweepback, Supercritical airfoils)",
        ],

        "03 Stability": [
            "Static Stability (Longitudinal, Lateral, Directional)",
            "Dynamic Stability (Phugoid, Dutch Roll, Short period)",
            "Centre of Gravity Effects (Neutral point, Static margin)",
        ],

        "04 Control": [
            "Primary Controls (Aileron, Elevator, Rudder effectiveness)",
            "Secondary Controls (Flaps, Slats, Spoilers)",
            "Balance and Trim Systems",
        ],

        "05 Flight Mechanics": [
            "Forces in Climb and Descent",
            "Forces in a Turn (Load factor, Radius)",
            "Stalling and Spinning",
        ],

        "06 Limitations": [
            "Maneuvering Envelope (V–n diagram, Gust loads)",
            "Structural Limits (Limit load, Ultimate load, Safety factors)",
        ],
    },

   "Airframes": {
        "01 System Design, Loads and Stresses": [
            "Loads and Combination Loadings (Static, Dynamic, Cyclic)",
            "Stress and Strain (Tension, Compression, Shear, Bending, Torsion)",
            "Structural Design Concepts (Safe-life, Fail-safe, Damage-tolerant)",
            "Material Properties (Aluminium alloys, Composites, Corrosion types)",
        ],

        "02 Airframe Construction": [
            "Fuselage Construction (Monocoque, Semi-monocoque, Frames, Stringers, Longerons)",
            "Wing Construction (Spars, Ribs, Skin, Torsion box, Wing-tip design)",
            "Stabilizing Surfaces (Fin, Stabilizer, Tailplane construction)",
            "Control Surface Construction (Mass balance, Aerodynamic balance)",
            "Structural Assembly (Bolts, Rivets, Bonding, Sandwich construction)",
        ],

        "03 Hydraulics": [
            "Hydromechanics (Pascal’s Law, Incompressibility)",
            "Hydraulic Fluids (Mineral-based, Synthetic Skydrol)",
            "System Components (Reservoirs, Pumps, Accumulators, Selectors, Filters)",
            "Monitoring and Protection (Pressure relief, Fuses, Priority valves)",
        ],

        "04 Landing Gear, Wheels, Tyres and Brakes": [
            "Landing Gear Types (Nose-wheel, Tail-wheel, Retractable logic)",
            "Shock Absorbers (Oleo-pneumatic operation)",
            "Wheels and Tyres (Thermal plugs, Ply ratings, Hydroplaning)",
            "Braking Systems (Multi-disc, Anti-skid, Auto-brake, Emergency air)",
        ],

        "05 Flight Controls": [
            "Primary Controls (Aileron, Elevator, Rudder actuation)",
            "Secondary Controls (Flaps, Slats, Spoilers, Speed brakes)",
            "Trimming Systems (Trim tabs, Balance tabs, Stabilizer trim)",
            "Fly-by-Wire Basics (Signal transmission, Redundancy logic)",
        ],

        "06 Pneumatics and Pressurization": [
            "Pneumatic Sources (Engine bleed, APU, Ground source)",
            "Air Conditioning Systems (Air cycle machine, Heat exchangers, Water separators)",
            "Pressurization Systems (Outflow valves, Safety valves, Negative relief)",
            "System Monitoring (Cabin altitude, Differential pressure, Rate of change)",
        ],
    },

    "Powerplant (Turbine Engines)": {
        "01 Turbine Engine Fundamentals": [
            "Basic Principles (Newton’s Laws, Bernoulli’s Principle)",
            "The Brayton Cycle (Constant pressure cycle, pV and T–s diagrams)",
            "Thrust Calculation (Gross thrust, Net thrust, Choked nozzle)",
            "Efficiency Types (Thermal, Propulsive, Overall efficiency)",
        ],

        "02 Engine Inlet and Compressor": [
            "Engine Inlets (Subsonic recovery, Supersonic diffusers, Particle separators)",
            "Centrifugal Compressors (Impeller, Diffuser, Compression ratios)",
            "Axial Compressors (Rotor, Stator, Stages, Pressure rise)",
            "Spool Configurations (Single, Twin, Triple spool)",
            "Compressor Aerodynamics (Stall, Surge, Variable stators, Bleed valves)",
        ],

        "03 Combustion, Turbine and Exhaust": [
            "Combustion Chambers (Can, Annular, Can-annular)",
            "Turbine Section (Impulse, Reaction, Multi-stage design)",
            "Turbine Blade Design (Nozzle guide vanes, Cooling, Creep)",
            "Exhaust Systems (Convergent, Divergent, Mixer nozzles)",
            "Thrust Reversal Systems (Clamshell, Bucket, Cold stream blockage)",
        ],

        "04 Engine Systems and Lubrication": [
            "Fuel Systems (FADEC, Hydromechanical control, Fuel heaters)",
            "Lubrication Systems (Dry sump, Magnetic chip detectors, Scavenge pumps)",
            "Ignition and Starting (High-energy igniters, Air starters, Relight envelope)",
            "Air Systems (Internal cooling, Sealing, External bleed services)",
        ],

        "05 Monitoring and Indications": [
            "Temperature Monitoring (EGT, TGT, ITT limits)",
            "Thrust and Power Indication (N1/N2 RPM, EPR, Torque)",
            "Vibration Monitoring (Airborne Vibration Monitoring)",
            "Engine Health Monitoring (Trend monitoring, Borescope inspections)",
        ],

        "06 Turbine Types and Performance": [
            "Turboprop Engines (Free turbine, Coupled turbine, Reduction gearbox)",
            "Turbofan Engines (Bypass ratio, Fan thrust contribution)",
            "Turbojet Fundamentals",
            "Performance Factors (Altitude, Temperature, Speed effects on thrust)",
        ],
    },

    "AC Electrics": {
        "01 AC Generation Principles": [
            "Fundamentals of AC (Frequency, Phase, Amplitude, RMS values)",
            "Three-Phase Systems (Star and Delta connections)",
            "Alternators (Rotating field, Rotating armature, Brushless design)",
        ],

        "02 AC System Components": [
            "Transformers (Step-up, Step-down, Efficiency, Core losses)",
            "Transformer Rectifier Units (AC to DC conversion)",
            "Inverters (Static and Rotary, DC to AC conversion)",
            "AC Motors (Induction and Synchronous motors)",
        ],

        "03 Constant Speed Drives and IDG": [
            "Need for Constant Frequency (400 Hz standard)",
            "Constant Speed Drive Mechanics",
            "Integrated Drive Generators (IDG)",
            "IDG Disconnect Procedures",
        ],

        "04 AC Distribution and Protection": [
            "AC Bus Architecture (Main and Essential buses)",
            "Parallel Operation (Frequency, Phase, Voltage synchronization)",
            "Split-Bus vs Parallel Systems",
            "Protection Devices (Generator Control Relay, Circuit breakers)",
        ],

        "05 Emergency AC Sources": [
            "Ram Air Turbine (RAT)",
            "APU Generators",
            "Static Inverters",
        ],
    },

    "Instruments and Avionics": {
        "01 Sensors and Pressure Measurement": [
            "Pressure Detection (Static, Total, Dynamic)",
            "Temperature Sensors (RAT and TAT)",
            "Fuel and Engine Sensors (Flow meters, Torque, Vibration monitoring)",
        ],

        "02 Measurement of Air Data Parameters": [
            "Altimetry (Pressure altimetry, VNAV errors, Servo altimeters)",
            "Airspeed Measurement (IAS, CAS, EAS, TAS conversions and errors)",
            "Vertical Speed Measurement (Instantaneous VSI vs Pressure lag)",
            "Mach Measurement (Mach number and compressibility)",
            "Air Data Computer (Inputs, distribution, failure modes)",
        ],

        "03 Magnetism and Compasses": [
            "Direct Reading Magnetic Compass (Dip, Acceleration and turning errors)",
            "Flux Valve Systems",
            "Gyro-Magnetic Compasses (Slaving and synchronization)",
        ],

        "04 Gyroscopic Instruments": [
            "Gyro Principles (Rigidity, Precession, Degrees of freedom)",
            "Directional Gyro (Apparent wander, Transport wander, Earth rate)",
            "Attitude Indicator (Erection systems and display logic)",
            "Turn and Slip / Turn Coordinator",
        ],

        "05 Inertial Navigation and Reference Systems": [
            "Inertial Reference Systems (Alignment and Ring Laser Gyros)",
            "Accelerometers and Integration Principles",
            "Attitude and Heading Reference Systems (AHRS)",
        ],

        "06 Automatic Flight Control Systems": [
            "Autopilot Logic (Inner and Outer loop control)",
            "Flight Director Modes (HDG, NAV, APP, VNAV)",
            "Autothrottle Systems",
        ],

        "07 Electronic Displays and Alerting": [
            "EFIS (PFD and Navigation Display)",
            "ECAM and EICAS",
            "Flight Management System (FMS)",
            "Alerting Systems (GPWS/EGPWS, TCAS II, Overspeed warnings)",
        ],
    },

    "Mass and Balance": {
        "01 Purpose of Mass and Balance": [
            "Mass Limitations (Relationship between mass and structural stress)",
            "Performance Implications (Takeoff, climb, cruise effects)",
            "CG Limitations (Stability and controllability)",
            "CG Effects on Performance (Speeds, fuel consumption, range)",
        ],

        "02 Loading": [
            "Terminology (BEM, DOM, OM, TOM, LM, MZFM, MRM)",
            "Load Terms (Payload, Traffic load, Block fuel, Trip fuel, Reserve fuel)",
            "Mass Limits (Structural vs Performance limits)",
            "Cargo Compartment Limits (Floor load and Running load)",
            "Standard Mass Calculations (Passengers, Crew, Baggage)",
        ],

        "03 Aircraft Mass and Balance Documentation": [
            "Weighing Reports and CG Schedules",
            "Datum and Moment Arms (Reference points and stations)",
            "Index Units and Scaling",
        ],

        "04 Determination of CG Position": [
            "Arithmetic Method (Mass × Arm = Moment)",
            "Graphic Method (Loading diagrams and envelopes)",
            "CG as Percentage of MAC",
            "Load Shifting and Addition Calculations",
        ],

        "05 Cargo Handling": [
            "Cargo Types (General cargo, ULDs, Pallets)",
            "Stowage and Securing (Tie-down points, Load spreaders)",
        ],
    },

    "Aircraft Performance": {
        "01 General Principles of Performance": [
            "Performance Speed Definitions (V1, Vr, V2, Vref, Vne, Vno)",
            "Atmospheric Effects (Pressure altitude, Density altitude, Humidity)",
            "Wind Effects (Headwind and Tailwind components, Factored winds)",
            "Runway Surface Effects (Slope, Standing water, Slush, Grass)",
            "Forces in Performance (Thrust vs Drag, Lift vs Weight in climb)",
        ],

        "02 Single Engine Performance (Class B)": [
            "Takeoff and Landing Performance",
            "Climb Performance (Vy, Vx, Cruise climb)",
            "Cruise Performance (Range vs Endurance, Specific range)",
            "Descent and Glide Performance",
            "Stall Speeds (Vs0, Vs1, Effects of bank angle and mass)",
        ],

        "03 Multi-Engine Performance (Class A)": [
            "Takeoff Speeds (Vef, V1, Vr, V2)",
            "Takeoff Distances (TORA, TODA, ASDA, Balanced field length)",
            "Takeoff Flight Path Segments",
            "Climb Gradients (Gross vs Net requirements)",
            "One Engine Inoperative (OEI) Performance",
        ],

        "04 Use of Performance Graphs and Tables": [
            "Takeoff Performance Charts",
            "Climb and Cruise Charts",
            "Landing Performance Charts",
        ],

        "05 Limitations and Certification": [
            "Structural Mass Limitations (MZFM, MTOM, MLM)",
            "Obstacle Clearance Requirements",
        ],
    },

    "Flight Planning": {
        "01 Flight Planning for VFR Flights": [
            "Route Selection (Airspace, terrain, weather)",
            "Navigation Plan (True/Magnetic tracks, Wind correction, ETE)",
            "Altitudes and Speeds (Semicircular rules, TAS vs GS)",
            "Basic Fuel Plan (Trip fuel and reserves)",
        ],

        "02 Flight Planning for IFR Flights": [
            "IFR Routes (SID, STAR, Airways, ATC restrictions)",
            "Minimum Altitudes (MEA, MOCA, MSA, Grid MORA)",
            "Instrument Approach Planning (Destination and alternate selection)",
            "IFR Navigation Log",
        ],

        "03 Fuel Planning (Commercial Standards)": [
            "Taxi Fuel",
            "Trip Fuel",
            "Contingency Fuel",
            "Alternate Fuel",
            "Final Reserve Fuel",
            "Additional and Extra Fuel",
        ],

        "04 Pre-Flight Preparation": [
            "NOTAM Interpretation",
            "Meteorological Briefing",
            "Point of Equal Time (PET) and Point of Safe Return (PSR)",
            "Alternate Selection",
        ],

        "05 ICAO ATS Flight Plan": [
            "Filing Procedures",
            "Flight Plan Management",
            "Closing the Flight Plan (SAR procedures)",
        ],

        "06 In-Flight Monitoring": [
            "Fuel Monitoring (Planned vs actual)",
            "In-Flight Replanning and Diversions",
        ],
    },    

    "General Navigation": {
        "01 Basics of Navigation": [
            "Solar System and Earth Movements",
            "Earth Geometry (Great Circles, Rhumb Lines)",
            "Position Coordinates (Latitude and Longitude)",
            "Distance Units (Nautical Mile, Statute Mile, Kilometre)",
            "Direction (True, Magnetic, Compass, Variation, Deviation)",
        ],

        "02 Magnetism and Compasses": [
            "Earth’s Magnetism (Dip, Isogonals, Agonic lines)",
            "Aircraft Magnetism (Hard iron, Soft iron, Coefficients)",
            "Compass Errors (Acceleration and Turning)",
        ],

        "03 Charts and Projections": [
            "Chart Properties (Scale, Convergence, Path types)",
            "Lambert Conformal Conic Projection",
            "Mercator Projection",
            "Polar Stereographic Projection and Grid Navigation",
        ],

        "04 Dead Reckoning Navigation": [
            "Triangle of Velocities (Heading, Track, Wind, TAS, GS)",
            "Flight Log Calculations (Time, Speed, Distance, Fuel)",
            "Navigation Computer (CR-3 / CRP-5)",
        ],

        "05 In-Flight Navigation": [
            "Position Fixing Methods",
            "Drift and Groundspeed Checks",
            "Critical Point / Equal Time Point / Point of No Return",
        ],

        "06 Time and Conversions": [
            "Time Systems (LMT, UTC, Standard Time, Date Line)",
            "Sunrise, Sunset and Twilight",
            "Equation of Time",
        ],
    },

    "Radio Navigation": {
        "01 Basic Radio Propagation Theory": [
            "Electromagnetic Waves (Frequency, Wavelength, Phase, Amplitude)",
            "Radio Spectrum (VLF to EHF bands)",
            "Propagation Paths (Ground, Sky, Space waves, Ducting)",
            "Antennas (Polarisation and Directivity)",
            "Modulation Methods (AM, FM, Phase, Pulse)",
        ],

        "02 Non-Directional Beacon (NDB) and ADF": [
            "System Principles",
            "Presentation and Interpretation (Fixed card, RMI)",
            "Errors and Accuracy",
        ],

        "03 VHF Omni-Directional Range (VOR)": [
            "Principle of Operation (Phase comparison)",
            "Types of VOR (CVOR, DVOR, Terminal)",
            "Errors and Range Limitations",
        ],

        "04 Distance Measuring Equipment (DME)": [
            "Principles of Operation",
            "Slant Range Considerations",
            "Frequency Pairing",
        ],

        "05 Instrument Landing System (ILS)": [
            "Localizer",
            "Glide Path",
            "Marker Beacons and DME",
        ],

        "06 Radar Principles and Systems": [
            "Primary Radar",
            "Secondary Surveillance Radar (Modes A, C, S)",
            "Airborne Weather Radar",
        ],

        "07 Satellite and Area Navigation": [
            "GNSS Basics",
            "GPS Principles (Pseudo-ranging and DOP)",
            "Performance-Based Navigation (PBN), RNAV and RNP",
        ],
    },

    "Meteorology": {
        "01 The Atmosphere": [
            "Composition and Structure (Troposphere, Tropopause, Stratosphere)",
            "Standard Atmosphere (ISA and lapse rates)",
            "Pressure and Density (Isobars, QNH, QFE, QNE, Density altitude)",
        ],

        "02 Thermodynamics and Moisture": [
            "Heat Transfer (Radiation, Convection, Advection, Latent heat)",
            "Adiabatic Processes (SALR, DALR, Stability)",
            "Moisture (Humidity, Dew point, Condensation)",
        ],

        "03 Precipitation and Clouds": [
            "Cloud Formation (Convective, Orographic, Frontal)",
            "Cloud Classification",
            "Precipitation Types",
        ],

        "04 Wind and Air Masses": [
            "Wind Forces (Pressure gradient, Coriolis, Friction)",
            "Local Winds",
            "Air Mass Classification",
        ],

        "05 Global Climatology": [
            "General Circulation (Hadley, Ferrel, Polar cells)",
            "Inter-Tropical Convergence Zone (ITCZ)",
            "Jet Streams and Clear Air Turbulence",
        ],

        "06 Meteorological Hazards": [
            "Aircraft Icing",
            "Thunderstorms and Associated Hazards",
            "Visibility Hazards",
        ],

        "07 Meteorological Information and Charts": [
            "Observation Reports (METAR, SPECI, PIREPs)",
            "Forecasts (TAF, SIGMET, AIRMET, GAMET)",
            "Weather Chart Interpretation (SigWX, Wind and Temperature charts)",
        ],
    },

    "Communications": {
        "01 Definitions and General Operating Procedures": [
            "VHF Propagation and Frequency Allocation",
            "Radio Telephony Phraseology (Standard words, Phonetic alphabet)",
            "Transmission Techniques (Speech rate, Read-back requirements)",
            "Call Signs (Aircraft and Ground stations)",
        ],

        "02 VFR Communications Procedures": [
            "Aerodrome Control Procedures",
            "En-Route VFR Communications",
            "Arrival and Landing Procedures",
        ],

        "03 IFR Communications Procedures": [
            "IFR Departure Procedures",
            "En-Route IFR Communications",
            "Approach and Arrival Communications",
        ],

        "04 Distress and Urgency Procedures": [
            "Distress Communications (MAYDAY)",
            "Urgency Communications (PAN-PAN)",
            "Silence and Cancellation Procedures",
        ],

        "05 Communications Failure": [
            "VFR Lost Communications Procedures",
            "IFR Lost Communications Procedures",
        ],

        "06 Meteorological and Aeronautical Information": [
            "Weather Reports (METAR, TAF via radio)",
            "ATIS and VOLMET",
        ],
    },

}



class Command(BaseCommand):
    help = "Seed PPL and CPL syllabus for GRID"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Seeding syllabus..."))

        self.seed_course(
            code="PPL",
            name="Private Pilot Licence",
            syllabus=PPL_SYLLABUS,
        )

        self.seed_course(
            code="CPL",
            name="Commercial Pilot Licence",
            syllabus=CPL_SYLLABUS,
        )

        self.stdout.write(self.style.SUCCESS("Syllabus seeding complete."))

    def seed_course(self, code, name, syllabus):
        course, _ = Course.objects.get_or_create(
            code=code,
            defaults={
                "name": name,
                "authority": "KCAA",
            },
        )

        for subject_order, (subject_name, topics) in enumerate(syllabus.items(), start=1):
            subject, _ = Subject.objects.get_or_create(
                course=course,
                name=subject_name,
                defaults={"order": subject_order},
            )

            for topic_order, (topic_title, subtopics) in enumerate(topics.items(), start=1):
                topic, _ = Topic.objects.get_or_create(
                    subject=subject,
                    title=topic_title,
                    defaults={"order": topic_order},
                )

                for subtopic_order, subtopic_title in enumerate(subtopics, start=1):
                    Subtopic.objects.get_or_create(
                        topic=topic,
                        title=subtopic_title,
                        defaults={"order": subtopic_order},
                    )