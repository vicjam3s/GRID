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
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  header: {
    marginBottom: "40px"
  },

  title: {
    fontSize: "42px",
    marginBottom: "10px",
    color: "#2E2E2E"
  },

  subtitle: {
    color: "#555"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "25px",
    maxWidth: "1100px"
  },

  card: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.65)",
    backdropFilter: "blur(10px)",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    display: "flex",
    flexDirection: "column",
    gap: "12px"
  },

  routeTitle: {
    fontSize: "20px",
    fontWeight: "600"
  },

  routeInfo: {
    fontSize: "14px",
    color: "#555"
  },

  actions: {
    display: "flex",
    gap: "10px",
    marginTop: "10px"
  },

  primaryButton: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    cursor: "pointer"
  },

  secondaryButton: {
    padding: "8px 14px",
    borderRadius: "8px",
    border: "none",
    background: "#2E2E2E",
    color: "white",
    cursor: "pointer"
  }

};