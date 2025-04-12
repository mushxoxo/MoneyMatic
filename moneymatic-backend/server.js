const express = require('express');
const cors = require('cors');
const path = require('path');
const connectDB = require('./config/db');
const authRoutes = require('./routes/auth');
const authMiddleware = require('./middleware/auth');
require('dotenv').config();

const app = express();

// Connect to MongoDB
connectDB();

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files from the frontend directory
const frontendPath = path.join(__dirname, '../frontend');
app.use(express.static(frontendPath));

// Routes
app.use('/api', authRoutes);

// Protected route example (dashboard)
app.get('/api/dashboard', authMiddleware, (req, res) => {
  res.json({ message: 'Welcome to the dashboard', userId: req.user.userId });
});

// Serve index.html for the root route
app.get('/', (req, res) => {
  res.sendFile(path.join(frontendPath, 'index.html'));
});

// Serve dashboard.html for the dashboard route
app.get('/dashboard', (req, res) => {
  res.sendFile(path.join(frontendPath, 'login', 'dashboard.html'));
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));