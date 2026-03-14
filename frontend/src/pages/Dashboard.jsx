import { Link } from "react-router-dom";
import { useState } from "react";

export default function Dashboard() {

  const [hovered, setHovered] = useState(null);

  return (
    <div style={styles.page}>

      <div style={styles.header}>
        <h1 style={styles.title}>GRID</h1>
        <p style={styles.subtitle}>
          Aviation Learning & Flight Planning Platform
        </p>
      </div>

      <div style={styles.splitContainer}>

        <div
          style={{
            ...styles.panel,
            ...styles.learning,
            flex: hovered === "learning" ? 1.2 : 1
          }}
          onMouseEnter={() => setHovered("learning")}
          onMouseLeave={() => setHovered(null)}
        >

          <div style={styles.glassCard}>

            <h2 style={styles.panelTitle}>E-Learning</h2>

            <p style={styles.panelText}>
              Study aviation theory through structured modules covering
              navigation, meteorology, air law, performance and aircraft
              systems. Practice exam questions, review notes and monitor
              learning progress as you prepare for aviation examinations.
            </p>

            <Link to="/learning">
              <button style={styles.button}>
                Enter Learning
              </button>
            </Link>

          </div>

        </div>

        <div
          style={{
            ...styles.panel,
            ...styles.flight,
            flex: hovered === "flight" ? 1.2 : 1
          }}
          onMouseEnter={() => setHovered("flight")}
          onMouseLeave={() => setHovered(null)}
        >

          <div style={styles.glassCard}>

            <h2 style={styles.panelTitle}>Flight Planning</h2>

            <p style={styles.panelText}>
              Plan and manage flights using an interactive aviation map.
              View aerodrome information, build routes, monitor flights
              in real time and organise saved navigation plans for
              training or operational use.
            </p>

            <Link to="/flight">
              <button style={styles.buttonDark}>
                Open Planner
              </button>
            </Link>

          </div>

        </div>

      </div>

    </div>
  );
}

const styles = {

  page: {
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    fontFamily: "system-ui",
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  header: {
    textAlign: "center",
    paddingTop: "60px",
    paddingBottom: "40px"
  },

  title: {
    fontSize: "80px",
    fontWeight: "700",
    color: "#2E2E2E",
    marginBottom: "10px",
    letterSpacing: "3px"
  },

  subtitle: {
    color: "#555",
    fontSize: "18px"
  },

  splitContainer: {
    flex: 1,
    display: "flex",
    transition: "all 0.4s ease"
  },

  panel: {
    flex: 1,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "40px",
    transition: "all 0.4s ease"
  },

  learning: {
    background:
      "linear-gradient(135deg,#FF9E8A 0%, #FFB7A5 100%)"
  },

  flight: {
    background:
      "linear-gradient(135deg,#2E2E2E 0%, #3A3A3A 100%)"
  },

  glassCard: {
    maxWidth: "420px",
    padding: "35px",
    borderRadius: "16px",
    background: "rgba(255,255,255,0.25)",
    backdropFilter: "blur(12px)",
    WebkitBackdropFilter: "blur(12px)",
    boxShadow: "0 8px 30px rgba(0,0,0,0.15)",
    color: "white"
  },

  panelTitle: {
    fontSize: "36px",
    marginBottom: "20px"
  },

  panelText: {
    fontSize: "16px",
    lineHeight: "1.6",
    marginBottom: "25px"
  },

  button: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "white",
    color: "#FF8A73",
    fontWeight: "600",
    cursor: "pointer"
  },

  buttonDark: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    fontWeight: "600",
    cursor: "pointer"
  }

};