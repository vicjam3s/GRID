import { useState } from "react";
import MapView from "../../components/flight/MapView";

export default function FlightPlanner() {

  const [departure, setDeparture] = useState("");
  const [destination, setDestination] = useState("");

  return (
    <div style={styles.page}>

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
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)",
    padding: "40px"
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "320px 1fr",
    gap: "25px"
  },

  sidebar: {
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    padding: "25px",
    borderRadius: "14px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    display: "flex",
    flexDirection: "column",
    gap: "15px"
  },

  title: {
    marginBottom: "10px"
  },

  field: {
    display: "flex",
    flexDirection: "column",
    gap: "6px"
  },

  input: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ddd"
  },

  primaryButton: {
    marginTop: "10px",
    padding: "12px",
    borderRadius: "10px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    fontWeight: "600",
    cursor: "pointer"
  },

  secondaryButton: {
    padding: "12px",
    borderRadius: "10px",
    border: "none",
    background: "#2E2E2E",
    color: "white",
    fontWeight: "600",
    cursor: "pointer"
  },

  mapArea: {
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    borderRadius: "14px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },

  mapPlaceholder: {
    fontSize: "22px",
    color: "#666"
  }

};