import { Link } from "react-router-dom";

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
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  title: {
    fontSize: "42px",
    marginBottom: "40px",
    color: "#2E2E2E"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "24px",
    maxWidth: "900px"
  },

  card: {
    padding: "24px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.65)",
    backdropFilter: "blur(10px)",
    textDecoration: "none",
    color: "#2E2E2E",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    transition: "all 0.35s ease"
  },

  code: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#FF9E8A",
    marginBottom: "8px"
  },

  name: {
    fontSize: "18px"
  },

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
    cursor: "pointer"
  }

};