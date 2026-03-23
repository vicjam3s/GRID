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

      <div style={styles.layout}>

        {/* Sidebar */}

        <div style={styles.sidebar}>

          <h3 style={styles.sidebarTitle}>Topics</h3>

          {topics.map((topic, index) => (
            <div key={index} style={styles.topicItem}>
              {topic}
            </div>
          ))}

        </div>

        {/* Content Area */}

        <div style={styles.content}>

          <h2 style={styles.contentTitle}>
            Select a topic to begin studying
          </h2>

          <p style={styles.contentText}>
            Study notes, explanations and practice questions for this
            subject will appear here.
          </p>

          <div style={styles.actions}>

            <button style={styles.primaryButton}>
              Practice Questions
            </button>

            <button style={styles.secondaryButton}>
              Mock Exam
            </button>

            <button style={styles.tertiaryButton}>
              Review Incorrect Questions
            </button>

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
    fontSize: "36px",
    color: "#F1F5F9"
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "260px 1fr",
    gap: "30px"
  },

  // topics sidebar (like syllabus panel)
  sidebar: {
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    borderRadius: "14px",
    padding: "20px",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)"
  },

  sidebarTitle: {
    marginBottom: "20px",
    fontSize: "18px",
    color: "#F1F5F9"
  },

  // topic items (interactive list)
  topicItem: {
    padding: "10px",
    borderRadius: "8px",
    marginBottom: "8px",
    cursor: "pointer",
    background: "#020617",
    border: "1px solid #1E293B",
    color: "#CBD5F5",
    transition: "all 0.25s ease"
  },

  // main content panel
  content: {
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    borderRadius: "14px",
    padding: "30px",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)"
  },

  contentTitle: {
    fontSize: "24px",
    marginBottom: "12px",
    color: "#F1F5F9"
  },

  contentText: {
    color: "#CBD5F5",
    marginBottom: "30px"
  },

  actions: {
    display: "flex",
    gap: "15px"
  },

  // unified action buttons
  notesButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#334155",
    color: "#F1F5F9",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  quizButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#1E293B",
    color: "#F1F5F9",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  examButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#020617",
    color: "#F1F5F9",
    cursor: "pointer",
    transition: "all 0.25s ease"
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