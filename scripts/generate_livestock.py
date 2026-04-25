#!/usr/bin/env python3
"""Generate Livestock Technician (Nayab Pashu Sewa) question sets."""
import json, os

# All 50 questions extracted from Sudurpashchim Pradesh Lok Sewa exam
# for Nayab Pashu Sewa Prabidhik (Livestock Technician), 4th level

QUESTIONS_NE = [
    {
        "id": "q1", "question": "नेपालमा हालसम्मको अध्ययन र अनुसन्धानअनुसार कति जातका माछाहरू पाइएको छ?",
        "options": ["१३२२", "२०२", "२३२२", "२६२२"], "correctIndex": 2,
        "explanation": "नेपालमा हालसम्मको अध्ययन र अनुसन्धानअनुसार २,३२२ जातका माछाहरू पाइएको छ।", "subject": "SCIENCE"
    },
    {
        "id": "q2", "question": "नेपालमा जल संरक्षण ऐन कति सालमा बनेको हो?",
        "options": ["२०१५ साल", "२०१७ साल", "२०२० साल", "२०३० साल"], "correctIndex": 1,
        "explanation": "नेपालमा जल संरक्षण ऐन सन् २०१७ मा बनेको हो।", "subject": "CONSTITUTION"
    },
    {
        "id": "q3", "question": "नेपालमा उन्नत तथा वणशंकर गाइको प्रतिशत कति छ?",
        "options": ["५%", "१३%", "३०%", "४०%"], "correctIndex": 1,
        "explanation": "नेपालमा उन्नत तथा वणशंकर (crossbred) गाइको प्रतिशत लगभग १३% रहेको छ।", "subject": "GK"
    },
    {
        "id": "q4", "question": "कृषि विभागबाट अलग्गो पशुपक्षी तथा पशु स्वास्थ्य विभागको छुट्टै स्थापना कुन सालमा भएको हो?",
        "options": ["२०१७", "२०२३", "२०२७", "२०३२"], "correctIndex": 1,
        "explanation": "कृषि विभागबाट अलग्गो पशुपक्षी तथा पशु स्वास्थ्य विभागको स्थापना सन् २०२३ मा भएको हो।", "subject": "GK"
    },
    {
        "id": "q5", "question": "कृषि/पशुपक्षी/मत्स्य प्रसारका विभिन्न तरिकाहरू के-के हुन्?",
        "options": ["रेडियो तथा टि.भी.", "पोस्टर, पम्पलेट, न्युज पेपर", "प्रदर्शनी", "माथिका सबै"], "correctIndex": 3,
        "explanation": "कृषि, पशुपक्षी र मत्स्य प्रसारका लागि रेडियो, टिभी, पोस्टर, पम्पलेट, न्युजपेपर र प्रदर्शनी सबै तरिकाहरू प्रयोग गरिन्छन्।", "subject": "GK"
    },
    {
        "id": "q6", "question": "नेपाल संघीय शासन प्रणालीमा गएपछि स्थानीय सरकार सञ्चालन ऐन कति सालमा कार्यान्वयनमा आयो?",
        "options": ["२०७३", "२०७४", "२०७५", "२०७६"], "correctIndex": 1,
        "explanation": "नेपाल संघीय शासन प्रणालीमा गएपछि स्थानीय सरकार सञ्चालन ऐन २०७४ मा कार्यान्वयनमा आएको हो।", "subject": "CONSTITUTION"
    },
    {
        "id": "q7", "question": "नेपालको संविधानमा खाद्य सम्बन्धी हक कुन धारामा उल्लेख छ?",
        "options": ["धारा ३६", "धारा ४४", "धारा २२", "धारा २४"], "correctIndex": 0,
        "explanation": "नेपालको संविधान २०७२ को धारा ३६ मा खाद्य सम्बन्धी हकको व्यवस्था गरिएको छ।", "subject": "CONSTITUTION"
    },
    {
        "id": "q8", "question": "चालु आवधिक योजनाको अन्तसम्म माछा उत्पादन वृद्धिको लक्ष्य कति छ?",
        "options": ["4 MT/Hact.", "6 MT/Hact.", "8 MT/Hact.", "10 MT/Hact."], "correctIndex": 1,
        "explanation": "चालु आवधिक योजनाको अन्तसम्म माछा उत्पादन वृद्धिको लक्ष्य ६ मेट्रिक टन प्रति हेक्टर रहेको छ।", "subject": "GK"
    },
    {
        "id": "q9", "question": "क्वारेन्टाइनको बाटो बिराई रोगी पशु पेटारी गरेमा सजाय कति हुन्छ?",
        "options": ["१० हजार", "२५ हजार", "५० हजार", "१ लाख"], "correctIndex": 2,
        "explanation": "क्वारेन्टाइनको बाटो बिराई रोगी पशु पेटारी गरेमा रु ५० हजारसम्म जरिवाना हुन सक्छ।", "subject": "CONSTITUTION"
    },
    {
        "id": "q10", "question": "नेपालमा कुल मासु उत्पादनको हिस्सामा बाख्राको मासुको हिस्सा कति प्रतिशत छ?",
        "options": ["१०%", "१५%", "२०%", "२५%"], "correctIndex": 1,
        "explanation": "नेपालमा कुल मासु उत्पादनको हिस्सामा बाख्राको मासुको योगदान लगभग १५% रहेको छ।", "subject": "GK"
    },
    {
        "id": "q11", "question": "दाना जाँचकीको नियुक्ति कसले गर्दछ?",
        "options": ["नेपाल सरकार", "प्रदेश सरकार", "पालिकाहरू", "A र B"], "correctIndex": 3,
        "explanation": "दाना जाँचकीको नियुक्ति नेपाल सरकार र प्रदेश सरकार दुवैले गर्ने व्यवस्था रहेको छ।", "subject": "CONSTITUTION"
    },
    {
        "id": "q12", "question": "दाना पदार्थ ऐन, २०३२ अनुसार कुन विभागको मुख्य जिम्मेवारी छ?",
        "options": ["पशु सेवा विभाग", "खाद्य प्रविधि तथा गुण नियन्त्रण विभाग", "कृषि विभाग", "वाणिज्य विभाग"], "correctIndex": 1,
        "explanation": "दाना पदार्थ ऐन, २०३२ अनुसार खाद्य प्रविधि तथा गुण नियन्त्रण विभागले दानाको गुणस्तर नियन्त्रणको मुख्य जिम्मेवारी लिएको छ।", "subject": "CONSTITUTION"
    },
    {
        "id": "q13", "question": "नेपालमा Hydroponics प्रविधिबाट पशुपालनमा के गरिन्छ?",
        "options": ["प्रयोगशालामा बिरुवा उत्पादन गर्ने", "जमिनमा घाँस उत्पादन गर्ने", "जमिनमा बिरुवा उत्पादन गर्ने", "पानीमा घाँस उत्पादन गर्ने"], "correctIndex": 3,
        "explanation": "Hydroponics प्रविधिमा बिरुवालाई माटोबिना पानीमा मात्र पोषक तत्व दिई उत्पादन गरिन्छ। नेपालमा यस प्रविधिबाट पशुका लागि पानीमा घाँस उत्पादन गरिन्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q14", "question": "पशु दुहानी गर्दा दैनिक कति घण्टाभन्दा बढी हिँडाउनु हुँदैन?",
        "options": ["६", "८", "१०", "१२"], "correctIndex": 1,
        "explanation": "पशु दुहानी गर्दा दैनिक ८ घण्टाभन्दा बढी हिँडाउनु हुँदैन। बढी हिँडाउँदा दुध उत्पादनमा ह्रास आउन सक्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q15", "question": "Penta sulfate कुन रोगमा प्रयोग गरिन्छ?",
        "options": ["पिका", "खेर", "किटोसिस", "क्षयरोग"], "correctIndex": 1,
        "explanation": "Penta sulfate (पेन्टा सल्फेट) खेर (anthrax) रोगको उपचारमा प्रयोग गरिने एन्टिबायोटिक हो।", "subject": "SCIENCE"
    },
    {
        "id": "q16", "question": "कुखुराको कुन रोगमा शरीरको रोगसँग लड्ने क्षमतामा पूर्ण ह्रास आउने गरी नोक्सानी गर्छ?",
        "options": ["फाउल पक्स", "फाउल क्लेरा", "गम्बोरो", "पुलोरम"], "correctIndex": 2,
        "explanation": "गम्बोरो (Infectious Bursal Disease - IBD) ले कुखुराको बर्सा (bursa) नष्ट गरी शरीरको रोग प्रतिरोधात्मक क्षमतामा पूर्ण ह्रास ल्याउँछ।", "subject": "SCIENCE"
    },
    {
        "id": "q17", "question": "Heterakis Gallinarum कुखुराको कुन अंशमा गई बस्छ?",
        "options": ["Small Intestine", "Caecum, Colon", "Oesophagus", "Caecum, colon, rectum"], "correctIndex": 1,
        "explanation": "Heterakis Gallinarum कुखुराको सिकम (caecum) र कोलन (colon) मा गई बस्ने एक प्रकारको परजीवी जुका हो।", "subject": "SCIENCE"
    },
    {
        "id": "q18", "question": "कुशी (Lumbar Paralysis) कुन परजीवीको कारणले हुन्छ?",
        "options": ["Thelazia sps.", "Staria sps.", "Oesophagostomum", "Nematodirus"], "correctIndex": 1,
        "explanation": "कुशी (Lumbar Paralysis) रोग Staria (Setaria) प्रजातिको परजीवीको कारणले हुन्छ, जुन गाइभैंसीको शरीरमा पाइन्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q19", "question": "Bladder worm भनाले तलका मध्ये कसलाई बुझाउँछ?",
        "options": ["पित थैली जुका", "पिसाब थैली जुका", "गोलो जुका", "फिते जुकाको पानी फोका"], "correctIndex": 1,
        "explanation": "Bladder worm भनाले Cysticercus (सिस्टिसर्कस) अवस्थालाई बुझाउँछ, जुन पिसाब थैली जुकाको एक अवस्था हो।", "subject": "SCIENCE"
    },
    {
        "id": "q20", "question": "दूषीको कारणबाट हाँस (duck) मा लाग्ने रोग कुन हो?",
        "options": ["कक्सिडियोसिस (Coccidiosis)", "साल्मोनेल्लोसिस (Salmonellosis)", "एस्परजेल्लोसिस (Aspergillosis)", "माथिका कुनै पनि होइन"], "correctIndex": 2,
        "explanation": "Aspergillosis (एस्परजेल्लोसिस) रोग दूषी (Aspergillus फङ्गस) को कारणले हाँसमा लाग्ने गर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q21", "question": "कुखुरामा लाग्ने निम्न रोगहरू मध्ये विषाणुबाट लाग्ने रोग कुन हो?",
        "options": ["ई. कोलाइ", "साल्मोनेल्लोसिस", "म्योरेक्स", "कक्सिडियोसिस"], "correctIndex": 2,
        "explanation": "म्योरेक्स (Marek's Disease) कुखुरामा लाग्ने एक विषाणुजन्य रोग हो। अन्य विकल्पहरू ब्याक्टेरिया वा परजीवीजन्य हुन्।", "subject": "SCIENCE"
    },
    {
        "id": "q22", "question": "रानीखेत रोगमा Post-mortem गर्दा रक्तश्राव कहाँ देखिन्छ?",
        "options": ["प्रोभेन्ट्रिकुलस", "सिजर", "छाला", "आँखा"], "correctIndex": 0,
        "explanation": "रानीखेत (Newcastle Disease) रोगमा मरेका कुखुराको Post-mortem गर्दा प्रोभेन्ट्रिकुलस (proventriculus) मा रक्तश्राव देखिन्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q23", "question": "नेपालमा भेडा बाख्रामा पाइने प्रमुख रोगको खोप दक्षिण एसियामा नै पहिलो पटक बनेको भियो, त्यो कुन रोग हो?",
        "options": ["Enterotaxemia", "FMD", "PPR", "Foot rot"], "correctIndex": 2,
        "explanation": "PPR (Peste des Petits Ruminants) रोगको खोप नेपालमा दक्षिण एसियामा नै पहिलो पटक बनाइएको हो। यो भेडा बाख्राको एक गम्भीर विषाणुजन्य रोग हो।", "subject": "SCIENCE"
    },
    {
        "id": "q24", "question": "Thelazia को आम बोलचालिको नाम के हो?",
        "options": ["Guinea worm", "Whip worm", "Pin worm", "Eye worm"], "correctIndex": 3,
        "explanation": "Thelazia लाई आम बोलचालमा 'Eye worm' (आँखा जुका) भनिन्छ किनभने यो पशुको आँखामा पाइन्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q25", "question": "White muscle disease पशुमा कुन तत्वको कमीबाट हुन्छ?",
        "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin E"], "correctIndex": 3,
        "explanation": "White muscle disease पशुमा Vitamin E र सेलेनियमको कमीबाट हुने रोग हो, जसले मांसपेशीमा सेतो दाग बनाउँछ।", "subject": "SCIENCE"
    },
    {
        "id": "q26", "question": "LSD खोप नेपालमा कुन Strain लगाउन सिफारिस गरिएको छ?",
        "options": ["Sheep pox", "Capri pox", "Neethling", "All of the above"], "correctIndex": 2,
        "explanation": "LSD (Lumpy Skin Disease) खोप नेपालमा Neethling strain लगाउन सिफारिस गरिएको छ।", "subject": "SCIENCE"
    },
    {
        "id": "q27", "question": "गाइभैंसीले राख्ने गरेको बच्चालाई सर्ने हर्मोन कुन हो?",
        "options": ["GnRH", "Prolactin", "Estrogen", "Progesterone"], "correctIndex": 3,
        "explanation": "Progesterone (प्रोजेस्टेरोन) हर्मोनले गर्भाधान र गर्भाशयमा बच्चा राख्ने क्रियालाई नियन्त्रण गर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q28", "question": "तलका मध्ये कुन बैंशी रैथाने होइन?",
        "options": ["लिमे", "पार्कटे", "राँढी", "निलिरामी"], "correctIndex": 3,
        "explanation": "निलिरामी (Nilirami) बैंशी रैथाने (indigenous) जात होइन। लिमे, पार्कटे र राँढी नेपालका रैथाने बैंशी जातहरू हुन्।", "subject": "GK"
    },
    {
        "id": "q29", "question": "मकैमा चिल्लो पदार्थको मात्रा कति हुन्छ?",
        "options": ["६०%", "५०%", "५०%", "९०%"], "correctIndex": 2,
        "explanation": "मकैमा चिल्लो पदार्थ (fat) को मात्रा लगभग ५०% हुन्छ। यो पशु आहारको राम्रो स्रोत हो।", "subject": "SCIENCE"
    },
    {
        "id": "q30", "question": "बहुउद्देशीय (Multipurpose use of eggs and meat) को लागि कुन जातको विकास कुखुरा सिफारिस गरिएको छ?",
        "options": ["Black Australorp", "New Hampshire", "Giriraja", "White leg-horn"], "correctIndex": 2,
        "explanation": "Giriraja (गिरिराज) कुखुरा नेपालमा बहुउद्देशीय (अन्डा र मासु दुवै) उत्पादनका लागि विकास गरिएको जात हो।", "subject": "GK"
    },
    {
        "id": "q31", "question": "परालमा युरियाको उपचार गरी खुवाउँदा अधिकतम कति प्रतिशत युरिया मिसाउन सकिन्छ?",
        "options": ["१-२%", "२-५%", "३-५%", "५-१०%"], "correctIndex": 1,
        "explanation": "परालमा युरिया मिसाउँदा अधिकतम २-५% सम्म मिसाउन सकिन्छ। बढी मिसाउँदा पशुलाई हानि हुन सक्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q32", "question": "गाइभैंसीले भाले खोजेको कति घण्टापछि AI गरिन्छ?",
        "options": ["१२-१८ घण्टा", "२०-२४ घण्टा", "६-१२ घण्टा", "१८-२२ घण्टा"], "correctIndex": 0,
        "explanation": "गाइभैंसीले भाले खोज्ने (heat) लक्षण देखाएको १२-१८ घण्टापछि AI (कृत्रिम गर्भाधान) गर्नुपर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q33", "question": "डोपिल डोपिल कुन प्रकारको घाँस हो?",
        "options": ["डाले-घाँस", "कोसे घाँस", "A र B दुवै", "मुई अकाँस"], "correctIndex": 2,
        "explanation": "डोपिल डोपिल (Desmodium) डाले-घाँस र कोसे (Leguminous) दुवै प्रकारको घाँस हो।", "subject": "SCIENCE"
    },
    {
        "id": "q34", "question": "तलका मध्ये कोसे घाँस (Leguminous) कुन हो?",
        "options": ["डेसमोडियम, स्टाइलो र वरसिम", "सेन्ट्रो, ह्वाइट क्लोभर र बोडी", "केराउ, भेड र ज्वाइन्ट भेड", "माथिका सबै"], "correctIndex": 3,
        "explanation": "डेसमोडियम, स्टाइलो, वरसिम, सेन्ट्रो, ह्वाइट क्लोभर, बोडी, केराउ, भेड र ज्वाइन्ट भेड सबै कोसे (Leguminous) घाँसहरू हुन्।", "subject": "SCIENCE"
    },
    {
        "id": "q35", "question": "तलका मध्ये उनको लागि पालिने उत्तम जातको भेडा कुन हो?",
        "options": ["लाम्पुच्छे", "कागे", "बरवाल", "मेरिनो"], "correctIndex": 3,
        "explanation": "मेरिनो (Merino) भेडा उन (wool) उत्पादनका लागि विश्वव्यापी रूपमा चिनिने उत्तम जातको भेडा हो।", "subject": "GK"
    },
    {
        "id": "q36", "question": "पाकिबास कालो बंगुर विकास गर्दा तल उल्लेखित कुन बंगुरलाई प्रजनन गराइएको विवरण?",
        "options": ["स्याउलब्याक", "फायुन", "योर्कसायर", "टेमवर्थ"], "correctIndex": 2,
        "explanation": "पाकिबास कालो बंगुर विकास गर्दा योर्कसायर (Yorkshire) जातको बंगुरलाई प्रजननमा प्रयोग गरिएको हो।", "subject": "GK"
    },
    {
        "id": "q37", "question": "बरसिम घाँस खेती गर्न बिउ कति कि.ग्रा./हेक्टर हुनुपर्छ?",
        "options": ["१०-१५", "२०-२५", "२५-३०", "३०-३५"], "correctIndex": 1,
        "explanation": "बरसिम घाँस खेती गर्न प्रति हेक्टर २०-२५ किलोग्राम बिउ आवश्यक पर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q38", "question": "बैंशीले रोगी खोजेको कति घण्टामा बाली लगाउनुपर्छ?",
        "options": ["०-६", "६-१२", "१२-१८", "१८-२४"], "correctIndex": 2,
        "explanation": "बैंशीले रोगी (heat) लक्षण देखाएको १२-१८ घण्टाभित्र बाली (insemination) लगाउनुपर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q39", "question": "माछा पोखरीमा अक्सिजन आपूर्ति गर्न कुन विधि प्रयोग गरिन्छ?",
        "options": ["एरिएसन", "पम्पिङ", "स्टिरिङ", "B र C"], "correctIndex": 0,
        "explanation": "माछा पोखरीमा अक्सिजन आपूर्ति गर्न Aeration (एरिएसन) विधि प्रयोग गरिन्छ, जसले पानीमा हावा मिसाई अक्सिजनको मात्रा बढाउँछ।", "subject": "SCIENCE"
    },
    {
        "id": "q40", "question": "नेपालमा अनुसन्धान गरी बिसो पानीको Raceway मा पालिने उन्नत माछा कुन हो?",
        "options": ["Labeo Rohita", "Rainbow trout", "Mrigala", "Grass Carp"], "correctIndex": 1,
        "explanation": "Rainbow trout (रेनबो ट्राउट) नेपालमा बिसो पानीको Raceway मा पालिने उन्नत माछा हो।", "subject": "GK"
    },
    {
        "id": "q41", "question": "तलका मध्ये कुन जातका माछाहरू धान खेतीमा पाल्न उपयुक्त हुन्छन्?",
        "options": ["कटला", "रोहु", "मृगाल र कटला", "माथिका सबै"], "correctIndex": 3,
        "explanation": "कटला (Catla), रोहु (Rohu) र मृगाल (Mrigal) सबै धान खेतीको पोखरीमा पाल्न उपयुक्त माछाहरू हुन्। यसलाई 'रितो माछापालन' (Rice-fish farming) भनिन्छ।", "subject": "GK"
    },
    {
        "id": "q42", "question": "कमन कार्प (Fry) को दानामा प्रोटिन कति प्रतिशत राखिन्छ?",
        "options": ["४५", "५०", "५५", "६०"], "correctIndex": 0,
        "explanation": "कमन कार्प (Fry) को दानामा प्रोटिनको मात्रा लगभग ४५% राखिन्छ। Fry लाई बढी प्रोटिन चाहिन्छ किनभने यो वृद्धिको चरणमा हुन्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q43", "question": "खचाखच हुनु गर्ने लागि माछाले कुन अन्नको प्रयोग गर्दछ?",
        "options": ["पचेउ", "मुख", "मिल", "भेट"], "correctIndex": 2,
        "explanation": "माछाले खचाखच (milling) गरिएको अन्न (मिल) को प्रयोग गर्छ। मिल गरिएको दाना सजिलै पच्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q44", "question": "ट्राइकोडिनोसिस (Trichodinosis) रोग माछामा के बाट लाग्छ?",
        "options": ["विषाणुबाट", "फिटोप्लाङ्कटनबाट", "दूषितबाट", "प्रोटोजोआबाट"], "correctIndex": 3,
        "explanation": "Trichodinosis रोग माछामा प्रोटोजोआ (Protozoa) परजीवी Trichodina को कारणले लाग्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q45", "question": "पोखरीको मोसाहारी माछा नियन्त्रण गर्न कुन साधनको प्रयोग अनुकूल हुन्छ?",
        "options": ["सोहन जाल", "थान्ने जाल", "बल्छी", "माथिका सबै"], "correctIndex": 3,
        "explanation": "पोखरीको मोसाहारी (unwanted) माछा नियन्त्रण गर्न सोहन जाल, थान्ने जाल र बल्छी सबैको प्रयोग गरिन्छ।", "subject": "GK"
    },
    {
        "id": "q46", "question": "माछाको लागि व्यावसायिक दाना बनाउँदा मुख्यतया के कुरालाई ध्यान दिइन्छ?",
        "options": ["भिटामिन", "कार्बोहाइड्रेट", "खनिज पदार्थ", "प्रोटीन"], "correctIndex": 3,
        "explanation": "माछाको लागि व्यावसायिक दाना बनाउँदा मुख्यतया प्रोटीनको मात्रालाई ध्यान दिइन्छ किनभने प्रोटीन माछाको वृद्धिको लागि सबैभन्दा महत्त्वपूर्ण पोषक तत्व हो।", "subject": "SCIENCE"
    },
    {
        "id": "q47", "question": "०.५ ग्राम माछाको मुरालाई डुबानी गर्दा लगभग कति तेल प्रति लिटर पानीमा कति राख्नुपर्छ?",
        "options": ["१-२ माइक्रोलिटर", "२-३ माइक्रोलिटर", "३-५ माइक्रोलिटर", "५-७ माइक्रोलिटर"], "correctIndex": 1,
        "explanation": "०.५ ग्राम माछाको मुरालाई डुबानी (dip treatment) गर्दा प्रति लिटर पानीमा २-३ माइक्रोलिटर तेल राख्नुपर्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q48", "question": "नेपालमा कुन पद्धति अनुसार सम्बन्ध वृद्धि मत्स्य पालन गरिन्छ?",
        "options": ["पोखरी कल्चर (Pond Culture)", "लामो कल्चर (Swamp Culture)", "केज फिस कल्चर (Cage Fish Culture)", "रेसवे कल्चर (Raceway Culture)"], "correctIndex": 0,
        "explanation": "नेपालमा मुख्यतया पोखरी कल्चर (Pond Culture) पद्धति अनुसार मत्स्य पालन गरिन्छ।", "subject": "GK"
    },
    {
        "id": "q49", "question": "माछामा लाग्ने Tail rot र Fin rot रोगको कारण के हो?",
        "options": ["ब्याक्टेरिया (Bacteria)", "फङ्गस (Fungus)", "भाइरस (Virus)", "परजीवी (Parasites)"], "correctIndex": 0,
        "explanation": "Tail rot र Fin rot रोग माछामा ब्याक्टेरिया (Aeromonas, Pseudomonas आदि) को कारणले लाग्छ।", "subject": "SCIENCE"
    },
    {
        "id": "q50", "question": "माछाको शारीरिक विकासका लागि कुन तत्वको बढी आवश्यकता हुन्छ?",
        "options": ["कार्बोहाइड्रेट", "प्रोटीन", "चिल्लो", "भिटामिन"], "correctIndex": 1,
        "explanation": "माछाको शारीरिक विकास र वृद्धिका लागि प्रोटीनको सबैभन्दा बढी आवश्यकता हुन्छ। माछाले आफ्नो शरीरको तौलको ३०-५०% सम्म प्रोटीन आहारमा चाहन्छ।", "subject": "SCIENCE"
    }
]

