import { Link } from "react-router-dom";

export default function FlightDashboard() {
  return (
    <div style={styles.page}>

      <Link to="/" style={styles.backButton} className="back-button">
        ← Back to Main
      </Link>

      <div style={styles.header}>
        <h1 style={styles.title}>Flight Planning</h1>

        <p style={styles.subtitle}>
          Plan routes, explore aerodromes and monitor flights.
        </p>
      </div>

      <div style={styles.grid}>

        {/* Planner */}

        <Link
          to="/flight/planner"
          style={styles.card}
          className="flight-card"
        >

          <div style={styles.cardTitle}>
            Flight Planner
          </div>

          <p style={styles.cardText}>
            Build routes between aerodromes, add waypoints and visualize
            navigation paths on the aviation map.
          </p>

          <div style={styles.cardButton}>
            Open Planner →
          </div>

        </Link>

        {/* Aerodrome Info */}

        <Link
          to="/flight/aerodromes"
          style={styles.card}
          className="flight-card"
        >

          <div style={styles.cardTitle}>
            Aerodrome Information
          </div>

          <p style={styles.cardText}>
            Search aerodromes, view runway information, frequencies and
            operational details.
          </p>

          <div style={styles.cardButton}>
            Browse Aerodromes →
          </div>

        </Link>

        {/* Saved Routes */}

        <Link
          to="/flight/routes"
          style={styles.card}
          className="flight-card"
        >

          <div style={styles.cardTitle}>
            Saved Routes
          </div>

          <p style={styles.cardText}>
            Access previously planned routes and review navigation
            details for upcoming flights.
          </p>

          <div style={styles.cardButton}>
            View Routes →
          </div>

        </Link>

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    padding: "80px 60px",
    fontFamily: "system-ui",
    background: "#0F172A"
  },

  header: {
    marginBottom: "50px"
  },

  title: {
    fontSize: "44px",
    color: "#F1F5F9",
    marginBottom: "10px"
  },

  subtitle: {
    color: "#94A3B8"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "30px",
    maxWidth: "1100px"
  },

  card: {
    padding: "30px",
    borderRadius: "16px",
    textDecoration: "none",
    background: "rgba(30,41,59,0.85)",
    backdropFilter: "blur(10px)",
    color: "#F1F5F9",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.5)",
    transition: "all 0.3s ease",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    height: "200px"
  },

  cardTitle: {
    fontSize: "22px",
    fontWeight: "600"
  },

  cardText: {
    fontSize: "14px",
    color: "#CBD5F5",
    lineHeight: "1.5"
  },

  // replaced peach with neutral action button
  cardButton: {
    marginTop: "10px",
    padding: "8px 14px",
    borderRadius: "8px",
    background: "#334155",
    border: "1px solid #475569",
    color: "#F1F5F9",
    width: "fit-content",
    fontWeight: "600",
    transition: "all 0.25s ease"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "40px",
    padding: "10px 20px",
    background: "rgba(30,41,59,0.85)",
    color: "#F1F5F9",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    border: "1px solid #334155",
    boxShadow: "0 6px 18px rgba(0,0,0,0.4)",
    transition: "all 0.25s ease",
    cursor: "pointer"
  }

};