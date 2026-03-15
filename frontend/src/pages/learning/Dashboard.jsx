import { Link } from "react-router-dom";

export default function LearningDashboard() {
  return (
    <div style={styles.page}>

      <div style={styles.container}>

        <Link to="/" style={styles.backButton} className="back-button">
          ← Back to Main
        </Link>

        <div style={styles.header}>
          <h1 style={styles.title}>E-Learning</h1>

          <p style={styles.subtitle}>
            Choose the aviation training programme you are preparing for.
          </p>
        </div>

        <div style={styles.programGrid}>

          <Link
            to="/learning/ppl"
            style={styles.programCard}
            className="program-card"
          >
            <div style={styles.badge}>PPL</div>

            <h2 style={styles.programTitle}>
              Private Pilot Licence
            </h2>

            <p style={styles.programText}>
              Core aviation theory covering navigation, meteorology,
              air law, aircraft systems and operational procedures.
            </p>

            {/* Display subjects button */}
            <div style={styles.cardAction} className="program-button">
                Open Programme →
            </div>

          </Link>


          <Link
            to="/learning/cpl"
            style={styles.programCard}
            className="program-card"
          >

            <div style={styles.badgeDark}>CPL</div>

            <h2 style={styles.programTitle}>
              Commercial Pilot Licence
            </h2>

            <p style={styles.programText}>
              Advanced aviation theory including flight planning,
              aircraft performance, navigation systems and professional
              flight operations.
            </p>

            {/* Display subjects button */}
            <div style={styles.cardAction} className="program-button">
                Open Programme →
            </div>

          </Link>

        </div>

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontFamily: "system-ui",
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  container: {
    width: "100%",
    maxWidth: "1000px",
    padding: "40px"
  },

  header: {
    textAlign: "center",
    marginBottom: "60px"
  },

  title: {
    fontSize: "50px",
    color: "#2E2E2E",
    marginBottom: "10px"
  },

  subtitle: {
    color: "#555",
    fontSize: "18px"
  },

  programGrid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "40px"
  },

  programCard: {
    padding: "40px",
    borderRadius: "18px",
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(12px)",
    textDecoration: "none",
    color: "#2E2E2E",
    boxShadow: "0 14px 35px rgba(0,0,0,0.1)",
    transition: "all 0.35s ease",
    display: "flex",
    flexDirection: "column",
    gap: "16px"
  },

  badge: {
    background: "#FF9E8A",
    color: "white",
    fontWeight: "700",
    width: "fit-content",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px"
  },

  badgeDark: {
    background: "#2E2E2E",
    color: "white",
    fontWeight: "700",
    width: "fit-content",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px"
  },

  programTitle: {
    fontSize: "26px"
  },

  programText: {
    fontSize: "15px",
    color: "#555",
    lineHeight: "1.6"
  },

  cardAction: {
    marginTop: "12px",
    padding: "10px 18px",
    borderRadius: "8px",
    background: "#FF9E8A",
    color: "white",
    fontWeight: "600",
    width: "fit-content",
    transition: "all 0.25s ease"  },

  backButton: {
    display: "inline-block",
    marginBottom: "30px",
    padding: "10px 20px",
    background: "rgba(255, 255, 255, 0.8)",
    color: "#2E2E2E",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    transition: "all 0.3s ease",
    cursor: "pointer"  },

};