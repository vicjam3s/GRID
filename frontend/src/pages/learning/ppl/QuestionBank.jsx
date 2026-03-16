export default function QuestionBank() {

  const question = {
    text: "What is the standard atmospheric pressure at sea level?",
    options: [
      "1013 hPa",
      "1000 hPa",
      "980 hPa",
      "1030 hPa"
    ]
  };

  return (

    <div style={styles.page}>

      <h1 style={styles.title}>Practice Questions</h1>

      <div style={styles.card}>

        <p style={styles.question}>
          {question.text}
        </p>

        {question.options.map((option, index) => (

          <button key={index} style={styles.option}>
            {option}
          </button>

        ))}

      </div>

    </div>

  );
}

const styles = {

  page: {
    padding: "80px",
    fontFamily: "system-ui"
  },

  title: {
    marginBottom: "40px"
  },

  card: {
    background: "white",
    padding: "30px",
    borderRadius: "12px",
    maxWidth: "600px"
  },

  question: {
    marginBottom: "20px",
    fontSize: "18px"
  },

  option: {
    display: "block",
    width: "100%",
    marginBottom: "10px",
    padding: "12px",
    borderRadius: "8px",
    border: "1px solid #ddd",
    cursor: "pointer"
  }

};