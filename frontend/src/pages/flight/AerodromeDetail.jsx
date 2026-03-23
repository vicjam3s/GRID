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
    background: "#0F172A"
  },

  header: {
    marginBottom: "40px"
  },

  title: {
    fontSize: "40px",
    color: "#F1F5F9"
  },

  subtitle: {
    color: "#94A3B8"
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
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "320px 1fr",
    gap: "30px"
  },

  // left panel (aerodrome data)
  sidebar: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)"
  },

  // right panel (operational info)
  content: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)"
  },

  sectionTitle: {
    marginBottom: "20px",
    fontSize: "20px",
    color: "#F1F5F9"
  },

  // structured info rows (like checklist data)
  infoItem: {
    display: "flex",
    justifyContent: "space-between",
    marginBottom: "12px",
    paddingBottom: "6px",
    borderBottom: "1px solid #1E293B",
    color: "#CBD5F5",
    fontSize: "14px"
  },

  // frequency cards look like selectable data blocks
  frequencyCard: {
    display: "flex",
    justifyContent: "space-between",
    padding: "12px",
    borderRadius: "8px",
    background: "#020617",
    border: "1px solid #334155",
    marginBottom: "10px",
    color: "#F1F5F9",
    transition: "all 0.25s ease"
  }

};