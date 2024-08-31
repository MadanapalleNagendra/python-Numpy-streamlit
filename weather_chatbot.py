import streamlit as st
import requests

# Function to check login credentials
def check_login(username, password):
    # Hardcoded credentials for simplicity
    if username == "virat" and password == "0018":
        return True
    else:
        return False


def get_weather(city, api_key):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}

    headers = {
        "x-rapidapi-key": "307431743dmsh2ab45047fc0e69cp1e2160jsncb6c225fc228", 
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    try:
        data = response.json()

        if "current" in data:
            current = data["current"]
            weather_description = current["condition"]["text"]
            return f"The temperature in {city.capitalize()} is {current['temp_c']}°C with {weather_description}."
        else:
            # Handle cases where the response doesn't have the 'current' key
            if "error" in data:
                return f"Error: {data['error']['message']}"
            else:
                return "Unexpected error occurred."
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except ValueError:
        return "Error parsing the API response."

# Function to handle the login page
def login():
    # Set the background image for the login page
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://imgur.com/an0AFto.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to trigger the login process
    if st.button("Login"):
        if check_login(username, password):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# Main function
def main():
    # Check if the user is logged in
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        login()  # Show the login page if not logged in
    else:
        # Set the background image for the weather chatbot
        st.markdown(
            """
            <style>
            .stApp {
                background-image: url("https://imgur.com/Sqzpknq.jpg");
                background-size: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("Simple Weather Chatbot")

        # Input field for user message
        user_input = st.text_input("You: ", "")

        # Your OpenWeatherMap API key
        api_key = "your_rapidapi_key_here"  

        # Process user input and provide a response
        if user_input:
            if "weather" in user_input.lower():
                # Extract the city from the user's message
                city = user_input.split("in")[-1].strip()
                response = get_weather(city, api_key)
            elif "hello" in user_input.lower():
                response = "Hello! How can I assist you today?"
            elif "hi" in user_input.lower():
                response = "Hi there! What can I do for you?"
            elif "how are you" in user_input.lower():
                response = "I'm just a bot, but I'm here to help you!"
            elif "bye" in user_input.lower():
                response = "Goodbye! Have a great day!"
            elif "thank you" in user_input.lower():
                response = "You're welcome!"
            else:
                response = "I'm sorry, I don't understand that."

            # Display the response from the chatbot
            st.write(f"Chatbot: {response}")

# Run the app
if __name__ == "__main__":
    main()
