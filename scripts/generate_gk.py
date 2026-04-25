#!/usr/bin/env python3
"""Generator for General Knowledge category questions."""
import json
import os

QUESTIONS_EN = [
    # Nepal Geography
    {
        "id": 1,
        "question": "What is the total area of Nepal?",
        "options": ["1,47,181 sq km", "1,48,181 sq km", "1,46,181 sq km", "1,45,181 sq km"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "Nepal covers an area of 1,47,181 square kilometers (56,827 sq mi), stretching approximately 885 km east-west and 145-241 km north-south.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 2,
        "question": "Which is the longest river in Nepal?",
        "options": ["Karnali", "Koshi", "Gandaki", "Narayani"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "The Karnali River is the longest river in Nepal, stretching approximately 1,080 km in total length.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 3,
        "question": "What is the highest peak in Nepal?",
        "options": ["Kanchenjunga", "Lhotse", "Makalu", "Mount Everest (Sagarmatha)"],
        "correctIndex": 3,
        "subject": "GK",
        "explanation": "Mount Everest (Sagarmatha) at 8,848.86 meters is the highest peak in Nepal and the world.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 4,
        "question": "Which is the largest lake in Nepal?",
        "options": ["Phewa Lake", "Rara Lake", "Tilicho Lake", "Begnas Lake"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Rara Lake in Mugu district is the largest lake in Nepal, covering about 10.8 sq km at an altitude of 2,990 meters.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 5,
        "question": "Which national park in Nepal is a UNESCO World Heritage Site?",
        "options": ["Shivapuri Nagarjun", "Chitwan National Park", "Sagarmatha National Park", "Both Chitwan and Sagarmatha"],
        "correctIndex": 3,
        "subject": "GK",
        "explanation": "Both Chitwan National Park (natural heritage, 1984) and Sagarmatha National Park (natural heritage, 1979) are UNESCO World Heritage Sites.",
        "reference": "UNESCO World Heritage Sites in Nepal"
    },
    {
        "id": 6,
        "question": "What is the lowest point in Nepal (in terms of elevation)?",
        "options": ["Pokhara", "Birgunj", "Kechana Kalan (Jhapa)", "Bhairahawa"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Kechana Kalan in Jhapa district is the lowest point in Nepal at approximately 59 meters above sea level.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 7,
        "question": "How many districts are there in Nepal currently?",
        "options": ["75", "77", "79", "81"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Nepal currently has 77 districts, after the addition of Nawalparasi East, Nawalparasi West, Rukum East, and Rukum West during federal restructuring.",
        "reference": "Administrative divisions of Nepal"
    },
    {
        "id": 8,
        "question": "Which is the deepest gorge in Nepal?",
        "options": ["Kali Gandaki Gorge", "Marsyangdi Gorge", "Trishuli Gorge", "Arun Gorge"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "The Kali Gandaki Gorge (Andha Galchi) is considered one of the deepest gorges in the world, between Annapurna and Dhaulagiri massifs.",
        "reference": "Geography of Nepal"
    },
    {
        "id": 9,
        "question": "Which region in Nepal receives the highest rainfall?",
        "options": ["Kathmandu Valley", "Pokhara", "Panchthar", "Biratnagar"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Panchthar district in Province No. 1 receives the highest rainfall in Nepal, with some areas getting over 5,000 mm annually.",
        "reference": "Climate of Nepal"
    },
    {
        "id": 10,
        "question": "What is the largest national park in Nepal by area?",
        "options": ["Chitwan National Park", "Sagarmatha National Park", "Shey Phoksundo National Park", "Bardia National Park"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Shey Phoksundo National Park in Dolpa district is the largest national park in Nepal, covering 3,555 sq km.",
        "reference": "National Parks of Nepal"
    },
    # Nepal History
    {
        "id": 11,
        "question": "When was the unification of Nepal completed under Prithvi Narayan Shah?",
        "options": ["1768", "1769", "1770", "1771"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Prithvi Narayan Shah completed the unification of Nepal in 1769 (1826 BS) after capturing Kathmandu Valley.",
        "reference": "History of Nepal"
    },
    {
        "id": 12,
        "question": "When was the Sugauli Treaty signed between Nepal and British India?",
        "options": ["1814", "1815", "1816", "1817"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The Sugauli Treaty was signed on March 4, 1816, after the Anglo-Nepalese War (1814-1816).",
        "reference": "History of Nepal"
    },
    {
        "id": 13,
        "question": "When was the People's Movement (Jana Andolan I) that restored multi-party democracy?",
        "options": ["1989", "1990", "1991", "1992"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The People's Movement (Jana Andolan I) of 1990 (2046 BS) ended the Panchayat system and restored multi-party democracy.",
        "reference": "History of Nepal"
    },
    {
        "id": 14,
        "question": "When was the Comprehensive Peace Agreement (CPA) signed in Nepal?",
        "options": ["2005", "2006", "2007", "2008"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The Comprehensive Peace Agreement was signed on November 21, 2006 (Mangsir 5, 2063 BS) between the government and Maoists.",
        "reference": "History of Nepal"
    },
    {
        "id": 15,
        "question": "When was the Republic of Nepal declared?",
        "options": ["May 28, 2008", "April 10, 2008", "January 15, 2007", "December 28, 2007"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "The Federal Democratic Republic of Nepal was declared on May 28, 2008 (Jestha 15, 2065 BS) by the first Constituent Assembly.",
        "reference": "History of Nepal"
    },
    {
        "id": 16,
        "question": "Who is known as the 'Father of the Nation' in Nepal?",
        "options": ["Jung Bahadur Rana", "Prithvi Narayan Shah", "Tribhuvan Bir Bikram Shah", "BP Koirala"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Prithvi Narayan Shah, who unified Nepal, is regarded as the 'Father of the Nation' (Rashtriya Pita).",
        "reference": "History of Nepal"
    },
    {
        "id": 17,
        "question": "When did Nepal become a member of the United Nations?",
        "options": ["1945", "1950", "1955", "1960"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Nepal became a member of the United Nations on December 14, 1955.",
        "reference": "International Relations"
    },
    {
        "id": 18,
        "question": "Which treaty opened Nepal to foreign trade in 1923?",
        "options": ["Sugauli Treaty", "Treaty of Peace and Friendship", "Nepal-Britain Treaty of 1923", "Tripartite Agreement"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The Nepal-Britain Treaty of 1923 recognized Nepal as an independent and sovereign nation and opened trade.",
        "reference": "History of Nepal"
    },
    {
        "id": 19,
        "question": "When was the first election held in Nepal?",
        "options": ["1950", "1958", "1959", "1960"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The first general election in Nepal was held in 1959 (2015 BS), in which the Nepali Congress won a majority.",
        "reference": "History of Nepal"
    },
    {
        "id": 20,
        "question": "When was the Kot Massacre (Kot Parva) that established Rana rule?",
        "options": ["1844", "1845", "1846", "1847"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The Kot Massacre occurred on September 14, 1846, after which Jung Bahadur Rana established the Rana oligarchy.",
        "reference": "History of Nepal"
    },
    # Nepal Politics & Current Affairs
    {
        "id": 21,
        "question": "How many provinces were established under the new Constitution of Nepal?",
        "options": ["Five", "Six", "Seven", "Eight"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The Constitution of Nepal 2015 established seven provinces for federal governance.",
        "reference": "Constitution of Nepal"
    },
    {
        "id": 22,
        "question": "What is the name of Province No. 1 after it was renamed?",
        "options": ["Bagmati", "Lumbini", "Koshi", "Gandaki"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Province No. 1 was officially renamed as Koshi Province (Koshi Pradesh) in 2023.",
        "reference": "Provinces of Nepal"
    },
    {
        "id": 23,
        "question": "What is the name of Province No. 5 after it was renamed?",
        "options": ["Madhesh", "Lumbini", "Karnali", "Gandaki"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Province No. 5 was officially renamed as Lumbini Province (Lumbini Pradesh) in 2020.",
        "reference": "Provinces of Nepal"
    },
    {
        "id": 24,
        "question": "Which is the capital city of Gandaki Province?",
        "options": ["Butwal", "Pokhara", "Damauli", "Baglung"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "Pokhara is the capital city of Gandaki Province, designated in 2020.",
        "reference": "Provinces of Nepal"
    },
    {
        "id": 25,
        "question": "Which is the capital city of Sudurpashchim Province?",
        "options": ["Dipayal", "Mahendranagar", "Godawari", "Dhangadhi"],
        "correctIndex": 3,
        "subject": "GK",
        "explanation": "Dhangadhi is the capital city of Sudurpashchim Province, designated in 2019.",
        "reference": "Provinces of Nepal"
    },
    {
        "id": 26,
        "question": "When was the last census conducted in Nepal?",
        "options": ["2068 BS (2011)", "2078 BS (2021)", "2081 BS (2024)", "2075 BS (2018)"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The last National Population and Housing Census was conducted in 2078 BS (2021 AD), recording approximately 29.19 million population.",
        "reference": "Central Bureau of Statistics, Nepal"
    },
    {
        "id": 27,
        "question": "What is the population of Nepal according to the 2021 census?",
        "options": ["26.49 million", "27.49 million", "28.19 million", "29.19 million"],
        "correctIndex": 3,
        "subject": "GK",
        "explanation": "According to the 2021 census, Nepal's population is approximately 29.19 million.",
        "reference": "Central Bureau of Statistics, Nepal"
    },
    {
        "id": 28,
        "question": "Which is the most populous district in Nepal?",
        "options": ["Kathmandu", "Morang", "Rupandehi", "Jhapa"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "Kathmandu district is the most populous district in Nepal with over 2 million people according to the 2021 census.",
        "reference": "Central Bureau of Statistics, Nepal"
    },
    {
        "id": 29,
        "question": "Which is the least populous district in Nepal?",
        "options": ["Manang", "Dolpa", "Mustang", "Humla"],
        "correctIndex": 0,
        "subject": "GK",
        "explanation": "Manang district is the least populous district in Nepal with approximately 5,600 people.",
        "reference": "Central Bureau of Statistics, Nepal"
    },
    {
        "id": 30,
        "question": "What is the literacy rate of Nepal according to the 2021 census?",
        "options": ["65.9%", "71.2%", "76.3%", "81.5%"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The literacy rate of Nepal is approximately 76.3% according to the 2021 census.",
        "reference": "Central Bureau of Statistics, Nepal"
    },
    # International Affairs & Organizations
    {
        "id": 31,
        "question": "Where is the headquarters of SAARC located?",
        "options": ["New Delhi", "Dhaka", "Islamabad", "Kathmandu"],
        "correctIndex": 3,
        "subject": "GK",
        "explanation": "The headquarters of SAARC (South Asian Association for Regional Cooperation) is located in Kathmandu, Nepal.",
        "reference": "SAARC"
    },
    {
        "id": 32,
        "question": "How many member states are there in SAARC?",
        "options": ["Six", "Seven", "Eight", "Nine"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "SAARC has eight member states: Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, and Sri Lanka.",
        "reference": "SAARC"
    },
    {
        "id": 33,
        "question": "Where is the headquarters of the United Nations located?",
        "options": ["Geneva", "New York", "Vienna", "Paris"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The headquarters of the United Nations is located in New York City, USA.",
        "reference": "United Nations"
    },
    {
        "id": 34,
        "question": "How many permanent members are there in the UN Security Council?",
        "options": ["Three", "Four", "Five", "Six"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The UN Security Council has five permanent members: USA, UK, France, Russia, and China.",
        "reference": "United Nations"
    },
    {
        "id": 35,
        "question": "Which country is NOT a member of BIMSTEC?",
        "options": ["Thailand", "Myanmar", "China", "Bhutan"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "BIMSTEC members are Bangladesh, India, Myanmar, Sri Lanka, Thailand, Bhutan, and Nepal. China is not a member.",
        "reference": "BIMSTEC"
    },
    {
        "id": 36,
        "question": "When was the United Nations established?",
        "options": ["1944", "1945", "1946", "1947"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The United Nations was established on October 24, 1945, after World War II.",
        "reference": "United Nations"
    },
    {
        "id": 37,
        "question": "Which is the largest continent in the world by area?",
        "options": ["Africa", "North America", "Asia", "Europe"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Asia is the largest continent, covering approximately 44.58 million square kilometers.",
        "reference": "World Geography"
    },
    {
        "id": 38,
        "question": "Which is the smallest country in the world by area?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "Vatican City (Holy See) is the smallest country in the world, covering only 0.44 sq km.",
        "reference": "World Geography"
    },
    {
        "id": 39,
        "question": "Which river is the longest in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "correctIndex": 1,
        "subject": "GK",
        "explanation": "The Nile River is traditionally considered the longest river at approximately 6,650 km, though the Amazon is close.",
        "reference": "World Geography"
    },
    {
        "id": 40,
        "question": "Which ocean is the largest by area?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "correctIndex": 2,
        "subject": "GK",
        "explanation": "The Pacific Ocean is the largest ocean, covering about 165.25 million square kilometers.",
        "reference": "World Geography"
    },
    # Science, Technology & Misc
    {
        "id": 41,
        "question": "What is the chemical formula of water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "correctIndex": 1,
        "subject": "SCIENCE",
        "explanation": "Water is composed of two hydrogen atoms and one oxygen atom, with the chemical formula H2O.",
        "reference": "Chemistry"
    },
    {
        "id": 42,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "Mars is called the Red Planet due to iron oxide (rust) on its surface, which gives it a reddish appearance.",
        "reference": "Astronomy"
    },
    {
        "id": 43,
        "question": "What is the speed of light in vacuum?",
        "options": ["3,00,000 km/s", "3,00,000 m/s", "1,50,000 km/s", "3,00,00,000 km/s"],
        "correctIndex": 0,
        "subject": "SCIENCE",
        "explanation": "The speed of light in vacuum is approximately 299,792 km/s, commonly rounded to 3,00,000 km/s.",
        "reference": "Physics"
    },
    {
        "id": 44,
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "Nitrogen makes up about 78% of Earth's atmosphere, followed by oxygen at about 21%.",
        "reference": "Earth Science"
    },
    {
        "id": 45,
        "question": "What is the SI unit of electric current?",
        "options": ["Volt", "Watt", "Ampere", "Ohm"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "The SI unit of electric current is the Ampere (A), named after André-Marie Ampère.",
        "reference": "Physics"
    },
    {
        "id": 46,
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"],
        "correctIndex": 1,
        "subject": "SCIENCE",
        "explanation": "Alexander Graham Bell is credited with inventing the telephone in 1876.",
        "reference": "History of Science"
    },
    {
        "id": 47,
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Iron", "Gold", "Diamond", "Platinum"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "Diamond is the hardest known natural material, rated 10 on the Mohs scale of mineral hardness.",
        "reference": "Geology"
    },
    {
        "id": 48,
        "question": "Which vitamin is produced when the skin is exposed to sunlight?",
        "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "Vitamin D is synthesized in the skin when exposed to ultraviolet B (UVB) radiation from sunlight.",
        "reference": "Biology"
    },
    {
        "id": 49,
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Brain", "Skin", "Heart"],
        "correctIndex": 2,
        "subject": "SCIENCE",
        "explanation": "The skin is the largest organ of the human body, with a total area of about 20 square feet in adults.",
        "reference": "Human Anatomy"
    },
    {
        "id": 50,
        "question": "Which blood group is known as the universal donor?",
        "options": ["A+", "B+", "AB+", "O-"],
        "correctIndex": 3,
        "subject": "SCIENCE",
        "explanation": "O negative (O-) is the universal donor because it lacks A, B, and Rh(D) antigens, making it compatible with all blood types.",
        "reference": "Biology"
    }
]

QUESTIONS_NE = [
    # Nepal Geography
    {"id": 1, "question": "नेपालको कुल क्षेत्रफल कति हो?", "options": ["१,४७,१८१ वर्ग कि.मी.", "१,४८,१८१ वर्ग कि.मी.", "१,४६,१८१ वर्ग कि.मी.", "१,४५,१८१ वर्ग कि.मी."], "correctIndex": 0, "subject": "GK", "explanation": "नेपालको कुल क्षेत्रफल १,४७,१८१ वर्ग किलोमिटर (५६,८२७ वर्ग माइल) हो।", "reference": "नेपालको भूगोल"},
    {"id": 2, "question": "नेपालको सबैभन्दा लामो नदी कुन हो?", "options": ["कर्णाली", "कोशी", "गण्डकी", "नारायणी"], "correctIndex": 0, "subject": "GK", "explanation": "कर्णाली नदी नेपालको सबैभन्दा लामो नदी हो, जसको कुल लम्बाइ लगभग १,०८० किलोमिटर छ।", "reference": "नेपालको भूगोल"},
    {"id": 3, "question": "नेपालको सबैभन्दा अग्लो शिखर कुन हो?", "options": ["कञ्चनजङ्घा", "ल्होत्से", "मकालु", "सगरमाथा"], "correctIndex": 3, "subject": "GK", "explanation": "सगरमाथा (माउन्ट एभरेस्ट) ८,८४८.८६ मिटर अग्लो र नेपाल र विश्वको सबैभन्दा अग्लो शिखर हो।", "reference": "नेपालको भूगोल"},
    {"id": 4, "question": "नेपालको सबैभन्दा ठूलो ताल कुन हो?", "options": ["फेवा ताल", "रारा ताल", "तिलिचो ताल", "बेगनास ताल"], "correctIndex": 1, "subject": "GK", "explanation": "मुगु जिल्लामा रहेको रारा ताल नेपालको सबैभन्दा ठूलो ताल हो, जसको क्षेत्रफल लगभग १०.८ वर्ग कि.मी. र समुद्र सतहभन्दा २,९९० मिटर उचाइमा छ।", "reference": "नेपालको भूगोल"},
    {"id": 5, "question": "नेपालको कुन राष्ट्रिय निकुञज युनेस्को विश्व सम्पदा सूचीमा परेको छ?", "options": ["शिवपुरी नागार्जुन", "चितवन राष्ट्रिय निकुञज", "सगरमाथा राष्ट्रिय निकुञज", "चितवन र सगरमाथा दुवै"], "correctIndex": 3, "subject": "GK", "explanation": "चितवन राष्ट्रिय निकुञज (१९८४) र सगरमाथा राष्ट्रिय निकुञज (१९७९) दुवै युनेस्को विश्व सम्पदा सूचीमा परेका छन्।", "reference": "नेपालका विश्व सम्पदा स्थलहरू"},
    {"id": 6, "question": "नेपालको सबैभन्दा होचो स्थान (समुद्र सतहबाट) कुन हो?", "options": ["पोखरा", "वीरगञ्ज", "केचना कालान (झापा)", "भैरहवा"], "correctIndex": 2, "subject": "GK", "explanation": "झापा जिल्लाको केचना कालान नेपालको सबैभन्दा होचो स्थान हो, जुन समुद्र सतहबाट लगभग ५९ मिटर माथि छ।", "reference": "नेपालको भूगोल"},
    {"id": 7, "question": "हाल नेपालमा कति वटा जिल्ला छन्?", "options": ["७५", "७७", "७९", "८१"], "correctIndex": 1, "subject": "GK", "explanation": "संघीय पुनर्संरचनापछि नेपालमा हाल ७७ वटा जिल्लाहरू छन्।", "reference": "नेपालको प्रशासनिक विभाजन"},
    {"id": 8, "question": "नेपालको सबैभन्दा गहिरो खोंच कुन हो?", "options": ["कालीगण्डकी खोंच", "मर्स्याङ्दी खोंच", "त्रिशूली खोंच", "अरुण खोंच"], "correctIndex": 0, "subject": "GK", "explanation": "कालीगण्डकी खोंच (अन्धा गल्छी) विश्वकै सबैभन्दा गहिरो खोंचमध्ये एक हो, जुन अन्नपूर्ण र धौलागिरी हिमशिखरबीचमा छ।", "reference": "नेपालको भूगोल"},
    {"id": 9, "question": "नेपालको कुन क्षेत्रमा सबैभन्दा बढी वर्षा हुन्छ?", "options": ["काठमाडौं उपत्यका", "पोखरा", "पाँचथर", "विराटनगर"], "correctIndex": 2, "subject": "GK", "explanation": "कोशी प्रदेशको पाँचथर जिल्लामा नेपालको सबैभन्दा बढी वर्षा हुन्छ, केही क्षेत्रमा वार्षिक ५,००० मि.मी. भन्दा बढी।", "reference": "नेपालको जलवायु"},
    {"id": 10, "question": "क्षेत्रफलको हिसाबले नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज कुन हो?", "options": ["चितवन राष्ट्रिय निकुञज", "सगरमाथा राष्ट्रिय निकुञज", "शे-फोक्सुन्डो राष्ट्रिय निकुञज", "बर्दिया राष्ट्रिय निकुञज"], "correctIndex": 2, "subject": "GK", "explanation": "डोल्पा जिल्लामा रहेको शे-फोक्सुन्डो राष्ट्रिय निकुञज नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञज हो, जसको क्षेत्रफल ३,५५५ वर्ग कि.मी. छ।", "reference": "नेपालका राष्ट्रिय निकुञजहरू"},
    # Nepal History
    {"id": 11, "question": "पृथ्वीनारायण शाहले नेपालको एकीकरण कहिले पूरा गर्नुभएको थियो?", "options": ["१७६८", "१७६९", "१७७०", "१७७१"], "correctIndex": 1, "subject": "GK", "explanation": "पृथ्वीनारायण शाहले १७६९ मा (१८२६ सालमा) काठमाडौं उपत्यका कब्जा गरी नेपालको एकीकरण पूरा गर्नुभएको थियो।", "reference": "नेपालको इतिहास"},
    {"id": 12, "question": "नेपाल र बेलायतबीच सुगौली सन्धि कहिले भएको थियो?", "options": ["१८१४", "१८१५", "१८१६", "१८१७"], "correctIndex": 2, "subject": "GK", "explanation": "सुगौली सन्धि १८१६ मार्च ४ मा अंग्रेज-नेपाल युद्ध (१८१४-१८१६) पछि भएको थियो।", "reference": "नेपालको इतिहास"},
    {"id": 13, "question": "बहुदलिय प्रजातन्त्र पुनर्स्थापनाको लागि भएको जनआन्दोलन (२०४६) कहिले भएको थियो?", "options": ["१९८९", "१९९०", "१९९१", "१९९२"], "correctIndex": 1, "subject": "GK", "explanation": "जनआन्दोलन (२०४६) १९९० मा भएको थियो, जसले पञ्चायत प्रणालीको अन्त्य र बहुदलिय प्रजातन्त्रको पुनर्स्थापना गर्‍यो।", "reference": "नेपालको इतिहास"},
    {"id": 14, "question": "व्यापक शान्ति सम्झौता (CPA) नेपालमा कहिले भएको थियो?", "options": ["२००५", "२००६", "२००७", "२००८"], "correctIndex": 1, "subject": "GK", "explanation": "व्यापक शान्ति सम्झौता २१ नोभेम्बर २००६ (मंसिर ५, २०६३) मा सरकार र माओवादीबीच भएको थियो।", "reference": "नेपालको इतिहास"},
    {"id": 15, "question": "नेपालमा गणतन्त्र कहिले घोषणा भएको थियो?", "options": ["२००८ मे २८", "२००८ अप्रिल १०", "२००७ जनवरी १५", "२००७ डिसेम्बर २८"], "correctIndex": 0, "subject": "GK", "explanation": "संघीय लोकतान्त्रिक गणतन्त्र नेपाल २८ मे २००८ (जेठ १५, २०६५) मा पहिलो संविधानसभाले घोषणा गरेको थियो।", "reference": "नेपालको इतिहास"},
    {"id": 16, "question": "नेपालमा 'राष्ट्रिय पिता' को रूपमा कसलाई चिनिन्छ?", "options": ["जंगबहादुर राणा", "पृथ्वीनारायण शाह", "त्रिभुवन वीर विक्रम शाह", "वी.पी. कोइराला"], "correctIndex": 1, "subject": "GK", "explanation": "नेपाल एकीकरण गर्ने पृथ्वीनारायण शाहलाई 'राष्ट्रिय पिता' को रूपमा सम्मान गरिन्छ।", "reference": "नेपालको इतिहास"},
    {"id": 17, "question": "नेपाल संयुक्त राष्ट्रसंघको सदस्य कहिले बनेको थियो?", "options": ["१९४५", "१९५०", "१९५५", "१९६०"], "correctIndex": 2, "subject": "GK", "explanation": "नेपाल १४ डिसेम्बर १९५५ मा संयुक्त राष्ट्रसंघको सदस्य बनेको थियो।", "reference": "अन्तर्राष्ट्रिय सम्बन्ध"},
    {"id": 18, "question": "नेपाललाई विदेश व्यापारका लागि खुला गर्ने १९२३ को सन्धि कुन हो?", "options": ["सुगौली सन्धि", "शान्ति तथा मैत्री सन्धि", "नेपाल-बेलायत सन्धि १९२३", "त्रिपक्षीय सम्झौता"], "correctIndex": 2, "subject": "GK", "explanation": "नेपाल-बेलायत सन्धि १९२३ ले नेपाललाई स्वतन्त्र र सार्वभौम राष्ट्रको रूपमा मान्यता दिएर व्यापार खुला गर्‍यो।", "reference": "नेपालको इतिहास"},
    {"id": 19, "question": "नेपालमा पहिलो आम निर्वाचन कहिले भएको थियो?", "options": ["१९५०", "१९५८", "१९५९", "१९६०"], "correctIndex": 2, "subject": "GK", "explanation": "नेपालको पहिलो आम निर्वाचन १९५९ (२०१५ साल) मा भएको थियो, जसमा नेपाली कांग्रेसले बहुमत प्राप्त गरेको थियो।", "reference": "नेपालको इतिहास"},
    {"id": 20, "question": "कोत पर्व जसले राणा शासन स्थापना गर्‍यो, कहिले भएको थियो?", "options": ["१८४४", "१८४५", "१८४६", "१८४७"], "correctIndex": 2, "subject": "GK", "explanation": "कोत पर्व १४ सेप्टेम्बर १८४६ मा भएको थियो, जसपछि जंगबहादुर राणाले राणा ओलिगार्की स्थापना गर्नुभएको थियो।", "reference": "नेपालको इतिहास"},
    # Nepal Politics & Current Affairs
    {"id": 21, "question": "नयाँ संविधान अनुसार नेपालमा कति वटा प्रदेश स्थापना गरिएका छन्?", "options": ["पाँच", "छ", "सात", "आठ"], "correctIndex": 2, "subject": "GK", "explanation": "नेपालको संविधान २०७२ ले संघीय शासन व्यवस्थाका लागि सात वटा प्रदेशको व्यवस्था गरेको छ।", "reference": "नेपालको संविधान"},
    {"id": 22, "question": "प्रदेश नं. १ को नयाँ नाम के राखिएको छ?", "options": ["बागमती", "लुम्बिनी", "कोशी", "गण्डकी"], "correctIndex": 2, "subject": "GK", "explanation": "प्रदेश नं. १ लाई २०२३ मा कोशी प्रदेशको रूपमा नामाकरण गरिएको छ।", "reference": "नेपालका प्रदेशहरू"},
    {"id": 23, "question": "प्रदेश नं. ५ को नयाँ नाम के राखिएको छ?", "options": ["मधेश", "लुम्बिनी", "कर्णाली", "गण्डकी"], "correctIndex": 1, "subject": "GK", "explanation": "प्रदेश नं. ५ लाई २०२० मा लुम्बिनी प्रदेशको रूपमा नामाकरण गरिएको छ।", "reference": "नेपालका प्रदेशहरू"},
    {"id": 24, "question": "गण्डकी प्रदेशको राजधानी कुन सहर हो?", "options": ["बुटवल", "पोखरा", "दमौली", "बागलुङ"], "correctIndex": 1, "subject": "GK", "explanation": "पोखरालाई २०२० मा गण्डकी प्रदेशको राजधानी तोकिएको छ।", "reference": "नेपालका प्रदेशहरू"},
    {"id": 25, "question": "सुदूरपश्चिम प्रदेशको राजधानी कुन सहर हो?", "options": ["दिपायल", "महेन्द्रनगर", "गोदावरी", "धनगढी"], "correctIndex": 3, "subject": "GK", "explanation": "धनगढीलाई २०१९ मा सुदूरपश्चिम प्रदेशको राजधानी तोकिएको छ।", "reference": "नेपालका प्रदेशहरू"},
    {"id": 26, "question": "नेपालमा पछिल्लो राष्ट्रिय जनगणना कहिले भएको थियो?", "options": ["२०६८ (२०११)", "२०७८ (२०२१)", "२०८१ (२०२४)", "२०७५ (२०१८)"], "correctIndex": 1, "subject": "GK", "explanation": "पछिल्लो राष्ट्रिय जनगणना २०७८ साल (२०२१ ई.) मा भएको थियो, जसमा नेपालको जनसंख्या लगभग २९.१९ मिलियन रेकर्ड गरिएको थियो।", "reference": "केन्द्रीय तथ्यांक विभाग, नेपाल"},
    {"id": 27, "question": "२०२१ को जनगणना अनुसार नेपालको जनसंख्या कति छ?", "options": ["२६.४९ मिलियन", "२७.४९ मिलियन", "२८.१९ मिलियन", "२९.१९ मिलियन"], "correctIndex": 3, "subject": "GK", "explanation": "२०२१ को जनगणना अनुसार नेपालको जनसंख्या लगभग २९.१९ मिलियन छ।", "reference": "केन्द्रीय तथ्यांक विभाग, नेपाल"},
    {"id": 28, "question": "नेपालको सबैभन्दा बढी जनसंख्या भएको जिल्ला कुन हो?", "options": ["काठमाडौं", "मोरङ", "रुपन्देही", "झापा"], "correctIndex": 0, "subject": "GK", "explanation": "काठमाडौं जिल्ला नेपालको सबैभन्दा बढी जनसंख्या भएको जिल्ला हो, जसमा २०२१ को जनगणनाअनुसार २ मिलियन भन्दा बढी जनसंख्या छ।", "reference": "केन्द्रीय तथ्यांक विभाग, नेपाल"},
    {"id": 29, "question": "नेपालको सबैभन्दा कम जनसंख्या भएको जिल्ला कुन हो?", "options": ["मनाङ", "डोल्पा", "मुस्ताङ", "हुम्ला"], "correctIndex": 0, "subject": "GK", "explanation": "मनाङ जिल्ला नेपालको सबैभन्दा कम जनसंख्या भएको जिल्ला हो, जसमा लगभग ५,६०० मात्र जनसंख्या छ।", "reference": "केन्द्रीय तथ्यांक विभाग, नेपाल"},
    {"id": 30, "question": "२०२१ को जनगणना अनुसार नेपालको साक्षरता दर कति छ?", "options": ["६५.९%", "७१.२%", "७६.३%", "८१.५%"], "correctIndex": 2, "subject": "GK", "explanation": "२०२१ को जनगणना अनुसार नेपालको साक्षरता दर लगभग ७६.३% छ।", "reference": "केन्द्रीय तथ्यांक विभाग, नेपाल"},
    # International Affairs
    {"id": 31, "question": "सार्क (SAARC) को मुख्यालय कहाँ छ?", "options": ["नयाँ दिल्ली", "ढाका", "इस्लामाबाद", "काठमाडौं"], "correctIndex": 3, "subject": "GK", "explanation": "दक्षिण एशियाली क्षेत्रीय सहयोग सङ्गठन (सार्क) को मुख्यालय काठमाडौं, नेपालमा छ।", "reference": "सार्क"},
    {"id": 32, "question": "सार्कमा कति वटा सदस्य राष्ट्रहरू छन्?", "options": ["छ", "सात", "आठ", "नौ"], "correctIndex": 2, "subject": "GK", "explanation": "सार्कमा आठ वटा सदस्य राष्ट्रहरू छन्: अफगानिस्तान, बंगलादेश, भूटान, भारत, माल्दिभ्स, नेपाल, पाकिस्तान र श्रीलंका।", "reference": "सार्क"},
    {"id": 33, "question": "संयुक्त राष्ट्रसंघको मुख्यालय कहाँ छ?", "options": ["जeneva", "न्यूयोर्क", "भियना", "पेरिस"], "correctIndex": 1, "subject": "GK", "explanation": "संयुक्त राष्ट्रसंघको मुख्यालय अमेरिकाको न्यूयोर्क शहरमा छ।", "reference": "संयुक्त राष्ट्रसंघ"},
    {"id": 34, "question": "संयुक्त राष्ट्रसंघको सुरक्षा परिषद्मा कति वटा स्थायी सदस्यहरू छन्?", "options": ["तीन", "चार", "पाँच", "छ"], "correctIndex": 2, "subject": "GK", "explanation": "संयुक्त राष्ट्रसंघको सुरक्षा परिषद्मा पाँच वटा स्थायी सदस्यहरू छन्: अमेरिका, बेलायत, फ्रान्स, रुस र चीन।", "reference": "संयुक्त राष्ट्रसंघ"},
    {"id": 35, "question": "निम्नमध्ये कुन देश बिम्सटेक (BIMSTEC) को सदस्य होइन?", "options": ["थाइल्याण्ड", "म्यानमार", "चीन", "भूटान"], "correctIndex": 2, "subject": "GK", "explanation": "बिम्सटेकका सदस्यहरू: बंगलादेश, भारत, म्यानमार, श्रीलंका, थाइल्याण्ड, भूटान र नेपाल। चीन सदस्य होइन।", "reference": "बिम्सटेक"},
    {"id": 36, "question": "संयुक्त राष्ट्रसंघ कहिले स्थापना भएको थियो?", "options": ["१९४४", "१९४५", "१९४६", "१९४७"], "correctIndex": 1, "subject": "GK", "explanation": "दोस्रो विश्वयुद्धपछि संयुक्त राष्ट्रसंघ २४ अक्टोबर १९४५ मा स्थापना भएको थियो।", "reference": "संयुक्त राष्ट्रसंघ"},
    {"id": 37, "question": "क्षेत्रफलको हिसाबले विश्वको सबैभन्दा ठूलो महादेश कुन हो?", "options": ["अफ्रिका", "उत्तर अमेरिका", "एशिया", "युरोप"], "correctIndex": 2, "subject": "GK", "explanation": "एशिया विश्वको सबैभन्दा ठूलो महादेश हो, जसको क्षेत्रफल लगभग ४४.५८ मिलियन वर्ग कि.मी. छ।", "reference": "विश्व भूगोल"},
    {"id": 38, "question": "क्षेत्रफलको हिसाबले विश्वको सबैभन्दा सानो देश कुन हो?", "options": ["मोनाको", "नाउरू", "भ्याटिकन सिटी", "सान मारिनो"], "correctIndex": 2, "subject": "GK", "explanation": "भ्याटिकन सिटी विश्वको सबैभन्दा सानो देश हो, जसको क्षेत्रफल मात्र ०.४४ वर्ग कि.मी. छ।", "reference": "विश्व भूगोल"},
    {"id": 39, "question": "विश्वको सबैभन्दा लामो नदी कुन हो?", "options": ["एमेजन", "नाइल", "याङ्त्जे", "मिसिसिपी"], "correctIndex": 1, "subject": "GK", "explanation": "नाइल नदी परम्परागत रूपमा विश्वको सबैभन्दा लामो नदी मानिन्छ, जसको लम्बाइ लगभग ६,६५० कि.मी. छ।", "reference": "विश्व भूगोल"},
    {"id": 40, "question": "क्षेत्रफलको हिसाबले विश्वको सबैभन्दा ठूलो महासागर कुन हो?", "options": ["अटलान्टिक महासागर", "हिन्द महासागर", "प्रशान्त महासागर", "आर्कटिक महासागर"], "correctIndex": 2, "subject": "GK", "explanation": "प्रशान्त महासागर विश्वको सबैभन्दा ठूलो महासागर हो, जसको क्षेत्रफल लगभग १६५.२५ मिलियन वर्ग कि.मी. छ।", "reference": "विश्व भूगोल"},
    # Science & Technology
    {"id": 41, "question": "पानीको रासायनिक सूत्र के हो?", "options": ["CO2", "H2O", "O2", "NaCl"], "correctIndex": 1, "subject": "SCIENCE", "explanation": "पानी दुई हाइड्रोजन र एक अक्सिजन परमाणुको बनेको हुन्छ, जसको रासायनिक सूत्र H2O हो।", "reference": "रसायनशास्त्र"},
    {"id": 42, "question": "कुन ग्रहलाई 'रातो ग्रह' को रूपमा चिनिन्छ?", "options": ["शुक्र", "बृहस्पति", "मंगल", "शनि"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "मंगल ग्रहलाई रातो ग्रह भनिन्छ किनभने यसको सतहमा रहेको फलामको अक्साइड (जङ्ग) ले यसलाई रातो देखाउँछ।", "reference": "खगोलशास्त्र"},
    {"id": 43, "question": "खाली स्थानमा प्रकाशको गति कति हुन्छ?", "options": ["३,००,००० कि.मी./से", "३,००,००० मि./से", "१,५०,००० कि.मी./से", "३,००,००,००० कि.मी./से"], "correctIndex": 0, "subject": "SCIENCE", "explanation": "खाली स्थानमा प्रकाशको गति लगभग २,९९,७९२ कि.मी./से हुन्छ, जसलाई सामान्यतया ३,००,००० कि.मी./से भनिन्छ।", "reference": "भौतिकशास्त्र"},
    {"id": 44, "question": "पृथ्वीको वायुमण्डलमा सबैभन्दा बढी मात्रामा कुन ग्यास छ?", "options": ["अक्सिजन", "कार्बन डाइअक्साइड", "नाइट्रोजन", "हाइड्रोजन"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "नाइट्रोजन पृथ्वीको वायुमण्डलको लगभग ७८% ओगट्छ, अक्सिजन लगभग २१% मा दोस्रो स्थानमा छ।", "reference": "पृथ्वी विज्ञान"},
    {"id": 45, "question": "विद्युत धाराको SI एकाइ के हो?", "options": ["भोल्ट", "वाट", "एम्पियर", "ओम"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "विद्युत धाराको SI एकाइ एम्पियर (A) हो, जुन आन्द्रे-मेरी एम्पियरको नामबाट नामाकरण गरिएको हो।", "reference": "भौतिकशास्त्र"},
    {"id": 46, "question": "टेलिफोनको आविष्कार कसले गरेका थिए?", "options": ["थोमस एडिसन", "अलेक्जेन्डर ग्राहम बेल", "निकोला टेस्ला", "गुग्लिएल्मो मार्कोनी"], "correctIndex": 1, "subject": "SCIENCE", "explanation": "अलेक्जेन्डर ग्राहम बेललाई १८७६ मा टेलिफोनको आविष्कारको श्रेय दिइन्छ।", "reference": "विज्ञानको इतिहास"},
    {"id": 47, "question": "पृथ्वीमा पाइने सबैभन्दा कठोर प्राकृतिक पदार्थ कुन हो?", "options": ["फलाम", "सुन", "हीरा", "प्लatinum"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "हीरा पृथ्वीमा पाइने सबैभन्दा कठोर प्राकृतिक पदार्थ हो, जुन मोह्स स्केलमा १० मा मापन गरिन्छ।", "reference": "भूविज्ञान"},
    {"id": 48, "question": "छालामा सूर्यको प्रकाश परेमा कुन भिटामिन उत्पादन हुन्छ?", "options": ["भिटामिन A", "भिटामिन C", "भिटामिन D", "भिटामिन E"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "छालामा सूर्यको अल्ट्राभायलेट B (UVB) विकिरण परेमा भिटामिन D संश्लेषित हुन्छ।", "reference": "जीवविज्ञान"},
    {"id": 49, "question": "मानव शरीरको सबैभन्दा ठूलो अंग कुन हो?", "options": ["कलेजो", "दिमाग", "छाला", "मुटु"], "correctIndex": 2, "subject": "SCIENCE", "explanation": "छाला मानव शरीरको सबैभन्दा ठूलो अंग हो, वयस्कमा यसको कुल क्षेत्रफल लगभग २० वर्ग फिट हुन्छ।", "reference": "मानव शरीर विज्ञान"},
    {"id": 50, "question": "कुन रक्त समूहलाई विश्वव्यापी दाता (universal donor) भनिन्छ?", "options": ["A+", "B+", "AB+", "O-"], "correctIndex": 3, "subject": "SCIENCE", "explanation": "O नेगेटिभ (O-) लाई विश्वव्यापी दाता भनिन्छ किनभने यसमा A, B र Rh(D) एन्टिजेन हुँदैन, जसले गर्दा यो सबै रक्त समूहसँग मिल्छ।", "reference": "जीवविज्ञान"}
]


def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    
    set1_en = {
        "setId": "gk-set1",
        "title": "Set 1: General Knowledge",
        "description": "50 questions covering Nepal geography, history, politics, international affairs, and science.",
        "category": "gk",
        "locked": False,
        "timeLimit": 1800,
        "passingScore": 60,
        "questions": QUESTIONS_EN
    }
    
    set1_ne = {
        "setId": "gk-set1",
        "title": "सेट १: सामान्य ज्ञान",
        "description": "नेपालको भूगोल, इतिहास, राजनीति, अन्तर्राष्ट्रिय मामिला र विज्ञान सम्बन्धी ५० प्रश्नहरू।",
        "category": "gk",
        "locked": False,
        "timeLimit": 1800,
        "passingScore": 60,
        "questions": QUESTIONS_NE
    }
    
    save_json(set1_en, os.path.join(base, '../data/en/gk/set1.json'))
    save_json(set1_ne, os.path.join(base, '../data/ne/gk/set1.json'))
    
    tests = {
        "category": "gk",
        "sets": [
            {"setId": "gk-set1", "setNumber": 1, "title": {"en": "Set 1: General Knowledge", "ne": "सेट १: सामान्य ज्ञान"}, "description": {"en": "50 questions on GK.", "ne": "सामान्य ज्ञान सम्बन्धी ५० प्रश्नहरू।"}, "locked": False, "passingScore": 60, "timeLimit": 1800},
            {"setId": "gk-set2", "setNumber": 2, "title": {"en": "Set 2: General Knowledge", "ne": "सेट २: सामान्य ज्ञान"}, "description": {"en": "Coming soon.", "ne": "चाँडै आउँदैछ।"}, "locked": True, "passingScore": 60, "timeLimit": 1800},
            {"setId": "gk-set3", "setNumber": 3, "title": {"en": "Set 3: General Knowledge", "ne": "सेट ३: सामान्य ज्ञान"}, "description": {"en": "Coming soon.", "ne": "चाँडै आउँदैछ।"}, "locked": True, "passingScore": 60, "timeLimit": 1800}
        ]
    }
    save_json(tests, os.path.join(base, '../data/en/gk/tests.json'))
    save_json(tests, os.path.join(base, '../data/ne/gk/tests.json'))
    
    print("GK category generated successfully!")
    print(f"Total questions: {len(QUESTIONS_EN)}")


if __name__ == '__main__':
    main()
