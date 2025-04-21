# Feedback Form App

A Flask-based web application for collecting and managing user feedback with a clean, responsive interface. The application features a modern design using Bootstrap and custom CSS styling.

## Features

- 🎯 User-friendly feedback submission form
- 📧 Email validation for feedback submissions
- 📝 Rich text area with word counter (up to 500 words)
- 📊 View all submitted feedbacks in a responsive table
- 🎨 Custom styling with a professional color scheme
- 📱 Fully responsive design for all devices

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with Flask-SQLAlchemy
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3
- **JavaScript**: Dynamic word counting and form validation

## Project Structure

```
Feedback Form App/
│
├── app.py                  # Main Flask application file
├── models.py              # Database models and user management
├── instance/
│   └── feedbacks.db       # SQLite database file
├── static/
│   └── style.css         # Custom CSS styles
├── templates/
│   ├── index.html        # Main feedback form page
│   ├── thankyou.html     # Success page after submission
│   └── all_feedbacks.html # Feedback listing page
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Feedback Form App"
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask flask-sqlalchemy
```

4. Initialize the database:
The database will be automatically created when you run the application for the first time.

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

### Submitting Feedback
1. Navigate to the home page
2. Fill out the feedback form with:
   - Name (required)
   - Email (required)
   - Feedback message (required, up to 500 words)
3. Click the "Submit Feedback" button

### Viewing Feedbacks
1. Click on "All Feedbacks" in the navigation bar
2. View all submitted feedbacks in a table format

## API Endpoints

- `GET /` - Home page with feedback form
- `POST /submit` - Submit new feedback
- `GET /feedbacks` - JSON API endpoint for all feedbacks
- `GET /all-feedbacks` - HTML page showing all feedbacks

## Database Schema

### Feedback Table
- `id` (Integer, Primary Key)
- `name` (String, 100 characters)
- `email` (String, 100 characters)
- `feedback` (Text)

## Styling

The application uses a custom color scheme:
- Background: #edffc9
- Navigation: #013846
- Accents: rgb(252, 165, 2)
- Text: Various complementary colors

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Bharati Patil

## Future Enhancements

- User authentication system
- Admin dashboard
- Email notifications for new feedback
- Feedback categorization
- Export feedback to CSV/PDF
- Rich text formatting in feedback