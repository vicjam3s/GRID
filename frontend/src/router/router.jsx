import { createBrowserRouter } from "react-router-dom";

import Dashboard from "../pages/Dashboard";

/* Learning */

import LearningDashboard from "../pages/learning/Dashboard";

/* PPL */

import PPLDashboard from "../pages/learning/ppl/Dashboard";
import PPLSubjects from "../pages/learning/ppl/Subjects";
import PPLSubjectDetail from "../pages/learning/ppl/SubjectDetail";
import PPLNotes from "../pages/learning/ppl/Notes";
import PPLQuiz from "../pages/learning/ppl/Quiz";
import PPLExam from "../pages/learning/ppl/Exam";

/* CPL */

import CPLDashboard from "../pages/learning/cpl/Dashboard";
import CPLSubjects from "../pages/learning/cpl/Subjects";
import CPLSubjectDetail from "../pages/learning/cpl/SubjectDetail";
import CPLNotes from "../pages/learning/cpl/Notes";
import CPLQuiz from "../pages/learning/cpl/Quiz";
import CPLExam from "../pages/learning/cpl/Exam";

/* Flight */

import FlightDashboard from "../pages/flight/Dashboard";
import FlightPlanner from "../pages/flight/FlightPlanner";


export const router = createBrowserRouter([

  {
    path: "/",
    element: <Dashboard />,
  },

  /* Learning Entry */

  {
    path: "/learning",
    element: <LearningDashboard />,
  },

  /* Programme Branches */

  {
    path: "/learning/ppl",
    element: <PPLDashboard />,
  },

  {
    path: "/learning/cpl",
    element: <CPLDashboard />,
  },

  /* Generic Learning Routes */

  {
    path: "/learning/ppl/subjects",
    element: <PPLSubjects />,
  },

  {
    path: "/learning/ppl/subjects/:id",
    element: <PPLSubjectDetail />,
  },

  {
    path: "/learning/ppl/notes",
    element: <PPLNotes />,
  },

  {
    path: "/learning/ppl/quiz",
    element: <PPLQuiz />,
  },

  {
    path: "/learning/ppl/exam",
    element: <PPLExam />,
  },

  // cpl

    {
    path: "/learning/cpl/subjects",
    element: <CPLSubjects />,
    },

    {
      path: "/learning/cpl/subjects/:id",
      element: <CPLSubjectDetail />,
    },

    {
      path: "/learning/cpl/notes",
      element: <CPLNotes />,
    },

    {
      path: "/learning/cpl/quiz",
      element: <CPLQuiz />,
    },

    {
      path: "/learning/cpl/exam",
      element: <CPLExam />,
    },

  /* Flight */

  {
    path: "/flight",
    element: <FlightDashboard />,
  },

  {
    path: "/flight/planner",
    element: <FlightPlanner />,
  },

  {
    path: "/learning/ppl/subjects",
    element: <PPLSubjects />,
  },

  {
    path: "/learning/ppl/subjects/:id",
    element: <PPLSubjectDetail />,
  },

]);