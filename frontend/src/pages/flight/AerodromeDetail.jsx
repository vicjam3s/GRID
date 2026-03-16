import { Link, useParams } from "react-router-dom";

export default function AerodromeDetail() {

  const { icao } = useParams();

  return (
    <div style={styles.page}>

      <Link to="/flight/aerodromes" style={styles.backButton} className="back-button">
        ← Back to Aerodromes
      </Link>

      <div style={styles.header}>
        <h1 style={styles.title}>{icao}</h1>
        <p style={styles.subtitle}>Aerodrome Information</p>
      </div>

      <div style={styles.layout}>

        {/* LEFT PANEL */}

        <div style={styles.sidebar}>

          <h3 style={styles.sectionTitle}>Aerodrome Details</h3>

          <div style={styles.infoItem}>
            <span>ICAO</span>
            <strong>{icao}</strong>
          </div>

          <div style={styles.infoItem}>
            <span>Elevation</span>
            <strong>—</strong>
          </div>

          <div style={styles.infoItem}>
            <span>Coordinates</span>
            <strong>—</strong>
          </div>

          <div style={styles.infoItem}>
            <span>Runways</span>
            <strong>—</strong>
          </div>

        </div>


        {/* RIGHT PANEL */}

        <div style={styles.content}>

          <h2 style={styles.sectionTitle}>
            Frequencies
          </h2>

          <div style={styles.frequencyCard}>
            <div>Tower</div>
            <div>—</div>
          </div>

          <div style={styles.frequencyCard}>
            <div>Ground</div>
            <div>—</div>
          </div>

          <div style={styles.frequencyCard}>
            <div>ATIS</div>
            <div>—</div>
          </div>

        </div>

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    padding: "60px",
    fontFamily: "system-ui",
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  header: {
    marginBottom: "40px"
  },

  title: {
    fontSize: "40px",
    color: "#2E2E2E"
  },

  subtitle: {
    color: "#555"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "40px",
    padding: "10px 20px",
    background: "rgba(255, 255, 255, 0.8)",
    color: "#2E2E2E",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    transition: "all 0.3s ease",
    cursor: "pointer"
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "320px 1fr",
    gap: "30px"
  },

  sidebar: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)"
  },

  content: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)"
  },

  sectionTitle: {
    marginBottom: "20px",
    fontSize: "20px"
  },

  infoItem: {
    display: "flex",
    justifyContent: "space-between",
    marginBottom: "10px"
  },

  frequencyCard: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px",
    borderRadius: "8px",
    background: "rgba(255,255,255,0.5)",
    marginBottom: "8px"
  }

};