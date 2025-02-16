import streamlit as st
from flight_search_agent import FlightSearchAgent
from datetime import datetime

# Set up the Streamlit app
st.title("Flight Search AI Agent")
st.write("Find the best flights using AI!")

# Create input fields
col1, col2 = st.columns(2)
with col1:
    origin = st.text_input("Origin Airport Code (e.g., DEL)", "DEL")
with col2:
    destination = st.text_input("Destination Airport Code (e.g., BLR)", "BLR")

date = st.date_input("Travel Date", datetime.now())

# Search button
if st.button("Search Flights"):
    # Initialize the agent
    flight_agent = FlightSearchAgent()
    
    # Perform the search
    with st.spinner("Searching for flights..."):
        best_flight = flight_agent.get_best_flight(origin, destination, date.strftime("%Y-%m-%d"))
    
    # Display results
    if best_flight:
        st.success("Best flight found!")
        st.subheader("Flight Details")
        st.write(f"**Airline:** {best_flight['airline']}")
        st.write(f"**Flight Number:** {best_flight['flight_number']}")
        st.write(f"**Departure:** {best_flight['departure']}")
        st.write(f"**Arrival:** {best_flight['arrival']}")
        st.write(f"**Price:** {best_flight['price']}")
        st.write(f"**Duration:** {best_flight['duration']}")
    else:
        st.warning("No flights found for the selected criteria.")

# Instructions
st.markdown("""
### Instructions:
1. Enter the 3-letter airport codes for origin and destination
2. Select your travel date
3. Click 'Search Flights' to find the best option
""")
