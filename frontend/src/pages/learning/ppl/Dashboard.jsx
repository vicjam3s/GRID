import { Link } from "react-router-dom";
import BackgroundLines from "../../../components/BackgroundLines";

const subjects = [

  { code: "AL", name: "Air Law" },
  { code: "MET", name: "Meteorology" },
  { code: "NAV", name: "Navigation" },

  { code: "HP", name: "Human Performance" },
  { code: "MB", name: "Mass & Balance" },
  { code: "OPS", name: "Operational Procedures" },

  { code: "POF", name: "Principles of Flight" },
  { code: "AGK", name: "Aircraft General Knowledge" },
  { code: "COM", name: "Communications" }

];

export default function PPLDashboard() {
  return (
    <div style={styles.page}>
      <BackgroundLines />

      <Link to="/learning" style={styles.backButton} className="back-button">
        ← Back to E-Learning
      </Link>

      <div style={styles.header}>

        <h1 style={styles.title}>
          Private Pilot Licence
        </h1>

        <p style={styles.subtitle}>
          Study subjects required for the Private Pilot Licence.
        </p>

      </div>

      <div style={styles.subjectGrid}>

        {subjects.map((subject) => (

          <Link
            key={subject.code}
            to={`/learning/ppl/subjects/${subject.code}`}
            style={styles.subjectCard}
            className="subject-card"
          >

            <div style={styles.subjectCode}>
              {subject.code}
            </div>

            <div style={styles.subjectName}>
              {subject.name}
            </div>

          </Link>

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

  subjectGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "24px",
    maxWidth: "1000px"
  },

  // subject cards = training modules
  subjectCard: {
    padding: "26px",
    borderRadius: "16px",
    textDecoration: "none",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    color: "#F1F5F9",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    transition: "all 0.3s ease",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    height: "120px"
  },

  // ICAO-like subject codes (clean, neutral)
  subjectCode: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#94A3B8",
    letterSpacing: "1px"
  },

  subjectName: {
    fontSize: "18px",
    fontWeight: "500"
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