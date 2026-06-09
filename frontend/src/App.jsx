import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import { ThemeProvider } from './contexts/ThemeContext'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import LandingPage   from './pages/LandingPage'
import UploadPage    from './pages/UploadPage'
import AnalysisPage  from './pages/AnalysisPage'
import HistoryPage   from './pages/HistoryPage'
import AboutPage     from './pages/AboutPage'

function NotFoundPage() {
  return (
    <div className="min-h-screen pt-28 flex items-center justify-center">
      <div className="text-center">
        <p className="text-8xl mb-4">🔍</p>
        <h1 className="text-3xl font-black text-white mb-2">Page Not Found</h1>
        <p className="text-slate-500 mb-8">The page you&apos;re looking for doesn&apos;t exist.</p>
        <Link to="/" className="btn-glow inline-flex items-center gap-2 px-6 py-3 rounded-xl text-sm font-bold text-white">
          Go Home
        </Link>
      </div>
    </div>
  )
}

function App() {
  return (
    <ThemeProvider>
      <Router>
        <div className="min-h-screen bg-dark font-sans flex flex-col">
          <Navbar />
          <main className="flex-1">
            <Routes>
              <Route path="/"               element={<LandingPage />} />
              <Route path="/upload"         element={<UploadPage />} />
              <Route path="/analysis/:id"   element={<AnalysisPage />} />
              <Route path="/history"        element={<HistoryPage />} />
              <Route path="/about"          element={<AboutPage />} />
              <Route path="*"              element={<NotFoundPage />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </ThemeProvider>
  )
}

export default App
