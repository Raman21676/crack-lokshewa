#!/usr/bin/env python3
"""Generator for Constitution of Nepal category questions."""
import json
import os
import sys

# English questions
QUESTIONS_EN = [
    # Preamble & Preliminary
    {
        "id": 1,
        "question": "When was the Constitution of Nepal, 2072 (2015) promulgated?",
        "options": ["20 September 2015", "28 May 2008", "15 January 2007", "10 November 2006"],
        "correctIndex": 0,
        "subject": "CONSTITUTION",
        "explanation": "The Constitution of Nepal was promulgated on 20 September 2015 (3 Ashwin 2072) by the Constituent Assembly.",
        "reference": "Constitution of Nepal, Preamble"
    },
    {
        "id": 2,
        "question": "What type of state is Nepal according to Article 4 of the Constitution?",
        "options": ["Federal Democratic Republic", "Federal Democratic Republican", "Socialism-oriented Federal Democratic Republican", "Socialist Federal Republic"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 4 states Nepal is an independent, indivisible, sovereign, secular, inclusive, democratic, socialism-oriented, federal democratic republican state.",
        "reference": "Constitution of Nepal, Article 4"
    },
    {
        "id": 3,
        "question": "What is the official language of Nepal according to Article 7?",
        "options": ["Nepali language in Devanagari script", "Nepali and English", "Nepali, Maithili and Bhojpuri", "All languages spoken as mother tongues"],
        "correctIndex": 0,
        "subject": "CONSTITUTION",
        "explanation": "Article 7(1): The Nepali language in the Devanagari script shall be the official language of Nepal.",
        "reference": "Constitution of Nepal, Article 7"
    },
    {
        "id": 4,
        "question": "Which bird is designated as the national bird of Nepal?",
        "options": ["Eagle", "Danphe (Lophophorus)", "Peacock", "Himalayan Monal"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 9(3) designates the Lophophorus (Danphe) as the national bird of Nepal.",
        "reference": "Constitution of Nepal, Article 9"
    },
    {
        "id": 5,
        "question": "What is the national flower of Nepal according to the Constitution?",
        "options": ["Lotus", "Rhododendron Arboreum (Lali Gurans)", "Sunflower", "Rose"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 9(3) states the Rhododendron Arboreum (Lali Gurans) shall be the national flower of Nepal.",
        "reference": "Constitution of Nepal, Article 9"
    },
    # Citizenship
    {
        "id": 6,
        "question": "According to Article 10, what type of citizenship does Nepal have?",
        "options": ["Dual citizenship", "Single federal citizenship with State identity", "State citizenship only", "Naturalized citizenship for all"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 10(2) provides for single federal citizenship with State identity in Nepal.",
        "reference": "Constitution of Nepal, Article 10"
    },
    {
        "id": 7,
        "question": "Under Article 11, who can acquire citizenship of Nepal by descent?",
        "options": ["Only those whose father is Nepali", "Persons whose father or mother was a citizen of Nepal", "Only naturalized citizens", "Foreigners married to Nepali citizens"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 11(2)(b): A person whose father or mother was a citizen of Nepal at his or her birth shall be the citizen of Nepal by descent.",
        "reference": "Constitution of Nepal, Article 11"
    },
    {
        "id": 8,
        "question": "What is the provision for non-resident Nepalese citizenship according to Article 14?",
        "options": ["Full political rights", "Economic, social and cultural rights only", "No rights granted", "Same as naturalized citizenship"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 14 grants non-resident Nepalese citizenship with rights to enjoy economic, social and cultural rights in accordance with Federal law.",
        "reference": "Constitution of Nepal, Article 14"
    },
    {
        "id": 9,
        "question": "According to Article 12, can citizenship certificate mention mother's name?",
        "options": ["No, only father's name", "Yes, with gender identity by mother's or father's name", "Only in special cases", "Not mentioned in Constitution"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 12 allows a person to obtain citizenship certificate with gender identity by the name of his or her mother or father.",
        "reference": "Constitution of Nepal, Article 12"
    },
    {
        "id": 10,
        "question": "How many years does the State have to make legal provisions for implementation of fundamental rights?",
        "options": ["One year", "Two years", "Three years", "Five years"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 47 requires the State to make legal provisions for implementation of fundamental rights within three years of commencement of the Constitution.",
        "reference": "Constitution of Nepal, Article 47"
    },
    # Fundamental Rights
    {
        "id": 11,
        "question": "Which Article guarantees the right to live with dignity?",
        "options": ["Article 16", "Article 17", "Article 18", "Article 20"],
        "correctIndex": 0,
        "subject": "CONSTITUTION",
        "explanation": "Article 16 guarantees every person's right to live with dignity.",
        "reference": "Constitution of Nepal, Article 16"
    },
    {
        "id": 12,
        "question": "Does the Constitution of Nepal allow death penalty?",
        "options": ["Yes, for serious crimes", "Yes, with President's approval", "No, no law shall provide for death penalty", "Not mentioned"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 16(2) explicitly states: No law shall be made providing for the death penalty to any person.",
        "reference": "Constitution of Nepal, Article 16"
    },
    {
        "id": 13,
        "question": "Within how many hours must an arrested person be produced before the adjudicating authority?",
        "options": ["12 hours", "24 hours", "48 hours", "72 hours"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 20(3): Any person arrested shall be produced before the adjudicating authority within 24 hours, excluding journey time.",
        "reference": "Constitution of Nepal, Article 20"
    },
    {
        "id": 14,
        "question": "Which Article guarantees the right to equality?",
        "options": ["Article 16", "Article 17", "Article 18", "Article 19"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 18 guarantees equality before law and equal protection of law to all citizens.",
        "reference": "Constitution of Nepal, Article 18"
    },
    {
        "id": 15,
        "question": "According to Article 18(5), do daughters have equal right to ancestral property?",
        "options": ["No, only sons", "Yes, equal right without gender discrimination", "Only if unmarried", "Only after father's death"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 18(5): All offspring shall have the equal right to the ancestral property without discrimination on the ground of gender.",
        "reference": "Constitution of Nepal, Article 18"
    },
    {
        "id": 16,
        "question": "Which Article guarantees the right to information?",
        "options": ["Article 25", "Article 26", "Article 27", "Article 28"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 27 guarantees every citizen the right to demand and receive information on any matter of public interest.",
        "reference": "Constitution of Nepal, Article 27"
    },
    {
        "id": 17,
        "question": "Which Article guarantees the right to education?",
        "options": ["Article 29", "Article 30", "Article 31", "Article 32"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 31 guarantees every citizen the right of access to basic education and compulsory free education up to basic level.",
        "reference": "Constitution of Nepal, Article 31"
    },
    {
        "id": 18,
        "question": "According to Article 31(5), do communities have the right to education in their mother tongue?",
        "options": ["No, only Nepali language", "Yes, every Nepalese community has the right", "Only in private schools", "Only up to primary level"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 31(5): Every Nepalese community residing in Nepal shall have the right to get education in its mother tongue.",
        "reference": "Constitution of Nepal, Article 31"
    },
    {
        "id": 19,
        "question": "Which Article guarantees the right to employment?",
        "options": ["Article 32", "Article 33", "Article 34", "Article 35"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 33 guarantees every citizen the right to employment and to choose employment.",
        "reference": "Constitution of Nepal, Article 33"
    },
    {
        "id": 20,
        "question": "Which Article guarantees the right to food sovereignty?",
        "options": ["Article 34", "Article 35", "Article 36", "Article 37"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 36(3) guarantees every citizen the right to food sovereignty in accordance with law.",
        "reference": "Constitution of Nepal, Article 36"
    },
    {
        "id": 21,
        "question": "Which Article prohibits untouchability and discrimination?",
        "options": ["Article 22", "Article 23", "Article 24", "Article 25"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 24 prohibits any form of untouchability or discrimination in any private or public place.",
        "reference": "Constitution of Nepal, Article 24"
    },
    {
        "id": 22,
        "question": "What is the right of a victim of crime according to Article 21?",
        "options": ["Only right to file FIR", "Right to information about investigation and compensation", "Right to punish the accused", "No special rights"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 21 guarantees victims the right to get information about investigation and proceedings, and right to justice including compensation.",
        "reference": "Constitution of Nepal, Article 21"
    },
    {
        "id": 23,
        "question": "Which Article guarantees the right to privacy?",
        "options": ["Article 26", "Article 27", "Article 28", "Article 29"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 28 guarantees the privacy of person, residence, property, document, data, correspondence and matters relating to character.",
        "reference": "Constitution of Nepal, Article 28"
    },
    {
        "id": 24,
        "question": "Which Article guarantees the right to clean environment?",
        "options": ["Article 28", "Article 29", "Article 30", "Article 31"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 30(1) guarantees every citizen the right to live in a clean and healthy environment.",
        "reference": "Constitution of Nepal, Article 30"
    },
    {
        "id": 25,
        "question": "According to Article 38(4), what principle applies to women's participation in State bodies?",
        "options": ["Merit-based only", "Principle of proportional inclusion", "Seniority-based", "First-come-first-served"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 38(4): Women shall have the right to participate in all bodies of the State on the basis of the principle of proportional inclusion.",
        "reference": "Constitution of Nepal, Article 38"
    },
    # Structure of State
    {
        "id": 26,
        "question": "How many levels of government does Nepal have under the Constitution?",
        "options": ["Two", "Three", "Four", "Five"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "The Constitution establishes three levels of government: Federation, State (Province), and Local level.",
        "reference": "Constitution of Nepal, Part 5"
    },
    {
        "id": 27,
        "question": "How many States (Provinces) are there in Nepal according to Schedule 4?",
        "options": ["Five", "Six", "Seven", "Eight"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Schedule 4 of the Constitution lists Seven States and their constituent districts.",
        "reference": "Constitution of Nepal, Schedule 4"
    },
    {
        "id": 28,
        "question": "Which Part of the Constitution deals with the President and Vice-President?",
        "options": ["Part 4", "Part 5", "Part 6", "Part 7"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 6 of the Constitution deals with the President and Vice-President of Nepal.",
        "reference": "Constitution of Nepal, Part 6"
    },
    {
        "id": 29,
        "question": "Which Part of the Constitution deals with the Federal Executive?",
        "options": ["Part 5", "Part 6", "Part 7", "Part 8"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 7 of the Constitution deals with the Federal Executive (Council of Ministers).",
        "reference": "Constitution of Nepal, Part 7"
    },
    {
        "id": 30,
        "question": "Which Part of the Constitution deals with the Federal Legislature (Parliament)?",
        "options": ["Part 7", "Part 8", "Part 9", "Part 10"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Part 8 of the Constitution establishes the Federal Legislature, which consists of two Houses: House of Representatives and National Assembly.",
        "reference": "Constitution of Nepal, Part 8"
    },
    # Judiciary & Commissions
    {
        "id": 31,
        "question": "Which Part of the Constitution deals with the Judiciary?",
        "options": ["Part 9", "Part 10", "Part 11", "Part 12"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 11 of the Constitution deals with the Judiciary, including the Supreme Court, High Courts, and District Courts.",
        "reference": "Constitution of Nepal, Part 11"
    },
    {
        "id": 32,
        "question": "Which Part of the Constitution deals with the Public Service Commission (Lok Sewa Aayog)?",
        "options": ["Part 21", "Part 22", "Part 23", "Part 24"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 23 of the Constitution deals with the Public Service Commission (Lok Sewa Aayog).",
        "reference": "Constitution of Nepal, Part 23"
    },
    {
        "id": 33,
        "question": "Which Part of the Constitution deals with the Election Commission?",
        "options": ["Part 22", "Part 23", "Part 24", "Part 25"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 24 of the Constitution deals with the Election Commission.",
        "reference": "Constitution of Nepal, Part 24"
    },
    {
        "id": 34,
        "question": "Which Part of the Constitution deals with the National Human Rights Commission?",
        "options": ["Part 23", "Part 24", "Part 25", "Part 26"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 25 of the Constitution deals with the National Human Rights Commission.",
        "reference": "Constitution of Nepal, Part 25"
    },
    {
        "id": 35,
        "question": "Which Part of the Constitution deals with the Auditor General?",
        "options": ["Part 20", "Part 21", "Part 22", "Part 23"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Part 22 of the Constitution deals with the Auditor General.",
        "reference": "Constitution of Nepal, Part 22"
    },
    # Directive Principles
    {
        "id": 36,
        "question": "Which Part of the Constitution contains Directive Principles, Policies and Obligations of the State?",
        "options": ["Part 3", "Part 4", "Part 5", "Part 6"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Part 4 of the Constitution contains Directive Principles, Policies and Obligations of the State.",
        "reference": "Constitution of Nepal, Part 4"
    },
    {
        "id": 37,
        "question": "According to Article 50(1), what is the political objective of the State?",
        "options": ["Establish communist rule", "Establish a public welfare system of governance", "Establish monarchy", "Establish military rule"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 50(1) states the political objective is to establish a public welfare system of governance through rule of law and social justice.",
        "reference": "Constitution of Nepal, Article 50"
    },
    {
        "id": 38,
        "question": "According to Article 50(3), what is the economic objective of the State?",
        "options": ["Capitalist economy", "Socialism-oriented independent and prosperous economy", "Pure socialist economy", "Free market economy only"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 50(3) aims to develop a socialism-oriented independent and prosperous economy while making the national economy independent, self-reliant and progressive.",
        "reference": "Constitution of Nepal, Article 50"
    },
    {
        "id": 39,
        "question": "According to Article 51(c)(5), what must the State end in society?",
        "options": ["Political parties", "All forms of discrimination, inequality, exploitation and injustice", "Religious practices", "Private property"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 51(c)(5) directs the State to end all forms of discrimination, inequality, exploitation and injustice in the name of religion, custom, usage, practice and tradition.",
        "reference": "Constitution of Nepal, Article 51"
    },
    {
        "id": 40,
        "question": "According to Article 51(d)(7), what trade practices must the State end?",
        "options": ["Export trade", "Black marketing, monopoly, artificial scarcity and restricting competition", "Small businesses", "Cooperatives"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 51(d)(7) directs the State to protect consumer interests by ending black marketing, monopoly, artificial scarcity and restricting competition.",
        "reference": "Constitution of Nepal, Article 51"
    },
    # Duties of Citizens
    {
        "id": 41,
        "question": "According to Article 48, which of the following is NOT a duty of citizens?",
        "options": ["To safeguard nationality and sovereignty", "To abide by the Constitution and law", "To pay taxes voluntarily", "To render compulsory service as required by State"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 48 lists duties: safeguard nationality, abide by Constitution/law, render compulsory service, protect public property. Paying taxes is not explicitly listed as a constitutional duty.",
        "reference": "Constitution of Nepal, Article 48"
    },
    {
        "id": 42,
        "question": "Which Article states that the Constitution is the fundamental law of Nepal?",
        "options": ["Article 1", "Article 2", "Article 3", "Article 4"],
        "correctIndex": 0,
        "subject": "CONSTITUTION",
        "explanation": "Article 1(1) states: This Constitution is the fundamental law of Nepal. Any law inconsistent with this Constitution shall be void.",
        "reference": "Constitution of Nepal, Article 1"
    },
    {
        "id": 43,
        "question": "Who does the sovereignty and state authority of Nepal vest in?",
        "options": ["The President", "The Parliament", "The Nepalese people", "The Council of Ministers"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 2 states: The sovereignty and state authority of Nepal shall be vested in the Nepalese people.",
        "reference": "Constitution of Nepal, Article 2"
    },
    {
        "id": 44,
        "question": "According to Article 26, what freedom does every person with faith in religion have?",
        "options": ["Only freedom to visit religious sites", "Freedom to profess, practice and protect religion", "Freedom to convert others", "Freedom to establish a state religion"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 26(1) guarantees freedom to profess, practice and protect religion according to one's conviction.",
        "reference": "Constitution of Nepal, Article 26"
    },
    {
        "id": 45,
        "question": "Which Article guarantees the right to social justice for marginalized communities?",
        "options": ["Article 40", "Article 41", "Article 42", "Article 43"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 42 guarantees the right to social justice and proportional inclusion in State bodies for socially backward groups.",
        "reference": "Constitution of Nepal, Article 42"
    },
    {
        "id": 46,
        "question": "According to Article 39(4), where can children NOT be employed?",
        "options": ["Schools", "Factories, mines or hazardous works", "Family businesses", "Agriculture"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "Article 39(4): No child shall be employed to work in any factory, mine or engaged in similar other hazardous works.",
        "reference": "Constitution of Nepal, Article 39"
    },
    {
        "id": 47,
        "question": "What is the minimum age for voting in Nepal according to the Constitution?",
        "options": ["16 years", "18 years", "21 years", "25 years"],
        "correctIndex": 1,
        "subject": "CONSTITUTION",
        "explanation": "The Constitution guarantees adult franchise (Article 50 mentions periodic elections and adult franchise as part of the democratic system).",
        "reference": "Constitution of Nepal, Preamble & Article 50"
    },
    {
        "id": 48,
        "question": "Which Article guarantees the right to health?",
        "options": ["Article 33", "Article 34", "Article 35", "Article 36"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 35 guarantees every citizen the right to free basic health services from the State and emergency health services.",
        "reference": "Constitution of Nepal, Article 35"
    },
    {
        "id": 49,
        "question": "Which Article guarantees the right to housing?",
        "options": ["Article 35", "Article 36", "Article 37", "Article 38"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Article 37 guarantees every citizen the right to appropriate housing and protection from arbitrary eviction.",
        "reference": "Constitution of Nepal, Article 37"
    },
    {
        "id": 50,
        "question": "Which Schedule of the Constitution lists the powers of the Local level?",
        "options": ["Schedule 6", "Schedule 7", "Schedule 8", "Schedule 9"],
        "correctIndex": 2,
        "subject": "CONSTITUTION",
        "explanation": "Schedule 8 lists the powers of the Local level. Schedule 5 is Federal, Schedule 6 is State, Schedule 7 is Concurrent (Federation and State).",
        "reference": "Constitution of Nepal, Schedule 8"
    }
]

# Nepali questions - direct translations with Nepali terminology
QUESTIONS_NE = [
    {"id": 1, "question": "नेपालको संविधान २०७२ (२०१५) कहिले जारी गरिएको थियो?", "options": ["२० सेप्टेम्बर २०१५", "२८ मे २००८", "१५ जनवरी २००७", "१० नोभेम्बर २००६"], "correctIndex": 0, "subject": "CONSTITUTION", "explanation": "नेपालको संविधान २० सेप्टेम्बर २०१५ (३ असोज २०७२) मा संविधानसभाबाट जारी गरिएको थियो।", "reference": "नेपालको संविधान, प्रस्तावना"},
    {"id": 2, "question": "संविधानको धारा ४ अनुसार नेपाल कस्तो राज्य हो?", "options": ["संघीय लोकतान्त्रिक गणतन्त्र", "संघीय लोकतान्त्रिक गणतन्त्रात्मक", "समाजवाद-oriented संघीय लोकतान्त्रिक गणतन्त्रात्मक", "समाजवादी संघीय गणतन्त्र"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ४ ले नेपाललाई स्वतन्त्र, अविभाज्य, सार्वभौमसत्ता सम्पन्न, धर्मनिरपेक्ष, समावेशी, लोकतान्त्रिक, समाजवाद-oriented संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य भनेको छ।", "reference": "नेपालको संविधान, धारा ४"},
    {"id": 3, "question": "संविधानको धारा ७ अनुसार नेपालको आधिकारिक भाषा के हो?", "options": ["देवनागरी लिपिमा नेपाली भाषा", "नेपाली र अंग्रेजी", "नेपाली, मैथिली र भोजपुरी", "आमाले बोल्ने सबै भाषाहरू"], "correctIndex": 0, "subject": "CONSTITUTION", "explanation": "धारा ७(१): नेपालको आधिकारिक भाषा देवनागरी लिपिमा नेपाली भाषा हुनेछ।", "reference": "नेपालको संविधान, धारा ७"},
    {"id": 4, "question": "नेपालको राष्ट्रिय चरा कुनलाई मान्यता दिइएको छ?", "options": ["गिद्ध", "डाँफे (लोफोफोरस)", "मयूर", "हिमाली मोनाल"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ९(३) ले डाँफे (लोफोफोरस) लाई नेपालको राष्ट्रिय चराको रूपमा घोषणा गरेको छ।", "reference": "नेपालको संविधान, धारा ९"},
    {"id": 5, "question": "संविधान अनुसार नेपालको राष्ट्रिय फूल के हो?", "options": ["कमल", "लालीगुराँस (रोडोडेन्ड्रोन अर्बोरियम)", "सूर्यमुखी", "गुलाब"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ९(३) ले लालीगुराँस (रोडोडेन्ड्रोन अर्बोरियम) लाई नेपालको राष्ट्रिय फूलको रूपमा घोषणा गरेको छ।", "reference": "नेपालको संविधान, धारा ९"},
    {"id": 6, "question": "धारा १० अनुसार नेपालमा कस्तो नागरिकताको व्यवस्था छ?", "options": ["दोहोरो नागरिकता", "एकल संघीय नागरिकता राज्य पहिचानसहित", "केवल राज्य नागरिकता", "सबैका लागि अंगीकृत नागरिकता"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा १०(२) ले नेपालमा एकल संघीय नागरिकता राज्य पहिचानसहितको व्यवस्था गरेको छ।", "reference": "नेपालको संविधान, धारा १०"},
    {"id": 7, "question": "धारा ११ अनुसार वंशजको आधारमा नागरिकता कसले प्राप्त गर्न सक्छ?", "options": ["जसको बुबा नेपाली हुन्छ", "जसको बुबा वा आमा नेपालको नागरिक हुन्", "केवल अंगीकृत नागरिकहरू", "नेपाली नागरिकसँग विवाह गर्ने विदेशीहरू"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ११(२)(क): जसको बुबा वा आमा नेपालको नागरिक हुन्, त्यस्तो व्यक्तिले वंशजको आधारमा नेपालको नागरिकता प्राप्त गर्नेछ।", "reference": "नेपालको संविधान, धारा ११"},
    {"id": 8, "question": "धारा १४ अनुसार गैर-आवासीय नेपाली नागरिकताको व्यवस्था के हो?", "options": ["पूर्ण राजनीतिक अधिकार", "आर्थिक, सामाजिक र सांस्कृतिक अधिकार मात्र", "कुनै अधिकार दिइँदैन", "अंगीकृत नागरिकताजस्तै"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा १४ ले गैर-आवासीय नेपाली नागरिकतालाई संघीय कानून बमोजिम आर्थिक, सामाजिक र सांस्कृतिक अधिकार प्रदान गर्छ।", "reference": "नेपालको संविधान, धारा १४"},
    {"id": 9, "question": "धारा १२ अनुसार नागरिकताको प्रमाणपत्रमा आमाको नाम उल्लेख गर्न मिल्छ?", "options": ["हुँदैन, केवल बुबाको नाम", "हुन्छ, लिङ्ग पहिचानसहित आमा वा बुबाको नाम", "विशेष अवस्थामा मात्र", "संविधानमा उल्लेख छैन"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा १२ ले नागरिकता प्रमाणपत्रमा लिङ्ग पहिचानसहित आमा वा बुबाको नाम उल्लेख गर्ने व्यवस्था गरेको छ।", "reference": "नेपालको संविधान, धारा १२"},
    {"id": 10, "question": "मौलिक हकहरू कार्यान्वयनका लागि राज्यलाई कति समयको म्याद दिइएको छ?", "options": ["एक वर्ष", "दुई वर्ष", "तीन वर्ष", "पाँच वर्ष"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ४७ ले संविधान प्रारम्भ भएको मितिले तीन वर्षभित्र मौलिक हकहरू कार्यान्वयन गर्ने कानूनी व्यवस्था गर्नुपर्ने व्यहोरा उल्लेख गरेको छ।", "reference": "नेपालको संविधान, धारा ४७"},
    {"id": 11, "question": "कुन धाराले सम्मानपूर्वक बाँच्ने हकको ग्यारेन्टी गर्छ?", "options": ["धारा १६", "धारा १७", "धारा १८", "धारा २०"], "correctIndex": 0, "subject": "CONSTITUTION", "explanation": "धारा १६ ले प्रत्येक व्यक्तिको सम्मानपूर्वक बाँच्ने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा १६"},
    {"id": 12, "question": "नेपालको संविधानले मृत्युदण्डको व्यवस्था गरेको छ?", "options": ["हो, गम्भीर अपराधका लागि", "हो, राष्ट्रपतिको अनुमोदनसहित", "हुँदैन, कुनै पनि व्यक्तिलाई मृत्युदण्ड दिने कानून बनाइनेछैन", "उल्लेख छैन"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा १६(२) मा स्पष्ट रूपमा भनिएको छ: कुनै पनि व्यक्तिलाई मृत्युदण्ड दिने व्यवस्था गर्ने कानून बनाइनेछैन।", "reference": "नेपालको संविधान, धारा १६"},
    {"id": 13, "question": "पक्राउ परेको व्यक्तिलाई कति घण्टाभित्र न्यायिक निकायसमक्ष पेश गर्नुपर्छ?", "options": ["१२ घण्टा", "२४ घण्टा", "४८ घण्टा", "७२ घण्टा"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा २०(३): पक्राउ परेको व्यक्तिलाई यात्राको समय बाहेक २४ घण्टाभित्र न्यायिक निकायसमक्ष पेश गर्नुपर्छ।", "reference": "नेपालको संविधान, धारा २०"},
    {"id": 14, "question": "समानताको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा १६", "धारा १७", "धारा १८", "धारा १९"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा १८ ले कानूनको अगाडि सबै नागरिक समान र समान कानूनी संरक्षणको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा १८"},
    {"id": 15, "question": "धारा १८(५) अनुसार छोरीहरूलाई पैतृक सम्पत्तिमा समान हक छ?", "options": ["हुँदैन, केवल छोरालाई", "हो, लैङ्गिक भेदभावबिना समान हक", "केवल अविवाहित छोरीलाई", "बुबाको मृत्युपछि मात्र"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा १८(५): सबै सन्तानलाई लैङ्गिक भेदभावबिना पैतृक सम्पत्तिमा समान हक हुनेछ।", "reference": "नेपालको संविधान, धारा १८"},
    {"id": 16, "question": "सूचनाको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा २५", "धारा २६", "धारा २७", "धारा २८"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा २७ ले प्रत्येक नागरिकलाई सार्वजनिक महत्त्वको विषयमा सूचना माग्ने र पाउने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा २७"},
    {"id": 17, "question": "शिक्षाको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा २९", "धारा ३०", "धारा ३१", "धारा ३२"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ३१ ले प्रत्येक नागरिकलाई आधारभूत शिक्षामा पहुँच र अनिवार्य निःशुल्क शिक्षाको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३१"},
    {"id": 18, "question": "धारा ३१(५) अनुसार समुदायहरूलाई आफ्नो मातृभाषामा शिक्षा पाउने हक छ?", "options": ["हुँदैन, केवल नेपाली भाषामा", "हो, प्रत्येक नेपाली समुदायलाई", "केवल निजी विद्यालयमा", "केवल प्राथमिक तहसम्म"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ३१(५): नेपालमा बसोबास गर्ने प्रत्येक नेपाली समुदायलाई आफ्नो मातृभाषामा शिक्षा पाउने हक हुनेछ।", "reference": "नेपालको संविधान, धारा ३१"},
    {"id": 19, "question": "रोजगारीको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा ३२", "धारा ३३", "धारा ३४", "धारा ३५"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ३३ ले प्रत्येक नागरिकलाई रोजगारीको हक र रोजगारी छनोट गर्ने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३३"},
    {"id": 20, "question": "खाद्य सार्वभौमसत्ताको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा ३४", "धारा ३५", "धारा ३६", "धारा ३७"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ३६(३) ले प्रत्येक नागरिकलाई कानून बमोजिम खाद्य सार्वभौमसत्ताको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३६"},
    {"id": 21, "question": "छुइछुत र भेदभाव निषेध कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा २२", "धारा २३", "धारा २४", "धारा २५"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा २४ ले कुनै पनि व्यक्तिलाई कुनै पनि निजी वा सार्वजनिक स्थानमा छुइछुत वा भेदभावको शिकार हुन नदिने व्यवस्था गर्छ।", "reference": "नेपालको संविधान, धारा २४"},
    {"id": 22, "question": "अपराधको पीडितको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["केवल प्रहरीमा उजुरी दिने हक", "अनुसन्धान र क्षतिपूर्तिको हक", "अपराधीलाई सजाय दिने हक", "कुनै विशेष हक छैन"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा २१ ले पीडितलाई अनुसन्धानको जानकारी र न्याय पाउने हक, क्षतिपूर्तিসহितको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा २१"},
    {"id": 23, "question": "गोपनीयताको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा २६", "धारा २७", "धारा २८", "धारा २९"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा २८ ले व्यक्तिको गोपनीयता, निवास, सम्पत्ति, कागजात, डाटा, पत्राचार र चरित्रसम्बन्धी विषयको गोपनीयताको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा २८"},
    {"id": 24, "question": "स्वच्छ वातावरणमा बाँच्ने हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा २८", "धारा २९", "धारा ३०", "धारा ३१"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ३०(१) ले प्रत्येक नागरिकलाई स्वच्छ र स्वस्थ्य वातावरणमा बाँच्ने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३०"},
    {"id": 25, "question": "धारा ३८(४) अनुसार राज्यका निकायमा महिलाको सहभागिताको सिद्धान्त के हो?", "options": ["योग्यतामा आधारित मात्र", "समानुपातिक समावेशीकरणको सिद्धान्त", "जेष्ठतामा आधारित", "पहिले आउने पहिले सेवा"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ३८(४): महिलालाई राज्यका सबै निकायमा समानुपातिक समावेशीकरणको सिद्धान्तको आधारमा सहभागी हुने हक हुनेछ।", "reference": "नेपालको संविधान, धारा ३८"},
    {"id": 26, "question": "संविधान अनुसार नेपालमा कति तहको सरकार छ?", "options": ["दुई", "तीन", "चार", "पाँच"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "संविधानले तीन तहको सरकारको व्यवस्था गरेको छ: संघ, प्रदेश र स्थानीय तह।", "reference": "नेपालको संविधान, भाग ५"},
    {"id": 27, "question": "अनुसूची ४ अनुसार नेपालमा कति वटा प्रदेश छन्?", "options": ["पाँच", "छ", "सात", "आठ"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "अनुसूची ४ मा नेपालका सात वटा प्रदेश र तिनका जिल्लाहरूको सूची रहेको छ।", "reference": "नेपालको संविधान, अनुसूची ४"},
    {"id": 28, "question": "संविधानको कुन भागमा राष्ट्रपति र उपराष्ट्रपतिसम्बन्धी व्यवस्था छ?", "options": ["भाग ४", "भाग ५", "भाग ६", "भाग ७"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग ६ मा राष्ट्रपति र उपराष्ट्रपतिसम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग ६"},
    {"id": 29, "question": "संविधानको कुन भागमा संघीय कार्यपालिकासम्बन्धी व्यवस्था छ?", "options": ["भाग ५", "भाग ६", "भाग ७", "भाग ८"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग ७ मा संघीय कार्यपालिका (मन्त्रिपरिषद्) सम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग ७"},
    {"id": 30, "question": "संविधानको कुन भागमा संघीय व्यवस्थापिका (संसद्) सम्बन्धी व्यवस्था छ?", "options": ["भाग ७", "भाग ८", "भाग ९", "भाग १०"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "भाग ८ मा संघीय व्यवस्थापिकाको व्यवस्था गरिएको छ, जसमा प्रतिनिधिसभा र राष्ट्रियसभा गरी दुई सदन रहन्छन्।", "reference": "नेपालको संविधान, भाग ८"},
    {"id": 31, "question": "संविधानको कुन भागमा न्यायपालिकासम्बन्धी व्यवस्था छ?", "options": ["भाग ९", "भाग १०", "भाग ११", "भाग १२"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग ११ मा न्यायपालिकासम्बन्धी व्यवस्था रहेको छ, जसमा सर्वोच्च अदालत, उच्च अदालत र जिल्ला अदालत रहन्छन्।", "reference": "नेपालको संविधान, भाग ११"},
    {"id": 32, "question": "संविधानको कुन भागमा लोक सेवा आयोगसम्बन्धी व्यवस्था छ?", "options": ["भाग २१", "भाग २२", "भाग २३", "भाग २४"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग २३ मा लोक सेवा आयोगसम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग २३"},
    {"id": 33, "question": "संविधानको कुन भागमा निर्वाचन आयोगसम्बन्धी व्यवस्था छ?", "options": ["भाग २२", "भाग २३", "भाग २४", "भाग २५"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग २४ मा निर्वाचन आयोगसम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग २४"},
    {"id": 34, "question": "संविधानको कुन भागमा राष्ट्रिय मानव अधिकार आयोगसम्बन्धी व्यवस्था छ?", "options": ["भाग २३", "भाग २४", "भाग २५", "भाग २६"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग २५ मा राष्ट्रिय मानव अधिकार आयोगसम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग २५"},
    {"id": 35, "question": "संविधानको कुन भागमा महालेखा परीक्षकसम्बन्धी व्यवस्था छ?", "options": ["भाग २०", "भाग २१", "भाग २२", "भाग २३"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "भाग २२ मा महालेखा परीक्षकसम्बन्धी व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग २२"},
    {"id": 36, "question": "संविधानको कुन भागमा राज्यका नीति तथा दायित्वहरू रहेका छन्?", "options": ["भाग ३", "भाग ४", "भाग ५", "भाग ६"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "भाग ४ मा राज्यका नी-directed सिद्धान्त, नीति र दायित्वहरूको व्यवस्था रहेको छ।", "reference": "नेपालको संविधान, भाग ४"},
    {"id": 37, "question": "धारा ५०(१) अनुसार राज्यको राजनीतिक उद्देश्य के हो?", "options": ["साम्यवाद स्थापना", "कल्याणकारी शासन व्यवस्थाको स्थापना", "राजतन्त्र पुनर्स्थापना", "सैनिक शासन स्थापना"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ५०(१) ले कानूनी राज्य र सामाजिक न्यायमार्फत कल्याणकारी शासन व्यवस्थाको स्थापना गर्ने राजनीतिक उद्देश्य राखेको छ।", "reference": "नेपालको संविधान, धारा ५०"},
    {"id": 38, "question": "धारा ५०(३) अनुसार राज्यको आर्थिक उद्देश्य के हो?", "options": ["पूँजीवादी अर्थतन्त्र", "समाजवाद-oriented स्वतन्त्र र समृद्ध अर्थतन्त्र", "शुद्ध समाजवादी अर्थतन्त्र", "केवल स्वतन्त्र बजार अर्थतन्त्र"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ५०(३) ले समाजवाद-oriented स्वतन्त्र र समृद्ध अर्थतन्त्र विकास गर्ने उद्देश्य राखेको छ।", "reference": "नेपालको संविधान, धारा ५०"},
    {"id": 39, "question": "धारा ५१(क)(५) अनुसार राज्यले समाजमा के अन्त्य गर्नुपर्छ?", "options": ["राजनीतिक दलहरू", "सबै प्रकारका भेदभाव, असमानता, शोषण र अन्याय", "धार्मिक अभ्यासहरू", "निजी सम्पत्ति"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ५१(क)(५) ले धर्म, संस्कृति, परम्परा, चलन र अभ्यासको नाममा हुने सबै प्रकारका भेदभाव, असमानता, शोषण र अन्याय अन्त्य गर्न निर्देशन दिएको छ।", "reference": "नेपालको संविधान, धारा ५१"},
    {"id": 40, "question": "धारा ५१(ख)(७) अनुसार राज्यले कस्ता व्यापारिक अभ्यासहरू अन्त्य गर्नुपर्छ?", "options": ["निर्यात व्यापार", "कालोबजारी, एकाधिकार, कृत्रिम अभाव र प्रतिस्पर्धा प्रतिबन्ध", "साना व्यवसायहरू", "सहकारीहरू"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ५१(ख)(७) ले उपभोक्ताको हित संरक्षण गर्न कालोबजारी, एकाधिकार, कृत्रिम अभाव र प्रतिस्पर्धा प्रतिबन्ध गर्ने क्रियाकलापहरू अन्त्य गर्न निर्देशन दिएको छ।", "reference": "नेपालको संविधान, धारा ५१"},
    {"id": 41, "question": "धारा ४८ अनुसार निम्नमध्ये कुन नागरिकको दायित्व होइन?", "options": ["राष्ट्रियता र सार्वभौमसत्ताको संरक्षण", "संविधान र कानूनको पालना", "स्वेच्छाले कर तिर्ने", "राज्यले माग गर्दा अनिवार्य सेवा"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ४८ मा नागरिकका दायित्वहरू: राष्ट्रियताको संरक्षण, संविधान/कानूनको पालना, अनिवार्य सेवा, सार्वजनिक सम्पत्तिको संरक्षण। स्वेच्छाले कर तिर्ने दायित्व स्पष्ट रूपमा उल्लेख छैन।", "reference": "नेपालको संविधान, धारा ४८"},
    {"id": 42, "question": "कुन धाराले संविधान नेपालको मौलिक कानून हो भन्ने व्यवस्था गर्छ?", "options": ["धारा १", "धारा २", "धारा ३", "धारा ४"], "correctIndex": 0, "subject": "CONSTITUTION", "explanation": "धारा १(१): यो संविधान नेपालको मौलिक कानून हो। यस संविधानसँग बाझिने कुनै पनि कानून त्यति मात्रामा बदर हुनेछ।", "reference": "नेपालको संविधान, धारा १"},
    {"id": 43, "question": "नेपालको सार्वभौमसत्ता र राज्य अधिकार कसमा निहित छ?", "options": ["राष्ट्रपतिमा", "संसद्मा", "नेपाली जनतामा", "मन्त्रिपरिषद्मा"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा २: नेपालको सार्वभौमसत्ता र राज्य अधिकार नेपाली जनतामा निहित हुनेछ।", "reference": "नेपालको संविधान, धारा २"},
    {"id": 44, "question": "धारा २६ अनुसार धार्मिक विश्वास राख्ने प्रत्येक व्यक्तिलाई कस्तो स्वतन्त्रता छ?", "options": ["केवल धार्मिक स्थलहरूमा जाने स्वतन्त्रता", "आफ्नो धर्म अवलम्बन, अभ्यास र संरक्षण गर्ने स्वतन्त्रता", "अरूलाई धर्म परिवर्तन गराउने", "राज्य धर्म स्थापना गर्ने"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा २६(१) ले धार्मिक विश्वास राख्ने प्रत्येक व्यक्तिलाई आफ्नो धर्म अवलम्बन, अभ्यास र संरक्षण गर्ने स्वतन्त्रताको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा २६"},
    {"id": 45, "question": "सामाजिक न्यायको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा ४०", "धारा ४१", "धारा ४२", "धारा ४३"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ४२ ले सामाजिक रूपमा पछाडि परेका समुदायलाई राज्य निकायमा समानुपातिक समावेशीकरणको हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ४२"},
    {"id": 46, "question": "धारा ३९(४) अनुसार बालबालिकालाई कहाँ रोजगारीमा लगाउन हुँदैन?", "options": ["विद्यालयहरूमा", "कारखाना, खानी वा जोखिमयुक्त काममा", "पारिवारिक व्यवसायमा", "कृषि काममा"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "धारा ३९(४): कुनै पनि बालबालिकालाई कारखाना, खानी वा त्यस्तै अन्य जोखिमयुक्त काममा रोजगारीमा लगाइनेछैन।", "reference": "नेपालको संविधान, धारा ३९"},
    {"id": 47, "question": "संविधान अनुसार नेपालमा मतदानको न्यूनतम उमेर कति हो?", "options": ["१६ वर्ष", "१८ वर्ष", "२१ वर्ष", "२५ वर्ष"], "correctIndex": 1, "subject": "CONSTITUTION", "explanation": "संविधानले वयस्क मताधिकार (१८ वर्ष पूरा भएका नागरिकको मताधिकार) को व्यवस्था गरेको छ।", "reference": "नेपालको संविधान, प्रस्तावना र धारा ५०"},
    {"id": 48, "question": "स्वास्थ्यसम्बन्धी हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा ३३", "धारा ३४", "धारा ३५", "धारा ३६"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ३५ ले प्रत्येक नागरिकलाई राज्यबाट निःशुल्क आधारभूत स्वास्थ्य सेवा र आपतकालीन स्वास्थ्य सेवाबाट वञ्चित नगरिने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३५"},
    {"id": 49, "question": "आवासको हक कुन धारामा व्यवस्था गरिएको छ?", "options": ["धारा ३५", "धारा ३६", "धारा ३७", "धारा ३८"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "धारा ३७ ले प्रत्येक नागरिकलाई उपयुक्त आवासको हक र आफ्नो निवासबाट अनावश्यक रूपमा निष्कासन नगरिने हकको ग्यारेन्टी गर्छ।", "reference": "नेपालको संविधान, धारा ३७"},
    {"id": 50, "question": "संविधानको कुन अनुसूचिमा स्थानीय तहका अधिकारहरूको सूची रहेको छ?", "options": ["अनुसूची ६", "अनुसूची ७", "अनुसूची ८", "अनुसूची ९"], "correctIndex": 2, "subject": "CONSTITUTION", "explanation": "अनुसूची ८ मा स्थानीय तहका अधिकारहरूको सूची रहेको छ। अनुसूची ५ = संघीय, अनुसूची ६ = प्रदेश, अनुसूची ७ = संयुक्त (संघ र प्रदेश)।", "reference": "नेपालको संविधान, अनुसूची ८"}
]


def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    
    # Set 1 English
    set1_en = {
        "setId": "constitution-set1",
        "title": "Set 1: Constitution of Nepal",
        "description": "50 questions on the Constitution of Nepal 2072 (2015).",
        "category": "constitution",
        "locked": False,
        "timeLimit": 1800,
        "passingScore": 60,
        "questions": QUESTIONS_EN
    }
    
    # Set 1 Nepali
    set1_ne = {
        "setId": "constitution-set1",
        "title": "सेट १: नेपालको संविधान",
        "description": "नेपालको संविधान २०७२ सम्बन्धी ५० प्रश्नहरू।",
        "category": "constitution",
        "locked": False,
        "timeLimit": 1800,
        "passingScore": 60,
        "questions": QUESTIONS_NE
    }
    
    save_json(set1_en, os.path.join(base, '../data/en/constitution/set1.json'))
    save_json(set1_ne, os.path.join(base, '../data/ne/constitution/set1.json'))
    
    # tests.json for constitution
    tests = {
        "category": "constitution",
        "sets": [
            {"setId": "constitution-set1", "setNumber": 1, "title": {"en": "Set 1: Constitution of Nepal", "ne": "सेट १: नेपालको संविधान"}, "description": {"en": "50 questions on Constitution of Nepal 2072.", "ne": "नेपालको संविधान २०७२ सम्बन्धी ५० प्रश्नहरू।"}, "locked": False, "passingScore": 60, "timeLimit": 1800},
            {"setId": "constitution-set2", "setNumber": 2, "title": {"en": "Set 2: Constitution of Nepal", "ne": "सेट २: नेपालको संविधान"}, "description": {"en": "Coming soon.", "ne": "चाँडै आउँदैछ।"}, "locked": True, "passingScore": 60, "timeLimit": 1800},
            {"setId": "constitution-set3", "setNumber": 3, "title": {"en": "Set 3: Constitution of Nepal", "ne": "सेट ३: नेपालको संविधान"}, "description": {"en": "Coming soon.", "ne": "चाँडै आउँदैछ।"}, "locked": True, "passingScore": 60, "timeLimit": 1800}
        ]
    }
    save_json(tests, os.path.join(base, '../data/en/constitution/tests.json'))
    save_json(tests, os.path.join(base, '../data/ne/constitution/tests.json'))
    
    print("Constitution category generated successfully!")
    print(f"Total questions: {len(QUESTIONS_EN)}")


if __name__ == '__main__':
    main()
