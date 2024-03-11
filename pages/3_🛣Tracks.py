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

st.write("You have entered", st.session_state["my_input"])
st.header = ("Top 10 Formula 1 drivers in 2024")
st.video("https://youtu.be/UDSyKMsyY68?si=d1YPjqj-ExqJW4CL")
st.markdown("F1 tracks board of 2024")
st.text("This website refer to:")
st.markdown("[https://www.formula1.com/](https://www.formula1.com/)  -  [https://en.wikipedia.org/wiki/Formula_One](https://en.wikipedia.org/wiki/Formula_One)")
st.write("---")

tracks = {
    "Bahrain International Circuit": {
        "description": "The Bahrain International Circuit (BIC) is a motorsport track opened in 2004 and used for auto racing. The main race is the Bahrain Grand Prix. The 2004 Grand Prix was the first held in the Middle East. In 2006, Australian V8 Supercar started racing at the BIC. 24 Hour endurance races also hosted at BIC.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Bahrain_International_Circuit--Grand_Prix_Layout.svg/1024px-Bahrain_International_Circuit--Grand_Prix_Layout.svg.png",
    },
    "Jeddah Corniche Circuit": {
        "description": "Jeddah Street Circuit is a racing track in the Jeddah city. The track is to held in the inaugural Formula One Saudi Arabian Grand Prix as the penultimate race on the season calendar. It will be the second longest track on the Formula One calendar (only Spa-Francorchamps is longer). The track was designed by Hermann Tilke.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Jeddah_Street_Circuit_2021.svg/1280px-Jeddah_Street_Circuit_2021.svg.png",
    },
    "Melbourne Grand Prix Circuit": {
        "description": "The Melbourne Grand Prix Circuit is a street circuit around Albert Park Lake, only a couple of kilometres south of central Melbourne. It is used once a year as a racetrack for the Australian Grand Prix and associated support races.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg/1024px-Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg.png",
    },
    "Suzuka Circuit": {
        "description": "Suzuka International Racing Course, Suzuka Circuit for short, is a motorsports race track in Ino, Suzuka City, Mie Prefecture, Japan. It is managed by Mobilityland Corporation, a subsidiary of Honda Motor Co., Ltd..",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/79/Circuit_Suzuka.png",
    },
    "Shanghai International Circuit": {
        "description": "The Shanghai International Circuit is a Chinese motor racing venue. It is in the district of Jiading near Shanghai in the People's Republic of China. It was the venue of the first Formula One Chinese Grand Prix on 26 September 2004.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Shanghai_International_Racing_Circuit_track_map.svg/1280px-Shanghai_International_Racing_Circuit_track_map.svg.png",
    },
    "Miami International Autodrome": {
        "description": "The Miami International Autodrome is a purpose-built temporary circuit around Hard Rock Stadium and its private facilities in the Miami suburb of Miami Gardens, Florida, United States. The track is 3.363 mi (5.412 km) long and features 19 corners with an anticipated average speed of around 140 mph (230 km/h). The track was designed and delivered by Formula One track designers, Apex Circuit Design, for the Miami Grand Prix, which was added to the Formula One calendar for the 2022 World Championship.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Hard_Rock_Stadium_Circuit_2022.svg/1920px-Hard_Rock_Stadium_Circuit_2022.svg.png",
    },
    "Autodromo Enzo e Dino Ferrari": {
        "description": "The Autodromo Internazionale Enzo e Dino Ferrari is an auto racing circuit near the Italian town of Imola, 40 kilometres (24.9 mi) east of Bologna and 80 kilometres (49.7 mi) east of the Ferrari factory in Maranello. Often, it is simply called Imola.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Imola_2009.svg/1280px-Imola_2009.svg.png",
    },
    "Circuit de Monaco": {
        "description": "Circuit de Monaco is the name given to a motor racing circuit laid out on the city streets of Monte Carlo and La Condamine around the harbor of the principality of Monaco. It is commonly referred to as Monte Carlo because it is largely inside the Monte Carlo neighborhood of Monaco.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Circuit_Monaco.svg/800px-Circuit_Monaco.svg.png",
    },
    "Circuit Gilles Villeneuve": {
        "description": "The Circuit Gilles Villeneuve is a motor racing circuit. It is the location the Formula One Canadian Grand Prix, NASCAR Canadian Tire Series, NASCAR Nationwide Series and Grand-Am Rolex Sports Car Series.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/%C3%8Ele_Notre-Dame_%28Circuit_Gilles_Villeneuve%29.svg/1024px-%C3%8Ele_Notre-Dame_%28Circuit_Gilles_Villeneuve%29.svg.png",
    },
    "Circuit de Catalunya": {
        "description": "The Circuit de Catalunya is a racetrack in Montmeló, to the north of Barcelona, Catalonia. It is home to the Formula One Spanish Grand Prix and the motorcycle Catalonia Grand Prix. With long straights and a variety of corners, the Circuit de Catalunya is seen as an all-rounder circuit. It is often used for off-season testing.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Formula1_Circuit_Catalunya.svg/1920px-Formula1_Circuit_Catalunya.svg.png",
    },
    "Red Bull Ring": {
        "description": "The Red Bull Ring is a motorsport race track in Spielberg, Styria, Austria. The race circuit was founded as Österreichring (translation: Austrian Circuit) and hosted the Austrian Grand Prix for 18 consecutive years, from 1970 to 1987. It was later shortened, rebuilt and renamed the A1-Ring (A Eins-Ring), and it hosted the Austrian Grand Prix again from 1997 to 2003",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Red_Bull_Ring_moto_2022.svg/1024px-Red_Bull_Ring_moto_2022.svg.png",
    },
    "Silverstone Circuit": {
        "description": "Silverstone Circuit is an English motor racing circuit next to the Northamptonshire villages of Silverstone and Whittlebury. Nearly half of the circuit is across the Northamptonshire boundary in Buckinghamshire. The closest large towns are Northampton and Milton Keynes. It is best known as the home of the British Grand Prix, which it first hosted in 1948 and which has been held on the circuit every year since 1987. The circuit is also home to the BRDC International Trophy, awarded to the winner of a race for historic F1 cars at the annual Silverstone Classic meeting.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Silverstone_circuit_opposite_straight.svg/1280px-Silverstone_circuit_opposite_straight.svg.png",
    },
    "Hungaroring": {
        "description": "The Hungaroring is a Formula One racing circuit in Mogyoród, near Budapest, Hungary where the Hungarian Grand Prix is held. In 1986, it became the location of the first Formula One Grand Prix behind the Iron Curtain. Formula One leader Bernie Ecclestone wanted a race in the USSR, but was not able to make a deal with Moscow. A Hungarian friend of his recommended the city of Budapest. Formula One wanted a street circuit similar to the Circuit de Monaco to be built in the Népliget,",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Hungaroring.svg/800px-Hungaroring.svg.png",
    },
    "Circuit de Spa-Francorchamps": {
        "description": "The Circuit de Spa-Francorchamps is the venue of the Formula One Belgian Grand Prix and the Spa 24 Hours and 1000 km Spa endurance races. It is also home to the all Volkswagen club event, 25 Hours of Spa, run by the Uniroyal Fun Cup. It is one of the most challenging race tracks in the world. This is mainly because of its fast, hilly and twisty nature. Spa is a favourite circuit of many racing drivers and fans.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Spa-Francorchamps_of_Belgium.svg/1280px-Spa-Francorchamps_of_Belgium.svg.png",
    },
    "Circuit Zandvoort": {
        "description": "Circuit Zandvoort known for sponsorship reasons as CM.com Circuit Zandvoort, previously known as Circuit Park Zandvoort until 2017, is a 4.259 km (2.646 mi) motorsport race track located in the dunes north of Zandvoort, the Netherlands, near the North Sea coast line. It returned to the Formula One calendar in 2021 as the location of the revived Dutch Grand Prix.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Zandvoort_Circuit.png/800px-Zandvoort_Circuit.png",
    },
    "Autodromo Nazionale Monza": {
        "description": "Autodromo Nazionale Monza is a motorsport race track. It is near the town of Monza, Italy, north of Milan. It is one of the oldest motor racing tracks in the world. It was built in 1922, and has been used for the Italian Grand Prix almost every year since.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Circuit_Monza.png",
    },
    "Baku City Circuit": {
        "description": "Bakı Şəhər Halqası (English: Baku City Circuit, formerly Baku Street Circuit) is a racetrack in Azerbaijan. It is located in Baku. The track hosts the Formula One Grand Prix (in 2016 it was the European Grand Prix, and since 2017 it has been the Azerbaijan Grand Prix). It was designed by Hermann Tilke.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Baku_Formula_One_circuit_map.svg/1024px-Baku_Formula_One_circuit_map.svg.png",
    },
    "Marina Bay Street Circuit": {
        "description": "The Marina Bay Street Circuit (otherwise known as the Singapore Street Circuit) is a street circuit around the Marina Bay. It is the track for the Singapore Grand Prix. The track is 5.073 km (3.15 miles) long. It is next to the harbour, similar in style to the Monaco Grand Prix.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Marina_Bay_circuit_2023.svg/1280px-Marina_Bay_circuit_2023.svg.png",
    },
    "Circuit of the Americas": {
        "description": "The Circuit of the Americas is a motor racing circuit in Austin, Texas. Hermann Tilke designed the circuit in the middle of 2010. Construction was started in early 2011. It is planned to open in 2012. The circuit will run counter-clockwise.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Austin_circuit.svg/800px-Austin_circuit.svg.png",
    },
    "Autódromo Hermanos Rodríguez": {
        "description": "The Autódromo Hermanos Rodríguez is a Mexican Formula One circuit near Mexico City. It was named after racing driver Ricardo Rodríguez (the brother of Pedro Rodríguez, a Formula One driver). It was finished in 1962 and held its first Formula One race there in the same year, though it did not count for the championship. A year later, the Mexican Grand Prix started, and continued from 1963 to 1970, where F1 did not return until 1986, and left once again 1992. The track still hosts various events, and even hosted the Nationwide Series from 2005 to 2008, before leaving once again.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Autodromo_Hermanos_Rodriguez_1963.svg/1024px-Autodromo_Hermanos_Rodriguez_1963.svg.png",
    },
    "Interlagos Circuit": {
        "description": "Autódromo José Carlos Pace, also known by its former name Interlagos, is a motor racing circuit. It is in the city of São Paulo. It is named after Carlos Pace. Pace was a Brazilian Formula One driver, who died in 1977. The track was renamed in his honor. It is well known for being the venue of the Formula One Brazilian Grand Prix.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace_%28AKA_Interlagos%29_track_map.svg/1280px-Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace_%28AKA_Interlagos%29_track_map.svg.png",
    },
    "Las Vegas Strip Circuit": {
        "description": "The Las Vegas Strip Circuit is a street circuit around parts of the Las Vegas Strip in Paradise, Nevada, immediately adjacent to Las Vegas, Nevada. It winds through the streets of the city and comprises the Las Vegas Strip, a section of Las Vegas Boulevard that is home to the city's major hotels and casinos. It incorporates some of the most notable landmarks of the city, including the Sphere, Caesars Palace, Bellagio, and Paris Las Vegas.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Las_Vegas_Strip_Circuit_2023.png",
    },
    "Losail International Circuit": {
        "description": "The Losail International Circuit or Lusail International Circuit (Arabic: حلبة لوسيل الدولية) is a motor racing circuit located just outside the city of Lusail, north of Doha, Qatar. The track is 5.419 km (3.367 mi) in length, with a main straight of 1.068 km (0.664 mi). It is surrounded by artificial grass intended to stop the sand encroaching on the track.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Lusail_International_Circuit_2023.svg/1024px-Lusail_International_Circuit_2023.svg.png",
    },
    "Yas Marina Circuit": {
        "description": "The Yas Marina Circuit is a race track. The Abu Dhabi Grand Prix is held there. The track was designed by Hermann Tilke. It is on Yas Island, about 30 minutes from the capital of the UAE, Abu Dhabi. Yas Marina is the second Formula One track in the Middle East. The first was Bahrain. It also hosted the opening event for the Australian V8 Supercars series, the Yas V8 400, in February 2010.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Circuit_Yas-Island.svg/800px-Circuit_Yas-Island.svg.png",
    },
}

search_query = st.sidebar.text_input("Search your tracks name.", "")
search_button = st.sidebar.button('Search')

if search_button:
    filtered_tracks = {key: value for key, value in tracks.items() if search_query.lower() in key.lower()}
else:
    filtered_tracks = tracks

for track_name, track_info in filtered_tracks.items():
    track_info = tracks[track_name]
    st.subheader(track_name)
    st.image(track_info["image"], caption=track_name, width=100, use_column_width='always', output_format='auto')
    st.write(track_info["description"])
    st.write("---")