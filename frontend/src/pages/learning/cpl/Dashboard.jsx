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

export default function CPLDashboard() {
  return (
    <div style={styles.page}>

      <Link to="/learning" style={styles.backButton} className="back-button">
        ← Back to E-Learning
      </Link>

      <div style={styles.header}>

        <h1 style={styles.title}>
          Commercial Pilot Licence
        </h1>

        <p style={styles.subtitle}>
          Advanced aviation theory subjects required for CPL training.
        </p>

      </div>

      <div style={styles.subjectGrid}>

        {subjects.map((subject) => (

          <Link
            key={subject.code}
            to={`/learning/cpl/subjects/${subject.code}`}
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
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  header: {
    marginBottom: "50px"
  },

  title: {
    fontSize: "44px",
    color: "#2E2E2E",
    marginBottom: "10px"
  },

  subtitle: {
    color: "#555"
  },

  subjectGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "24px",
    maxWidth: "1000px"
  },

  subjectCard: {
    padding: "26px",
    borderRadius: "16px",
    textDecoration: "none",
    background: "rgba(255,255,255,0.65)",
    backdropFilter: "blur(10px)",
    color: "#2E2E2E",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    transition: "all 0.35s ease",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    height: "120px"
  },

  subjectCode: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#FF9E8A",
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