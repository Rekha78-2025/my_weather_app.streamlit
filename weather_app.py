import streamlit as st 
import requests

st.title("🌧️ My weather App")

 
Indian_cities_name = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata",
    "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal",
    "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi",
    "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad",
    "Ranchi", "Howrah", "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur",
    "Madurai", "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubli–Dharwad",
    "Bareilly", "Mysore", "Tiruchirappalli", "Tiruppur", "Moradabad", "Jalandhar",
    "Bhubaneswar", "Salem", "Warangal", "Guntur", "Bhiwandi", "Saharanpur", "Gorakhpur",
    "Bikaner", "Amravati", "Noida", "Jamshedpur", "Bhilai", "Cuttack", "Firozabad",
    "Kochi", "Nellore", "Bhavnagar", "Dehradun", "Durgapur", "Asansol", "Rourkela",
    "Nanded", "Kolhapur", "Ajmer", "Akola", "Gulbarga", "Jamnagar", "Ujjain", "Loni",
    "Siliguri", "Jhansi", "Ulhasnagar", "Nellore", "Jammu", "Mangalore", "Erode",
    "Belgaum", "Kurnool", "Ambattur", "Tirunelveli", "Malegaon", "Gaya", "Udaipur",
    "Maheshtala", "Davanagere", "Kozhikode", "Kakinada", "Agartala", "Bilaspur", "Allahabad(paryagraj)"]


API_KEY = "770f005c98bcf79dd0ae095605536a92"


choice = st.selectbox("Choose your city name", Indian_cities_name)

if choice:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_KEY}"
    
    response = requests.get(url) 
    
    if response.status_code == 200:
        st.write("API working")
        # st.json(response.json())
        
        weather_info = response.json()
        
        # st.write(weather_info["weather"][0]["main"])
        
        st.json(weather_info)
           
    else:
        st.write("something went wrong")
      
    
   
    
    