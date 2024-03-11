import streamlit as st

st.set_page_config(
    page_title = "Formula 1 2024",
    page_icon = "🏎"
)

bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://preview.redd.it/dux4xq5v0zs41.jpg?width=1080&crop=smart&auto=webp&s=e1fddcfebc5b99225cf1bf1a3297e450cc840b6a");
background-size: cover;
}

}
</style>
"""
st.markdown(bg, unsafe_allow_html=True)

st.header = ("Top 10 Formula 1 drivers in 2024")
st.write("You have entered", st.session_state["my_input"])
st.video("https://youtu.be/T93qx70JyxA?si=FO-aj6F5AxEnYptE")
st.markdown("F1 driver board of 2024")
st.text("This website refer to:")
st.markdown("[https://www.formula1.com/](https://www.formula1.com/)  -  [https://en.wikipedia.org/wiki/Formula_One](https://en.wikipedia.org/wiki/Formula_One)")
st.write("---")

racers = {
    "Max Verstappen": {
        "description": "Max Emilian Verstappen was born 30 September 1997 is a Belgian and Dutch racing driver competing in Formula One, where he is the 2021, 2022, and 2023 World Champion. He races under the Dutch flag in Formula One for Red Bull Racing.Verstappen is the son of former Formula One driver Jos Verstappen, and former go-kart racer Sophie Kumpen. He had a successful run in karting and single-seater categories – including FIA European Formula 3 – breaking several records.",
        "image": "https://a.espncdn.com/i/headshots/rpm/players/full/4665.png",
    },
    "Lewis Hamilton": {
        "description": "Sir Lewis Carl Davidson Hamilton MBE HonFREng (born 7 January 1985) is a British racing driver competing in Formula One, driving for Mercedes, and has also driven for McLaren. Hamilton has won a joint-record seven Formula One World Drivers' Championship titles (tied with Michael Schumacher), and holds the records for most number of wins (103), pole positions (104), and podium finishes (197), among other records.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/868.png",
    },
    "Charles Leclerc": {
        "description": "Charles Marc Hervé Perceval Leclerc was born 16 October 1997 is a Monégasque racing driver, currently racing in Formula One for Scuderia Ferrari. He won the GP3 Series championship in 2016 and the FIA Formula 2 Championship in 2017.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/5498.png",
    },
    "Sergio Pérez": {
        "description": "Sergio Michel Checo Pérez Mendoza was born 26 January 1990 is a Mexican racing driver who races in Formula One for Red Bull Racing, having previously driven for Sauber, McLaren, Force India, and Racing Point. He has won 6 Grand Prix races and scored 36 podium finishes.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/4472.png",
    },
    "Carlos Sainz Jr.": {
        "description": "Carlos Sainz Vázquez de Castro was born 1 September 1994 is a Spanish racing driver currently competing in Formula One for Scuderia Ferrari. He is the son of Carlos Sainz Sr., a double World Rally Champion.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/4686.png&w=350&h=254",
    },
    "Lando Norris": {
        "description": "Lando Norris was born 13 November 1999 is a British and Belgian racing driver currently competing in Formula One with McLaren, racing under the British flag. He won the MSA Formula championship in 2015, and the Toyota Racing Series, Eurocup Formula Renault 2.0 and Formula Renault 2.0 Northern European Cup in 2016. He also received the McLaren Autosport BRDC Award that year.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/5579.png&w=350&h=254",
    },
    "George Russell": {
        "description": "George William Russell was born 15 February 1998 is a British racing driver currently competing in Formula One for Mercedes. He previously raced for Williams from 2019 to 2021. After winning several karting championships including the CIK-FIA European Karting Championship in 2012, he repeated his success by becoming the 2018 Formula 2 champion and the 2017 GP3 Series champion.",
        "image": "https://a.espncdn.com/i/headshots/rpm/players/full/5503.png",
    },
    "Oscar Piastri": {
        "description": "Oscar Jack Piastri was born 6 April 2001 is an Australian racing driver currently competing in Formula One for McLaren. Piastri won the 2019 Formula Renault Eurocup with R-ace GP, and won the 2020 FIA Formula 3 Championship and 2021 Formula 2 Championship with Prema Racing.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/5752.png&w=350&h=254",
    },
    "Fernando Alonso": {
        "description": "Fernando Alonso Díaz was born 29 July 1981 is a Spanish racing driver currently competing for Aston Martin in Formula One. He won the series' World Drivers' Championship in 2005 and 2006 with Renault, and has also driven for McLaren, Ferrari, and Minardi. With Toyota, Alonso won the 24 Hours of Le Mans twice, in 2018 and 2019.",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/348.png",
    },
    "Lance Stroll": {
        "description": "Lance Strulovitch was born 29 October 1998 better known as Lance Stroll, is a Canadian and Belgian racing driver competing under the Canadian flag in Formula One. He has driven for Aston Martin since 2021, having previously driven for Williams and Racing Point. He was Italian F4 champion in 2014",
        "image": "https://a.espncdn.com/combiner/i?img=/i/headshots/rpm/players/full/4775.png",
    },
    
}

search_query = st.sidebar.text_input("Search your driver name.", "")
search_button = st.sidebar.button('Search')

if search_button:
    filtered_racers = {key: value for key, value in racers.items() if search_query.lower() in key.lower()}
else:
    filtered_racers = racers

for racer_name, racer_info in filtered_racers.items():
    racer_info = racers[racer_name]
    st.subheader(racer_name)
    st.image(racer_info["image"], caption=racer_name, width=200, use_column_width='always', output_format='auto')
    st.write(racer_info["description"])
    st.write("---")