import { Link, useParams } from "react-router-dom";

export default function PPLSubjectDetail() {

  const { id } = useParams();

  const topics = [
    "Introduction",
    "Fundamentals",
    "Operational Concepts",
    "Examples & Applications",
    "Practice Questions"
  ];

  return (
      <div style={styles.page}>

        <Link to="/learning/ppl/subjects" style={styles.backButton} className="back-button">
          ← Back to Subjects
        </Link>

        <div style={styles.header}>
          <h1 style={styles.title}>{id} — PPL Subject</h1>
        </div>

        <div style={styles.grid}>

    {/* MOCK EXAMS */}
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>Mock Exams</h2>
      <p style={styles.cardText}>
        Simulate real aviation exam conditions with timed tests
        and full subject coverage.
      </p>

      <button style={styles.primaryButton}>
        Start Exam
      </button>
    </div>

    {/* QUESTION BANK */}
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>Question Bank</h2>
      <p style={styles.cardText}>
        Practice questions by topic and improve your understanding
        with instant feedback.
      </p>

      <button style={styles.primaryButton}>
        Practice Questions
      </button>
    </div>

    {/* NOTES */}
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>Notes</h2>
      <p style={styles.cardText}>
        Access structured notes and reference material for
        quick revision.
      </p>

      <button style={styles.secondaryButton}>
        View Notes
      </button>
    </div>

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
    fontSize: "36px",
    color: "#F1F5F9",
    marginBottom: "40px"
  },

  // 3-tile layout
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "30px",
    maxWidth: "1000px"
  },

  // main tiles
  card: {
    padding: "30px",
    borderRadius: "16px",
    background: "rgba(30,41,59,0.9)",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    gap: "16px",
    transition: "all 0.3s ease"
  },

  cardTitle: {
    fontSize: "22px",
    color: "#F1F5F9"
  },

  cardText: {
    fontSize: "14px",
    color: "#CBD5F5",
    lineHeight: "1.5"
  },

  primaryButton: {
    marginTop: "10px",
    padding: "10px 16px",
    borderRadius: "8px",
    border: "1px solid #475569",
    background: "#334155",
    color: "#F1F5F9",
    fontWeight: "600",
    cursor: "pointer"
  },

  secondaryButton: {
    marginTop: "10px",
    padding: "10px 16px",
    borderRadius: "8px",
    border: "1px solid #475569",
    background: "#1E293B",
    color: "#F1F5F9",
    fontWeight: "600",
    cursor: "pointer"
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