import { Link } from "react-router-dom";
import BackgroundLines from "../../components/BackgroundLines";

export default function LearningDashboard() {
  return (
    <div style={styles.page}>
      <BackgroundLines />

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
    background: "#0F172A",
    position: "relative"
  },

  container: {
    width: "100%",
    maxWidth: "1000px",
    padding: "40px",
    position: "relative",
    zIndex: 2
  },

  header: {
    textAlign: "center",
    marginBottom: "60px"
  },

  title: {
    fontSize: "50px",
    color: "#F1F5F9",
    marginBottom: "10px"
  },

  subtitle: {
    color: "#94A3B8",
    fontSize: "18px"
  },

  programGrid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "40px"
  },

  // training program cards
  programCard: {
    padding: "40px",
    borderRadius: "18px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(12px)",
    textDecoration: "none",
    color: "#F1F5F9",
    border: "1px solid #334155",
    boxShadow: "0 14px 40px rgba(0,0,0,0.6)",
    transition: "all 0.3s ease",
    display: "flex",
    flexDirection: "column",
    gap: "16px"
  },

  // badges
  badge: {
    background: "#334155",
    color: "#F1F5F9",
    fontWeight: "700",
    width: "fit-content",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px",
    border: "1px solid #475569"
  },

  badgeDark: {
    background: "#020617",
    color: "#F1F5F9",
    fontWeight: "700",
    width: "fit-content",
    padding: "6px 12px",
    borderRadius: "6px",
    fontSize: "12px",
    border: "1px solid #334155"
  },

  programTitle: {
    fontSize: "26px"
  },

  programText: {
    fontSize: "15px",
    color: "#CBD5F5",
    lineHeight: "1.6"
  },

  // action button (neutral system)
  cardAction: {
    marginTop: "12px",
    padding: "10px 18px",
    borderRadius: "8px",
    background: "#334155",
    border: "1px solid #475569",
    color: "#F1F5F9",
    fontWeight: "600",
    width: "fit-content",
    transition: "all 0.25s ease"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "30px",
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

};