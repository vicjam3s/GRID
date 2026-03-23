import { Link } from "react-router-dom";

const routes = [

  {
    id: 1,
    departure: "HKJK",
    destination: "HKNY",
    distance: "84 NM"
  },

  {
    id: 2,
    departure: "HKJK",
    destination: "HKMO",
    distance: "232 NM"
  },

  {
    id: 3,
    departure: "HKEL",
    destination: "HKLO",
    distance: "175 NM"
  }

];

export default function Routes() {

  return (
    <div style={styles.page}>

      <Link to="/flight" style={styles.backButton} className="back-button">
        ← Back to Flight Planning
      </Link>

      <div style={styles.header}>

        <h1 style={styles.title}>
          Saved Routes
        </h1>

        <p style={styles.subtitle}>
          Previously planned navigation routes.
        </p>

      </div>


      <div style={styles.grid}>

        {routes.map((route) => (

          <div
            key={route.id}
            style={styles.card}
            className="route-card"
          >

            <div style={styles.routeTitle}>
              {route.departure} → {route.destination}
            </div>

            <div style={styles.routeInfo}>
              Distance: {route.distance}
            </div>

            <div style={styles.actions}>

              <button style={styles.primaryButton}>
                Load Route
              </button>

              <button style={styles.secondaryButton}>
                Delete
              </button>

            </div>

          </div>

        ))}

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
    marginBottom: "40px"
  },

  title: {
    fontSize: "42px",
    marginBottom: "10px",
    color: "#F1F5F9"
  },

  subtitle: {
    color: "#94A3B8"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "25px",
    maxWidth: "1100px"
  },

  // route cards = mission blocks
  card: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    display: "flex",
    flexDirection: "column",
    gap: "12px",
    transition: "all 0.3s ease"
  },

  routeTitle: {
    fontSize: "20px",
    fontWeight: "600",
    color: "#F1F5F9"
  },

  routeInfo: {
    fontSize: "14px",
    color: "#CBD5F5"
  },

  actions: {
    display: "flex",
    gap: "10px",
    marginTop: "10px"
  },

  // consistent neutral buttons
  primaryButton: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "1px solid #475569",
    background: "#334155",
    color: "#F1F5F9",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  secondaryButton: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "1px solid #475569",
    background: "#1E293B",
    color: "#F1F5F9",
    cursor: "pointer",
    transition: "all 0.25s ease"
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