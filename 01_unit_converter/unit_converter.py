import streamlit as st

categories = {
    "Length": ["meter", "kilometer", "millimeter"],
    "Mass": ["gram", "kilogram", "milligram"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Frequency": ["hertz", "kilohertz", "megahertz"]
     }
def convert_units(value, unit_from, unit_to):

    # Conversion factors for unit conversions
    convertions = {
        #Length set: all conversions are in meters
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "meter_millimeter": 1000, # 1 meter = 1000 millimeters
        "millimeter_meter": 0.001, # 1 millimeter = 0.001 meters
        "kilometer_millimeter": 1000000, # 1 kilometer = 1000000 millimeters
        "millimeter_kilometer": 0.000001, # 1 millimeter = 0.000001 kilometers

        #Mass set: all conversions are in grams
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000,     # 1 kilogram = 1000 grams
        "gram_milligram":1000,   # 1 gram = 1000 milligrams
        "milligram_gram":0.001,   # 1 milligram = 0.001 grams
        "kilogram_milligram":1000000, # 1 kilogram = 1000000 milligrams
        "milligram_kilogram":0.000001, # 1 milligram = 0.000001 kilograms


        # Temprature set: all conversions are in celsius
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32, # 1 Celsius = 33.8 Fahrenheit
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9, # 1 Fahrenheit = -17.2222 Celsius
        "celsius_kelvin": lambda c: c + 273.15,    # 1 Celsius = 274.15 Kelvin
        "kelvin_celsius": lambda k: k - 273.15,  # 1 Kelvin = -272.15 Celsius
        "fahrenheit_kelvin": lambda f: (f - 32) * 5/9 + 273.15,   # 1 Fahrenheit = 255.372 Kelvin
        "kelvin_fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,   # 1 Kelvin = 491.67 Fahrenheit

        # Frequency set: all conversions are in hertz
        "hertz_kilohertz": 0.001,  # 1 hertz = 0.001 kilohertz
        "kilohertz_hertz": 1000,   # 1 kilohertz = 1000 hertz
        "hertz_megahertz": 0.000001, # 1 hertz = 0.000001 megahertz
        "megahertz_hertz": 1_000_000, # 1 megahertz = 1_000_000 hertz
        "kilohertz_megahertz": 0.001,  # 1 kilohertz = 0.001 megahertz
        "megahertz_kilohertz": 1000    # 1 megahertz = 1000 kilohertz
    }
    
    key = f"{unit_from}_{unit_to}"

    if key in convertions:
        convertion = convertions[key]
        return value * convertion
    else:
        return "invalid conversion type"
  
    
    
st.title("CONVERTER UNIT - ENTER VALUE TO GET RESULT")
value = st.number_input("Enter the value to convert it( minium 0): ",min_value= 1.0, step = 1.0 )
selected_category = st.selectbox("Select Category", list(categories.keys()))
unit_from =st.selectbox("convert from: ",categories[selected_category])
unit_to =st.selectbox("convert to: ", categories[selected_category])
if st.button("Convert"):
    result = convert_units(value, unit_from,unit_to)
    st.write(f"Result:{result}") 