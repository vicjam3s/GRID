import { Link } from "react-router-dom";
import BackgroundLines from "../../../components/BackgroundLines";

const subjects = [
  { code: "AL", name: "Air Law" },
  { code: "MET", name: "Meteorology" },
  { code: "NAV", name: "General Navigation" },
  { code: "RNAV", name: "Radio Navigation" },
  { code: "FP", name: "Flight Planning" },
  { code: "ACP", name: "Aircraft Performance" },
  { code: "HP", name: "Human Performance" },
  { code: "OPS", name: "Operational Procedures" },
  { code: "INS", name: "Instruments" },
  { code: "AGK", name: "Aircraft General Knowledge" },
  { code: "POF", name: "Principles of Flight" },
  { code: "COMM", name: "Communications" }
];

export default function CPLSubjects() {
  return (
    <div style={styles.page}>
      <BackgroundLines />

      <Link to="/learning/cpl" style={styles.backButton} className="back-button">
        ← Back to Dashboard
      </Link>

      <h1 style={styles.title}>CPL Subjects</h1>

      <div style={styles.grid}>

        {subjects.map((subject) => (
          <Link
            key={subject.code}
            to={`/learning/cpl/subjects/${subject.code}`}
            style={styles.card}
            className="subject-card"
          >
            <div style={styles.code}>{subject.code}</div>
            <div style={styles.name}>{subject.name}</div>
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

  title: {
    fontSize: "42px",
    marginBottom: "40px",
    color: "#F1F5F9"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "24px",
    maxWidth: "900px"
  },

  // subject cards
  card: {
    padding: "24px",
    borderRadius: "14px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    textDecoration: "none",
    color: "#F1F5F9",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    transition: "all 0.3s ease"
  },

  // subject codes (ICAO-style look)
  code: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#94A3B8",
    marginBottom: "8px",
    letterSpacing: "1px"
  },

  name: {
    fontSize: "18px",
    fontWeight: "500"
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
  }

};