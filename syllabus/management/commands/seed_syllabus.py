from django.core.management.base import BaseCommand
from syllabus.models import Course, Subject, Topic, Subtopic


PPL_SYLLABUS = {
    "Air Law": {
        "International Agreements & Organizations": [
            "Chicago Convention",
            "ICAO Structure",
            "National Aviation Law (Kenya)",
        ],
        "Personnel Licensing (ICAO Annex 1)": [
            "PPL Privileges & Limitations",
            "Medical Certification",
        ],
        "Rules of the Air (ICAO Annex 2)": [
            "General Rules",
            "Avoidance of Collisions",
            "VFR Weather Minima",
        ],
        "Air Traffic Services (ICAO Annex 11)": [
            "Airspace Classification",
            "ATS Services",
        ],
        "Aerodromes (ICAO Annex 14)": [
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

    
}


CPL_SYLLABUS = {
   
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