# English translations
QUESTIONS_EN = [
    {
        "id": "q1", "question": "According to current research and studies, how many species of fish are found in Nepal?",
        "options": ["1322", "202", "2322", "2622"], "correctIndex": 2,
        "explanation": "According to current research and studies, 2,322 species of fish have been found in Nepal.", "subject": "SCIENCE"
    },
    {
        "id": "q2", "question": "In which year was the Water Conservation Act enacted in Nepal?",
        "options": ["2015 AD", "2017 AD", "2020 AD", "2030 AD"], "correctIndex": 1,
        "explanation": "The Water Conservation Act was enacted in Nepal in 2017 AD.", "subject": "CONSTITUTION"
    },
    {
        "id": "q3", "question": "What is the percentage of improved and crossbred cows in Nepal?",
        "options": ["5%", "13%", "30%", "40%"], "correctIndex": 1,
        "explanation": "The percentage of improved and crossbred cows in Nepal is approximately 13%.", "subject": "GK"
    },
    {
        "id": "q4", "question": "In which year was the separate Department of Livestock and Animal Health established from the Agriculture Department?",
        "options": ["2017", "2023", "2027", "2032"], "correctIndex": 1,
        "explanation": "The separate Department of Livestock and Animal Health was established from the Agriculture Department in 2023 AD.", "subject": "GK"
    },
    {
        "id": "q5", "question": "What are the various methods of agriculture/livestock/fisheries extension?",
        "options": ["Radio and TV", "Poster, pamphlet, newspaper", "Exhibition", "All of the above"], "correctIndex": 3,
        "explanation": "For agriculture, livestock and fisheries extension, radio, TV, posters, pamphlets, newspapers and exhibitions are all used as methods.", "subject": "GK"
    },
    {
        "id": "q6", "question": "After Nepal adopted the federal system, in which year did the Local Government Operation Act come into implementation?",
        "options": ["2073 BS", "2074 BS", "2075 BS", "2076 BS"], "correctIndex": 1,
        "explanation": "After Nepal adopted the federal system, the Local Government Operation Act came into implementation in 2074 BS.", "subject": "CONSTITUTION"
    },
    {
        "id": "q7", "question": "In which article of Nepal's Constitution is the Right to Food mentioned?",
        "options": ["Article 36", "Article 44", "Article 22", "Article 24"], "correctIndex": 0,
        "explanation": "The Right to Food is mentioned in Article 36 of the Constitution of Nepal 2072.", "subject": "CONSTITUTION"
    },
    {
        "id": "q8", "question": "What is the target for fish production increase by the end of the current periodic plan?",
        "options": ["4 MT/Hact.", "6 MT/Hact.", "8 MT/Hact.", "10 MT/Hact."], "correctIndex": 1,
        "explanation": "The target for fish production increase by the end of the current periodic plan is 6 metric tons per hectare.", "subject": "GK"
    },
    {
        "id": "q9", "question": "What is the penalty for illegally selling quarantined animals?",
        "options": ["Rs. 10,000", "Rs. 25,000", "Rs. 50,000", "Rs. 1 lakh"], "correctIndex": 2,
        "explanation": "For illegally selling quarantined animals, a fine of up to Rs. 50,000 can be imposed.", "subject": "CONSTITUTION"
    },
    {
        "id": "q10", "question": "What is the share of goat meat in Nepal's total meat production?",
        "options": ["10%", "15%", "20%", "25%"], "correctIndex": 1,
        "explanation": "The contribution of goat meat in Nepal's total meat production is approximately 15%.", "subject": "GK"
    },
    {
        "id": "q11", "question": "Who appoints the feed inspector?",
        "options": ["Government of Nepal", "Provincial Government", "Local levels", "Both A and B"], "correctIndex": 3,
        "explanation": "The appointment of feed inspectors is done by both the Government of Nepal and the Provincial Governments.", "subject": "CONSTITUTION"
    },
    {
        "id": "q12", "question": "According to the Feed Material Act, 2032, which department has the main responsibility?",
        "options": ["Livestock Service Department", "Food Technology and Quality Control Department", "Agriculture Department", "Commerce Department"], "correctIndex": 1,
        "explanation": "According to the Feed Material Act, 2032, the Food Technology and Quality Control Department has the main responsibility for feed quality control.", "subject": "CONSTITUTION"
    },
    {
        "id": "q13", "question": "What is done in livestock farming using Hydroponics technology in Nepal?",
        "options": ["Producing plants in laboratory", "Producing grass on land", "Producing plants on land", "Producing grass in water"], "correctIndex": 3,
        "explanation": "In Hydroponics technology, plants are grown without soil, using only water with nutrients. In Nepal, this technology is used to produce grass for animals in water.", "subject": "SCIENCE"
    },
    {
        "id": "q14", "question": "During animal milking, how many hours per day should they not be walked more than?",
        "options": ["6", "8", "10", "12"], "correctIndex": 1,
        "explanation": "During milking, animals should not be walked more than 8 hours per day. Walking more can reduce milk production.", "subject": "SCIENCE"
    },
    {
        "id": "q15", "question": "Penta sulfate is used for which disease?",
        "options": ["Pica", "Anthrax", "Ketosis", "Tuberculosis"], "correctIndex": 1,
        "explanation": "Penta sulfate is an antibiotic used in the treatment of anthrax disease.", "subject": "SCIENCE"
    },
    {
        "id": "q16", "question": "In which disease of chicken does the body's ability to fight disease completely deteriorate?",
        "options": ["Fowl pox", "Fowl cholera", "Gumboro", "Pullorum"], "correctIndex": 2,
        "explanation": "Gumboro (Infectious Bursal Disease - IBD) destroys the bursa in chickens, completely deteriorating the body's disease-fighting capacity.", "subject": "SCIENCE"
    },
    {
        "id": "q17", "question": "In which part of the chicken does Heterakis Gallinarum reside?",
        "options": ["Small Intestine", "Caecum, Colon", "Oesophagus", "Caecum, colon, rectum"], "correctIndex": 1,
        "explanation": "Heterakis Gallinarum is a parasitic worm that resides in the caecum and colon of chickens.", "subject": "SCIENCE"
    },
    {
        "id": "q18", "question": "Lumbar Paralysis (Kushi) is caused by which parasite?",
        "options": ["Thelazia sps.", "Staria (Setaria) sps.", "Oesophagostomum", "Nematodirus"], "correctIndex": 1,
        "explanation": "Lumbar Paralysis (Kushi) is caused by parasites of the Staria (Setaria) species, which are found in cattle and buffaloes.", "subject": "SCIENCE"
    },
    {
        "id": "q19", "question": "Bladder worm refers to which of the following?",
        "options": ["Gall bladder worm", "Urinary bladder worm", "Round worm", "Tapeworm water bladder"], "correctIndex": 1,
        "explanation": "Bladder worm refers to the Cysticercus stage, which is a stage of the urinary bladder worm (Taenia).", "subject": "SCIENCE"
    },
    {
        "id": "q20", "question": "Which disease in ducks is caused by fungus?",
        "options": ["Coccidiosis", "Salmonellosis", "Aspergillosis", "None of the above"], "correctIndex": 2,
        "explanation": "Aspergillosis is a disease caused by Aspergillus fungus that affects ducks.", "subject": "SCIENCE"
    },
    {
        "id": "q21", "question": "Among the following diseases in chickens, which one is caused by a virus?",
        "options": ["E. coli", "Salmonellosis", "Marek's Disease", "Coccidiosis"], "correctIndex": 2,
        "explanation": "Marek's Disease is a viral disease in chickens. The other options are caused by bacteria or parasites.", "subject": "SCIENCE"
    },
    {
        "id": "q22", "question": "In Newcastle disease, where is bleeding seen during post-mortem?",
        "options": ["Proventriculus", "Caecum", "Skin", "Eyes"], "correctIndex": 0,
        "explanation": "In Newcastle disease, post-mortem examination of dead chickens shows bleeding in the proventriculus.", "subject": "SCIENCE"
    },
    {
        "id": "q23", "question": "For which disease was the vaccine first developed in South Asia for sheep and goats in Nepal?",
        "options": ["Enterotaxemia", "FMD", "PPR", "Foot rot"], "correctIndex": 2,
        "explanation": "The PPR (Peste des Petits Ruminants) vaccine was first developed in South Asia in Nepal. It is a serious viral disease of sheep and goats.", "subject": "SCIENCE"
    },
    {
        "id": "q24", "question": "What is the common name for Thelazia?",
        "options": ["Guinea worm", "Whip worm", "Pin worm", "Eye worm"], "correctIndex": 3,
        "explanation": "Thelazia is commonly called 'Eye worm' because it is found in the eyes of animals.", "subject": "SCIENCE"
    },
    {
        "id": "q25", "question": "White muscle disease in animals is caused by deficiency of which element?",
        "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin E"], "correctIndex": 3,
        "explanation": "White muscle disease is caused by deficiency of Vitamin E and selenium, which creates white spots in the muscles.", "subject": "SCIENCE"
    },
    {
        "id": "q26", "question": "Which strain of LSD vaccine is recommended in Nepal?",
        "options": ["Sheep pox", "Capri pox", "Neethling", "All of the above"], "correctIndex": 2,
        "explanation": "The Neethling strain of LSD (Lumpy Skin Disease) vaccine is recommended for use in Nepal.", "subject": "SCIENCE"
    },
    {
        "id": "q27", "question": "Which hormone helps maintain pregnancy in cattle and buffaloes?",
        "options": ["GnRH", "Prolactin", "Estrogen", "Progesterone"], "correctIndex": 3,
        "explanation": "Progesterone hormone controls conception and maintains the fetus in the uterus.", "subject": "SCIENCE"
    },
    {
        "id": "q28", "question": "Which of the following is NOT an indigenous buffalo breed?",
        "options": ["Lime", "Parkote", "Rhadi", "Nilirami"], "correctIndex": 3,
        "explanation": "Nilirami is not an indigenous buffalo breed. Lime, Parkote and Rhadi are indigenous buffalo breeds of Nepal.", "subject": "GK"
    },
    {
        "id": "q29", "question": "What is the fat content in maize?",
        "options": ["60%", "50%", "50%", "90%"], "correctIndex": 2,
        "explanation": "Maize contains approximately 50% fat content. It is a good source of animal feed.", "subject": "SCIENCE"
    },
    {
        "id": "q30", "question": "Which breed of chicken has been developed for multipurpose use (eggs and meat)?",
        "options": ["Black Australorp", "New Hampshire", "Giriraja", "White leg-horn"], "correctIndex": 2,
        "explanation": "Giriraja chicken is a dual-purpose breed developed in Nepal for both egg and meat production.", "subject": "GK"
    },
    {
        "id": "q31", "question": "What is the maximum percentage of urea that can be mixed when treating straw for feed?",
        "options": ["1-2%", "2-5%", "3-5%", "5-10%"], "correctIndex": 1,
        "explanation": "When treating straw with urea, a maximum of 2-5% urea can be mixed. Adding more can be harmful to animals.", "subject": "SCIENCE"
    },
    {
        "id": "q32", "question": "How many hours after showing heat signs should AI be performed in cattle/buffaloes?",
        "options": ["12-18 hours", "20-24 hours", "6-12 hours", "18-22 hours"], "correctIndex": 0,
        "explanation": "AI (Artificial Insemination) should be performed 12-18 hours after cattle/buffaloes show heat signs.", "subject": "SCIENCE"
    },
    {
        "id": "q33", "question": "What type of grass is Desmodium?",
        "options": ["Shrub grass", "Leguminous grass", "Both A and B", "Tall grass"], "correctIndex": 2,
        "explanation": "Desmodium (Dopil Dopil) is both a shrub grass and a leguminous grass.", "subject": "SCIENCE"
    },
    {
        "id": "q34", "question": "Which of the following are leguminous grasses?",
        "options": ["Desmodium, Stylo and Berseem", "Centro, White clover and Bodi", "Pea, Sheep and Joint vetch", "All of the above"], "correctIndex": 3,
        "explanation": "Desmodium, Stylo, Berseem, Centro, White clover, Bodi, Pea, Sheep and Joint vetch are all leguminous grasses.", "subject": "SCIENCE"
    },
    {
        "id": "q35", "question": "Which is the best sheep breed for wool production?",
        "options": ["Lampucchhe", "Kage", "Baruwal", "Merino"], "correctIndex": 3,
        "explanation": "Merino is internationally recognized as the best sheep breed for wool production.", "subject": "GK"
    },
    {
        "id": "q36", "question": "For developing Pakhribas black pig, which breed was used for breeding?",
        "options": ["Saulbak", "Fayun", "Yorkshire", "Tamworth"], "correctIndex": 2,
        "explanation": "Yorkshire breed pigs were used for breeding in the development of Pakhribas black pig.", "subject": "GK"
    },
    {
        "id": "q37", "question": "How many kg of seed per hectare is required for Berseem grass cultivation?",
        "options": ["10-15", "20-25", "25-30", "30-35"], "correctIndex": 1,
        "explanation": "For Berseem grass cultivation, 20-25 kg of seed per hectare is required.", "subject": "SCIENCE"
    },
    {
        "id": "q38", "question": "Within how many hours of showing heat signs should buffaloes be inseminated?",
        "options": ["0-6", "6-12", "12-18", "18-24"], "correctIndex": 2,
        "explanation": "Buffaloes should be inseminated within 12-18 hours of showing heat signs.", "subject": "SCIENCE"
    },
    {
        "id": "q39", "question": "Which method is used to supply oxygen in fish ponds?",
        "options": ["Aeration", "Pumping", "Stirring", "B and C"], "correctIndex": 0,
        "explanation": "Aeration method is used to supply oxygen in fish ponds, which increases the oxygen level by mixing air with water.", "subject": "SCIENCE"
    },
    {
        "id": "q40", "question": "Which improved fish is cultivated in Raceway with cold water in Nepal?",
        "options": ["Labeo Rohita", "Rainbow trout", "Mrigala", "Grass Carp"], "correctIndex": 1,
        "explanation": "Rainbow trout is an improved fish cultivated in Raceway with cold water in Nepal.", "subject": "GK"
    },
    {
        "id": "q41", "question": "Which fish species are suitable for cultivation in rice fields?",
        "options": ["Catla", "Rohu", "Mrigal and Catla", "All of the above"], "correctIndex": 3,
        "explanation": "Catla, Rohu and Mrigal are all suitable fish species for cultivation in rice fields. This is called 'Rice-fish farming'.", "subject": "GK"
    },
    {
        "id": "q42", "question": "What percentage of protein is kept in common carp (Fry) feed?",
        "options": ["45", "50", "55", "60"], "correctIndex": 0,
        "explanation": "Common carp (Fry) feed contains approximately 45% protein. Fry requires more protein as it is in the growth stage.", "subject": "SCIENCE"
    },
    {
        "id": "q43", "question": "Which type of grain do fish use for easy digestion?",
        "options": ["Whole grain", "Mouth grain", "Milled grain", "Wet grain"], "correctIndex": 2,
        "explanation": "Fish use milled (ground) grain which is easier to digest.", "subject": "SCIENCE"
    },
    {
        "id": "q44", "question": "Trichodinosis disease in fish is caused by what?",
        "options": ["Virus", "Phytoplankton", "Contamination", "Protozoa"], "correctIndex": 3,
        "explanation": "Trichodinosis in fish is caused by the protozoan parasite Trichodina.", "subject": "SCIENCE"
    },
    {
        "id": "q45", "question": "Which tools are suitable for controlling unwanted fish in ponds?",
        "options": ["Seine net", "Cast net", "Hook", "All of the above"], "correctIndex": 3,
        "explanation": "Seine nets, cast nets and hooks are all used for controlling unwanted fish in ponds.", "subject": "GK"
    },
    {
        "id": "q46", "question": "What is mainly considered when making commercial feed for fish?",
        "options": ["Vitamin", "Carbohydrate", "Mineral", "Protein"], "correctIndex": 3,
        "explanation": "Protein content is mainly considered when making commercial fish feed because protein is the most important nutrient for fish growth.", "subject": "SCIENCE"
    },
    {
        "id": "q47", "question": "For dip treatment of 0.5g fish fry, how much oil per liter of water should be used?",
        "options": ["1-2 microliters", "2-3 microliters", "3-5 microliters", "5-7 microliters"], "correctIndex": 1,
        "explanation": "For dip treatment of 0.5g fish fry, 2-3 microliters of oil per liter of water should be used.", "subject": "SCIENCE"
    },
    {
        "id": "q48", "question": "Which method is mainly used for fish farming in Nepal?",
        "options": ["Pond Culture", "Swamp Culture", "Cage Fish Culture", "Raceway Culture"], "correctIndex": 0,
        "explanation": "Pond Culture is the main method used for fish farming in Nepal.", "subject": "GK"
    },
    {
        "id": "q49", "question": "What causes Tail rot and Fin rot disease in fish?",
        "options": ["Bacteria", "Fungus", "Virus", "Parasites"], "correctIndex": 0,
        "explanation": "Tail rot and Fin rot in fish are caused by bacteria such as Aeromonas and Pseudomonas.", "subject": "SCIENCE"
    },
    {
        "id": "q50", "question": "Which nutrient is most needed for the physical development of fish?",
        "options": ["Carbohydrate", "Protein", "Fat", "Vitamin"], "correctIndex": 1,
        "explanation": "Protein is the most needed nutrient for the physical development and growth of fish. Fish require 30-50% protein in their diet relative to their body weight.", "subject": "SCIENCE"
    }
]


def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Save question sets
save_json(QUESTIONS_EN, "../data/en/livestock/set1.json")
save_json(QUESTIONS_NE, "../data/ne/livestock/set1.json")

# Create tests.json
tests = [
    {
        "id": "set1",
        "title": "Livestock Technician Model Set 1",
        "questionCount": 50,
        "timeLimit": 45,
        "difficulty": "Medium",
        "locked": False
    },
    {
        "id": "set2",
        "title": "Livestock Technician Model Set 2",
        "questionCount": 50,
        "timeLimit": 45,
        "difficulty": "Hard",
        "locked": True
    },
    {
        "id": "set3",
        "title": "Livestock Technician Model Set 3",
        "questionCount": 50,
        "timeLimit": 45,
        "difficulty": "Easy",
        "locked": True
    }
]

save_json(tests, "../data/en/livestock/tests.json")
save_json(tests, "../data/ne/livestock/tests.json")

print("✅ Generated livestock question sets:")
print(f"  - en/livestock/set1.json: {len(QUESTIONS_EN)} questions")
print(f"  - ne/livestock/set1.json: {len(QUESTIONS_NE)} questions")
print(f"  - tests.json created for both languages")
