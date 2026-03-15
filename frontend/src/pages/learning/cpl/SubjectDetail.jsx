import { useParams } from "react-router-dom";

export default function CPLSubjectDetail() {

  const { id } = useParams();

  const topics = [
    "Introduction",
    "Theory & Concepts",
    "Operational Applications",
    "Performance Considerations",
    "Examples & Calculations",
    "Practice Questions"
  ];

  return (
    <div style={styles.page}>

      <div style={styles.header}>
        <h1 style={styles.title}>{id} — CPL Subject</h1>
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

        {/* Content */}

        <div style={styles.content}>

          <h2 style={styles.contentTitle}>
            Select a topic to begin studying
          </h2>

          <p style={styles.contentText}>
            Detailed CPL study material, explanations and exam preparation
            content will appear here once connected to the backend.
          </p>

          <div style={styles.actions}>

            <button style={styles.notesButton}>
              View Notes
            </button>

            <button style={styles.quizButton}>
              Practice Questions
            </button>

            <button style={styles.examButton}>
              Mock Exam
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
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  header: {
    marginBottom: "40px"
  },

  title: {
    fontSize: "36px",
    color: "#2E2E2E"
  },

  layout: {
    display: "grid",
    gridTemplateColumns: "260px 1fr",
    gap: "30px"
  },

  sidebar: {
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    borderRadius: "14px",
    padding: "20px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)"
  },

  sidebarTitle: {
    marginBottom: "20px",
    fontSize: "18px"
  },

  topicItem: {
    padding: "10px",
    borderRadius: "8px",
    marginBottom: "8px",
    cursor: "pointer",
    background: "rgba(255,255,255,0.5)",
    transition: "all 0.25s ease"
  },

  content: {
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    borderRadius: "14px",
    padding: "30px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)"
  },

  contentTitle: {
    fontSize: "24px",
    marginBottom: "12px"
  },

  contentText: {
    color: "#555",
    marginBottom: "30px"
  },

  actions: {
    display: "flex",
    gap: "15px"
  },

  notesButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    cursor: "pointer"
  },

  quizButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "none",
    background: "#2E2E2E",
    color: "white",
    cursor: "pointer"
  },

  examButton: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "none",
    background: "#555",
    color: "white",
    cursor: "pointer"
  }

};