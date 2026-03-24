import BackgroundLines from "../../../components/BackgroundLines";

export default function Quiz() {
  return (
    <div style={styles.page}>
      <BackgroundLines />
      <div style={styles.content}>
        <h1>Practice Quiz</h1>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    padding: "60px",
    fontFamily: "system-ui",
    background: "#0F172A",
    position: "relative"
  },
  content: {
    position: "relative",
    zIndex: 2
  }
};