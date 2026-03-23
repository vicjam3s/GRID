import { useState } from "react";
import { Link } from "react-router-dom";
import MapView from "../../components/flight/MapView";

export default function FlightPlanner() {

  const [departure, setDeparture] = useState("");
  const [destination, setDestination] = useState("");

  return (
    <div style={styles.page}>

      <Link to="/flight" style={styles.backButton} className="back-button">
        ← Back to Flight Planning
      </Link>

      <div style={styles.layout}>

        {/* LEFT PANEL */}

        <div style={styles.sidebar}>

          <h2 style={styles.title}>Flight Planner</h2>

          <div style={styles.field}>
            <label>Departure</label>
            <input
              type="text"
              placeholder="e.g HKJK"
              value={departure}
              onChange={(e) => setDeparture(e.target.value)}
              style={styles.input}
            />
          </div>

          <div style={styles.field}>
            <label>Destination</label>
            <input
              type="text"
              placeholder="e.g HKMO"
              value={destination}
              onChange={(e) => setDestination(e.target.value)}
              style={styles.input}
            />
          </div>

          <button style={styles.primaryButton}>
            Build Route
          </button>

          <button style={styles.secondaryButton}>
            Save Route
          </button>

        </div>

        {/* MAP AREA */}

        <div style={styles.mapArea}>
          <MapView departure={departure} destination={destination} />
        </div>

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    fontFamily: "system-ui",
    background: "#0F172A",
    padding: "40px"
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "320px 1fr",
    gap: "25px"
  },

  // cockpit-style control panel
  sidebar: {
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    padding: "25px",
    borderRadius: "14px",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    display: "flex",
    flexDirection: "column",
    gap: "15px"
  },

  title: {
    marginBottom: "10px",
    color: "#F1F5F9",
    fontSize: "20px",
    fontWeight: "600"
  },

  field: {
    display: "flex",
    flexDirection: "column",
    gap: "6px",
    color: "#94A3B8",
    fontSize: "13px"
  },

  // dark input like avionics fields
  input: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #334155",
    background: "#020617",
    color: "#F1F5F9",
    outline: "none"
  },

  primaryButton: {
    marginTop: "10px",
    padding: "12px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#334155",
    color: "#F1F5F9",
    fontWeight: "600",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  secondaryButton: {
    padding: "12px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#1E293B",
    color: "#F1F5F9",
    fontWeight: "600",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  // map becomes main display
  mapArea: {
    background: "#020617",
    borderRadius: "14px",
    border: "1px solid #334155",
    boxShadow: "0 12px 45px rgba(0,0,0,0.7)",
    overflow: "hidden", // important for leaflet
    display: "flex"
  },

  mapPlaceholder: {
    fontSize: "22px",
    color: "#64748B"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "40px",
    padding: "10px 20px",
    background: "rgba(30,41,59,0.9)",
    color: "#F1F5F9",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    border: "1px solid #334155",
    boxShadow: "0 6px 20px rgba(0,0,0,0.5)",
    transition: "all 0.25s ease",
    cursor: "pointer"
  }

};