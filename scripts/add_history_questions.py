import json, re, os

# The 10 World History questions from the transcript
HISTORY_QUESTIONS = [
    {
        "q_en": "Which country has the world's shortest constitution?",
        "q_ne": "विश्वको सबैभन्दा छोटो संविधान भएको मुलुक कुन हो?",
        "options_en": ["America", "Britain", "India", "China"],
        "options_ne": ["अमेरिका", "बेलायत", "भारत", "चीन"],
        "correct": 0,
        "explanation_en": "America has the world's shortest constitution with only 7 articles. Article 1 = Legislature, Article 7 = Ratification.",
        "explanation_ne": "अमेरिकामा विश्वको सबैभन्दा छोटो संविधान छ जसमा मात्र ७ वटा धारा छन्। धारा १ = विधायिका, धारा ७ = अनुमोदन।",
        "subject": "GK"
    },
    {
        "q_en": "Who was the King of Britain during the Glorious Revolution?",
        "q_ne": "गौरवमय क्रान्तिका समयमा बेलायतका राजा को थिए?",
        "options_en": ["James II", "Nicholas II", "Charles II", "John II"],
        "options_ne": ["जेम्स द्वितीय", "निकोलस द्वितीय", "चार्ल्स द्वितीय", "जोन द्वितीय"],
        "correct": 0,
        "explanation_en": "James II was the King of Britain during the Glorious Revolution (1688). Nicholas II was the Russian Tsar during the Russian Revolution.",
        "explanation_ne": "गौरवमय क्रान्ति (१६८८) का समयमा बेलायतका राजा जेम्स द्वितीय थिए। निकोलस द्वितीय रुसी राज्य क्रान्तिका बेला रुसका सम्राट थिए।",
        "subject": "GK"
    },
    {
        "q_en": "What was the slogan of the American War of Independence?",
        "q_ne": "अमेरिकी स्वतन्त्रता संग्रामको नारा के थियो?",
        "options_en": ["Unity in Diversity", "Equality, Liberty and Fraternity", "Bread for Survival", "Give me liberty or give me death"],
        "options_ne": ["विविधतामा एकता", "समानता, स्वतन्त्रता र भातृत्व", "बाँच्नका लागि रोटी", "मृत्यु देउ वा स्वतन्त्रता"],
        "correct": 3,
        "explanation_en": "'Give me liberty or give me death' was the slogan. 'Bread for Survival' = Russian Revolution. 'Equality, Liberty, Fraternity' = French Revolution. 'Unity in Diversity' = European Union.",
        "explanation_ne": "'मृत्यु देउ वा स्वतन्त्रता' नारा थियो। 'बाँच्नका लागि रोटी' = रुसी क्रान्ति। 'समानता, स्वतन्त्रता र भातृत्व' = फ्रान्सिली क्रान्ति। 'विविधतामा एकता' = युरोपेली युनियन।",
        "subject": "GK"
    },
    {
        "q_en": "Who was the first President of independent Pakistan?",
        "q_ne": "स्वतन्त्र पाकिस्तानको प्रथम राष्ट्रपति को हुन्?",
        "options_en": ["Muhammad Ali Jinnah", "Rabindranath Tagore", "Liaquat Ali Khan", "Sarvepalli Radhakrishnan"],
        "options_ne": ["मोहम्मद अली जिन्ना", "रवीन्द्रनाथ टेगोर", "लियाकत अली खान", "सर्वपल्ली राधाकृष्ण"],
        "correct": 0,
        "explanation_en": "Muhammad Ali Jinnah was the first President. Rabindranath Tagore gave 'Mahatma' title to Gandhi. Liaquat Ali Khan = first PM of Pakistan. Sarvepalli Radhakrishnan = first Vice President of India.",
        "explanation_ne": "मोहम्मद अली जिन्ना प्रथम राष्ट्रपति हुन्। रवीन्द्रनाथ टेगोरले गान्धीलाई 'महात्मा' उपाधि दिएका हुन्। लियाकत अली खान = पाकिस्तानका प्रथम प्रधानमन्त्री। सर्वपल्ली राधाकृष्ण = भारतका प्रथम उपराष्ट्रपति।",
        "subject": "GK"
    },
    {
        "q_en": "Approximately how many civilians were killed in World War II?",
        "q_ne": "द्वितीय विश्व युद्धमा करिब कति सर्वसाधारण मारिएका थिए?",
        "options_en": ["1 crore", "2 crore", "3 crore", "4 crore"],
        "options_ne": ["१ करोड", "२ करोड", "३ करोड", "४ करोड"],
        "correct": 0,
        "explanation_en": "About 1 crore civilians were killed. Soldiers killed = 1 crore 46 lakh. Total wounded = 3 crore 40 lakh. Total who lost lives = 2 crore 20 lakh. Expenditure = 11,92,000 crore dollars.",
        "explanation_ne": "करिब १ करोड सर्वसाधारण मारिएका थिए। सैनिक मारिएका = १ करोड ४६ लाख। घाइते = ३ करोड ४० लाख। ज्यान गुमाएका = २ करोड २० लाख। खर्च = ११,९२,००० खर्ब डलर।",
        "subject": "GK"
    },
    {
        "q_en": "Which was the first country where an atomic bomb was dropped?",
        "q_ne": "परमाणु बम खसालिएको विश्वको पहिलो मुलुक कुन हो?",
        "options_en": ["China", "France", "Japan", "America"],
        "options_ne": ["चीन", "फ्रान्स", "जापान", "अमेरिका"],
        "correct": 2,
        "explanation_en": "Japan was the first country (Hiroshima). China = first country to start civil service. France = first country to introduce metric system. America = first country to issue a constitution.",
        "explanation_ne": "जापान पहिलो मुलुक हो (हिरोसिमा)। चीन = निजामती सेवा सुरु गर्ने पहिलो देश। फ्रान्स = मेट्रिक प्रणाली प्रचलनमा ल्याउने पहिलो देश। अमेरिका = संविधान जारी गर्ने पहिलो मुलुक।",
        "subject": "GK"
    },
    {
        "q_en": "Which country surrendered first in World War II?",
        "q_ne": "दोस्रो विश्व युद्धमा सबैभन्दा पहिला आत्मसमर्पण गर्ने मुलुक कुन हो?",
        "options_en": ["Germany", "Portugal", "Japan", "Italy"],
        "options_ne": ["जर्मनी", "पोर्चुगल", "जापान", "इटाली"],
        "correct": 3,
        "explanation_en": "Italy surrendered first. Germany was second. Japan surrendered last on August 14, 1945.",
        "explanation_ne": "इटालीले सबैभन्दा पहिला आत्मसमर्पण गर्यो। जर्मनी दोस्रो। जापानले अन्तिममा अगस्ट १४, १९४५ मा आत्मसमर्पण गर्यो।",
        "subject": "GK"
    },
    {
        "q_en": "When did the Sepoy Mutiny occur in India?",
        "q_ne": "भारतमा सैनिक विद्रोह कहिले भयो?",
        "options_en": ["1863", "1804", "1865", "1857"],
        "options_ne": ["सन् १८६३", "सन् १८०४", "सन् १८६५", "सन् १८५७"],
        "correct": 3,
        "explanation_en": "The Sepoy Mutiny (Indian Rebellion) occurred in 1857. 1863 = Abolition of slavery in America. 1865 = Assassination of Abraham Lincoln. 1804 = Napoleon Bonaparte declared Emperor of France (Note: some sources cite 1854 for Vellore Mutiny).",
        "explanation_ne": "भारतमा सैनिक विद्रोह (सिपाही विद्रोह) १८५७ मा भयो। १८६३ = अमेरिकामा दास प्रथा उन्मूलन। १८६५ = अब्राहाम लिङकनको हत्या। १८०४ = नेपोलियन बोनापार्ट फ्रान्सका सम्राट घोषित।",
        "subject": "GK"
    },
    {
        "q_en": "Which revolution is known as the Intellectual Revolution?",
        "q_ne": "बौद्धिक क्रान्ति भनेर कुन क्रान्तिलाई चिनिन्छ?",
        "options_en": ["French Revolution", "Russian Revolution", "Industrial Revolution", "Glorious Revolution of Britain"],
        "options_ne": ["फ्रान्सको राज्य क्रान्ति", "रुसी क्रान्ति", "औद्योगिक क्रान्ति", "बेलायतको गौरवमय क्रान्ति"],
        "correct": 0,
        "explanation_en": "The French Revolution is called the Intellectual Revolution. Russian Revolution = also called October Revolution. Industrial Revolution = also called Mechanical Revolution. Glorious Revolution = also called Bloodless Revolution.",
        "explanation_ne": "फ्रान्सको राज्य क्रान्तिलाई बौद्धिक क्रान्ति भनिन्छ। रुसी क्रान्ति = अक्टोबर क्रान्ति। औद्योगिक क्रान्ति = यान्त्रिक क्रान्ति। गौरवमय क्रान्ति = रक्तहीन क्रान्ति।",
        "subject": "GK"
    },
    {
        "q_en": "Which country did the Industrial Revolution start from?",
        "q_ne": "औद्योगिक क्रान्तिको सुरुवात कुन देशबाट भएको हो?",
        "options_en": ["Germany", "America", "France", "Britain"],
        "options_ne": ["जर्मनी", "अमेरिका", "फ्रान्स", "बेलायत"],
        "correct": 3,
        "explanation_en": "The Industrial Revolution started from Britain.",
        "explanation_ne": "औद्योगिक क्रान्तिको सुरुवात बेलायतबाट भएको हो।",
        "subject": "GK"
    },
]

# Read the existing build script
with open('/Users/kalikali/Desktop/crack-lokshewa/scripts/build_real_questions.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the line with the last question before the closing bracket of ALL_QUESTIONS
# We need to add these questions before the closing ] of ALL_QUESTIONS

# Find the pattern: the last question dict before ]
last_q_pattern = r'(\{"q_en": "When did the Sepoy Mutiny.*?"subject": "GK"\},)'
# Actually, we need to find where ALL_QUESTIONS ends
# Let's find the line: ]

# Find the position of the closing ] for ALL_QUESTIONS
# It should be after the last question dict
lines = content.split('\n')

# Find the line that starts the ALL_QUESTIONS list
insert_idx = None
for i, line in enumerate(lines):
    if line.strip() == ']':
        # Check if this is the closing of ALL_QUESTIONS (before the empty line and function defs)
        if i > 0 and 'def ' not in lines[i+1] if i+1 < len(lines) else True:
            insert_idx = i
            break

print(f"Found closing bracket at line {insert_idx}")
