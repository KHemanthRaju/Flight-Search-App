# Flight Search AI Agent

## Overview

The Flight Search AI Agent is a powerful tool that helps users find the best flight options using AI. It searches for flights based on origin, destination, and date, then presents the top 5 options sorted by price and duration.

## Features

- AI-powered flight search
- Real-time flight information
- Easy-to-use interface
- Secure API key management
- Deployment ready

## Installation

### Prerequisites

- Python 3.10 or higher
- Git

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/KHemanthRaju/Flight-Search-App.git
   cd Flight-Search-App
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```bash
   echo "HF_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Running Locally

1. Start the Streamlit app:

   ```bash
   streamlit run flight_search_app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your search criteria:

   - Origin airport code (e.g., DEL)
   - Destination airport code (e.g., BLR)
   - Travel date

4. Click "Search Flights" to see results

### Deployment

This project is configured for deployment to GitHub Pages. Follow these steps:

1. Add your Hugging Face API key to GitHub Secrets
2. Push your changes to the main branch
3. Enable GitHub Pages in repository settings

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For any issues or questions, please open an issue on GitHub.
