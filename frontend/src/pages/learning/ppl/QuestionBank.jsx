import { useEffect, useState } from "react";
import axios from "axios";

export default function QuestionBank() {

  const [questions, setQuestions] = useState([]);
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [score, setScore] = useState(0);

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/api/questions/?subject=NAV");
      setQuestions(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  if (!questions.length) return <p style={styles.loading}>Loading...</p>;

  const q = questions[current];

  const options = [
    { key: "A", text: q.option_a },
    { key: "B", text: q.option_b },
    { key: "C", text: q.option_c },
    { key: "D", text: q.option_d }
  ];

  const handleSelect = (key) => {
    if (showAnswer) return;

    setSelected(key);
    setShowAnswer(true);

    if (key === q.correct_answer) {
      setScore(score + 1);
    }
  };

  const nextQuestion = () => {
    setCurrent(current + 1);
    setSelected(null);
    setShowAnswer(false);
  };

  return (
    <div style={styles.page}>

      <h1 style={styles.title}>Question Bank</h1>

      <div style={styles.card}>

        <p style={styles.question}>
          {q.question_text}
        </p>

        <div style={styles.options}>
          {options.map((opt) => {

            let bg = "#1E293B";

            if (showAnswer) {
              if (opt.key === q.correct_answer) bg = "#166534"; // green
              else if (opt.key === selected) bg = "#7F1D1D"; // red
            }

            return (
              <button
                key={opt.key}
                onClick={() => handleSelect(opt.key)}
                style={{ ...styles.option, background: bg }}
              >
                <strong>{opt.key}.</strong> {opt.text}
              </button>
            );
          })}
        </div>

        {showAnswer && (
          <div style={styles.explanation}>
            <strong>Explanation:</strong>
            <p>{q.explanation}</p>
          </div>
        )}

        {showAnswer && current < questions.length - 1 && (
          <button style={styles.nextButton} onClick={nextQuestion}>
            Next Question
          </button>
        )}

        <p style={styles.score}>
          Score: {score} / {questions.length}
        </p>

      </div>

    </div>
  );
}


const styles = {

  page: {
    minHeight: "100vh",
    padding: "80px 60px",
    background: "#0F172A",
    color: "#F1F5F9",
    fontFamily: "system-ui"
  },

  title: {
    fontSize: "36px",
    marginBottom: "30px"
  },

  card: {
    maxWidth: "750px",
    background: "rgba(30,41,59,0.9)",
    padding: "30px",
    borderRadius: "14px",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)"
  },

  question: {
    fontSize: "18px",
    marginBottom: "25px",
    lineHeight: "1.6",
    color: "#F1F5F9"
  },

  options: {
    display: "flex",
    flexDirection: "column",
    gap: "12px"
  },

  option: {
    padding: "14px",
    borderRadius: "10px",
    border: "1px solid #334155",
    background: "#020617",
    color: "#F1F5F9",
    cursor: "pointer",
    textAlign: "left",
    transition: "all 0.25s ease"
  },

  explanation: {
    marginTop: "25px",
    padding: "18px",
    background: "#020617",
    borderRadius: "10px",
    border: "1px solid #334155",
    color: "#CBD5F5"
  },

  nextButton: {
    marginTop: "25px",
    padding: "12px 18px",
    borderRadius: "10px",
    background: "#334155",
    border: "1px solid #475569",
    color: "#F1F5F9",
    cursor: "pointer",
    fontWeight: "600",
    transition: "all 0.25s ease"
  },

  score: {
    marginTop: "20px",
    fontSize: "14px",
    color: "#94A3B8"
  },

  loading: {
    color: "#F1F5F9",
    padding: "50px"
  }

};