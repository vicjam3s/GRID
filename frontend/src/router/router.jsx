import { createBrowserRouter } from "react-router-dom";

import Dashboard from "../pages/Dashboard";

import LearningDashboard from "../pages/learning/Dashboard";
import Subjects from "../pages/learning/Subjects";
import SubjectDetail from "../pages/learning/SubjectDetail";
import Notes from "../pages/learning/Notes";
import Quiz from "../pages/learning/Quiz";
import Exam from "../pages/learning/Exam";

import FlightDashboard from "../pages/flight/Dashboard";
import FlightPlanner from "../pages/flight/FlightPlanner";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard />,
  },

  {
    path: "/learning",
    element: <LearningDashboard />,
  },

  {
    path: "/learning/subjects",
    element: <Subjects />,
  },

  {
    path: "/learning/subjects/:id",
    element: <SubjectDetail />,
  },

  {
    path: "/learning/notes",
    element: <Notes />,
  },

  {
    path: "/learning/quiz",
    element: <Quiz />,
  },

  {
    path: "/learning/exam",
    element: <Exam />,
  },

  {
    path: "/flight",
    element: <FlightDashboard />,
  },

  {
    path: "/flight/planner",
    element: <FlightPlanner />,
  },
]);