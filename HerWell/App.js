import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { motion } from "framer-motion";
import Login from "./__pycache__/HerWellPrototype/src/pages/Login";
import Signup from "./__pycache__/HerWellPrototype/src/pages/Signup";
import BookAppointment from "./__pycache__/HerWellPrototype/src/pages/BookAppointment";
import CheckSymptoms from "./__pycache__/HerWellPrototype/src/pages/CheckSymptoms";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/book-appointment" element={<BookAppointment />} />
        <Route path="/check-symptoms" element={<CheckSymptoms />} />
      </Routes>
    </Router>
  );
}

function Header() {
  return (
    <header className="p-4 shadow-md flex justify-between items-center bg-pink-500 text-white">
      <Link to="/">
        <h1 className="text-xl font-bold">HerWell</h1>
      </Link>
      <nav>
        <Link to="/" className="mr-4 hover:underline">Home</Link>
        <Link to="/book-appointment" className="mr-4 hover:underline">Services</Link>
        <Link to="/community" className="mr-4 hover:underline">Community</Link>
        <Link to="/blogs" className="mr-4 hover:underline">Blogs</Link>
        <Link to="/about" className="mr-4 hover:underline">About Us</Link>
        <Link to="/login" className="mr-4 hover:underline">Login</Link>
        <Link to="/signup" className="border px-3 py-1 rounded-full bg-white text-pink-500 hover:bg-pink-100">Create an Account</Link>
      </nav>
    </header>
  );
}

function Home() {
  return (
    <div className="p-6 bg-pink-100 min-h-screen text-center">
      <h2 className="text-3xl font-bold text-pink-700">Empowering Women's Health</h2>
      <p className="text-gray-700 mt-2">Personalized care, expert consultations, and a supportive community.</p>
      <div className="mt-4">
        <Input type="text" placeholder="Check symptoms and treatments..." className="p-2 rounded-md w-1/2" />
      </div>
      <div className="mt-6 flex justify-center gap-4">
        <Button className="bg-pink-500 text-white px-6 py-2 rounded-md">Women's Diet & Workouts</Button>
        <Button className="bg-pink-500 text-white px-6 py-2 rounded-md">Latest Women's Health Highlights</Button>
        <Button className="bg-pink-500 text-white px-6 py-2 rounded-md">Other Relevant Health Topics</Button>
      </div>
      <div className="mt-6">
        <Link to="/book-appointment">
          <Button className="bg-red-500 text-white px-6 py-2 rounded-md">Book an Appointment</Button>
        </Link>
        <Link to="/signup">
          <Button className="border px-6 py-2 rounded-md text-pink-500">Create an Account</Button>
        </Link>
      </div>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-8">
        <Card className="bg-red-100 p-4">One-Tap Ambulance & Emergency Transport</Card>
        <Card className="bg-blue-100 p-4">Instant Doctor Consultations & Telemedicine</Card>
        <Card className="bg-yellow-100 p-4">Women's Safety & Self-Defense Assistance</Card>
        <Card className="bg-green-100 p-4">Emergency Medications & Pharmacy Access</Card>
        <Card className="bg-purple-100 p-4">Mental Health & Trauma Support</Card>
      </div>
    </div>
  );
}

export default App;
