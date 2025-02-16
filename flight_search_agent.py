import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from datetime import datetime

class FlightSearchAgent:
    def __init__(self):
        # Initialize the model with proper authentication
        self.agent = CodeAgent(
            tools=[DuckDuckGoSearchTool()],
            model=HfApiModel(
                max_tokens=2096,
                temperature=0.5,
                model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
                custom_role_conversions=None,
                token=os.getenv('HF_API_KEY')
            )
        )
        self.origin = None
        self.destination = None
        self.date = None

    def search_flights(self, origin, destination, date):
        """Search for flights using AI agent."""
        print(f"Starting flight search: {origin} -> {destination} on {date}")
        self.origin = origin
        self.destination = destination
        self.date = date
        
        prompt = f"""
        Search for flights from {origin} to {destination} on {date}.
        Return the top 5 flight options with:
        - Airline name
        - Flight number
        - Departure time
        - Arrival time
        - Price
        - Duration
        """
        print("Generated search prompt")
        
        try:
            result = self.agent.run(prompt)
            print("API request successful, processing results...")
            flights = self._process_flights(result)
            print(f"Found {len(flights)} flights")
            return flights
        except Exception as e:
            print(f"Error searching flights: {e}")
            print("Returning empty flight list")
            return []

    def _process_flights(self, result):
        """Process the AI agent's flight search results."""
        print("Processing flight results...")
        processed_flights = []
        
        # Example processing (modify based on actual agent output)
        if isinstance(result, list):
            for flight in result:
                processed_flights.append({
                    'airline': flight.get('airline', 'Unknown'),
                    'flight_number': flight.get('flight_number', 'Unknown'),
                    'departure': flight.get('departure', 'Unknown'),
                    'arrival': flight.get('arrival', 'Unknown'),
                    'price': float(flight.get('price', float('inf'))),
                    'duration': self._calculate_duration(
                        flight.get('departure'),
                        flight.get('arrival')
                    )
                })
        
        # Sort flights by price, then by duration
        sorted_flights = sorted(processed_flights, key=lambda x: (x['price'], x['duration']))
        top_flights = sorted_flights[:5]
        print(f"Selected top {len(top_flights)} flights")
        return top_flights

    def _calculate_duration(self, departure_time, arrival_time):
        """Calculate flight duration in minutes."""
        try:
            dep_time = datetime.fromisoformat(departure_time)
            arr_time = datetime.fromisoformat(arrival_time)
            duration = (arr_time - dep_time).total_seconds() / 60
            return duration
        except:
            return float('inf')

    def get_best_flight(self, origin, destination, date):
        """Get the best flight option based on price and duration."""
        flights = self.search_flights(origin, destination, date)
        return flights[0] if flights else None

# Example usage
if __name__ == "__main__":
    flight_agent = FlightSearchAgent()
    
    origin = "DEL"  # Delhi
    destination = "BLR"  # Bangalore
    date = "2023-10-15"  # Example date
    
    best_flight = flight_agent.get_best_flight(origin, destination, date)
    if best_flight:
        print(f"Best flight found: {best_flight}")
    else:
        print("No flights found.")
