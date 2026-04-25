#!/usr/bin/env python3
"""Generate extended sets 4-10 for administrative categories."""
import json, random, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_real_questions import ALL_QUESTIONS, make_json_question, make_json_question_ne, balance_questions

# NEW QUESTIONS - 40 CONSTITUTION, 30 IQ, 20 MATH, 20 SCIENCE
NEW_QUESTIONS = []

# --- 40 CONSTITUTION ---
for i, (q_en, q_ne, opts_en, opts_ne, corr, expl_en, expl_ne) in enumerate([
    ("Which part of the Constitution deals with the Directive Principles?", "संविधानको कुन भागमा नीति निर्देशक सिद्धान्तहरू छन्?", ["Part 2","Part 3","Part 4","Part 5"], ["भाग २","भाग ३","भाग ४","भाग ५"], 2, "Part 4 deals with Directive Principles.", "भाग ४ मा नीति निर्देशक सिद्धान्तहरू छन्।"),
    ("Which article deals with the Right to Education?", "शिक्षाको हक कुन धारामा छ?", ["Article 30","Article 31","Article 32","Article 33"], ["धारा ३०","धारा ३१","धारा ३२","धारा ३३"], 1, "Article 31 guarantees Right to Education.", "धारा ३१ ले शिक्षाको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Employment?", "रोजगारीको हक कुन धारामा छ?", ["Article 30","Article 32","Article 33","Article 35"], ["धारा ३०","धारा ३२","धारा ३३","धारा ३५"], 2, "Article 33 guarantees Right to Employment.", "धारा ३३ ले रोजगारीको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Health?", "स्वास्थ्यको हक कुन धारामा छ?", ["Article 33","Article 35","Article 37","Article 39"], ["धारा ३३","धारा ३५","धारा ३७","धारा ३९"], 1, "Article 35 guarantees Right to Health.", "धारा ३५ ले स्वास्थ्यको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Food Sovereignty?", "खाद्य सम्प्रभुताको हक कुन धारामा छ?", ["Article 34","Article 35","Article 36","Article 38"], ["धारा ३४","धारा ३५","धारा ३६","धारा ३८"], 2, "Article 36 guarantees Right to Food Sovereignty.", "धारा ३६ ले खाद्य सम्प्रभुताको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right of Women?", "महिलाको हक कुन धारामा छ?", ["Article 36","Article 37","Article 38","Article 40"], ["धारा ३६","धारा ३७","धारा ३८","धारा ४०"], 2, "Article 38 guarantees Rights of Women.", "धारा ३८ ले महिलाको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right of Children?", "बालबालिकाको हक कुन धारामा छ?", ["Article 37","Article 38","Article 39","Article 41"], ["धारा ३७","धारा ३८","धारा ३९","धारा ४१"], 2, "Article 39 guarantees Rights of Children.", "धारा ३९ ले बालबालिकाको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right of Dalit?", "दलितको हक कुन धारामा छ?", ["Article 38","Article 40","Article 42","Article 44"], ["धारा ३८","धारा ४०","धारा ४२","धारा ४४"], 1, "Article 40 guarantees Rights of Dalit.", "धारा ४० ले दलितको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Social Justice?", "सामाजिक न्यायको हक कुन धारामा छ?", ["Article 38","Article 40","Article 42","Article 44"], ["धारा ३८","धारा ४०","धारा ४२","धारा ४४"], 2, "Article 42 guarantees Right to Social Justice.", "धारा ४२ ले सामाजिक न्यायको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Privacy?", "गोपनीयताको हक कुन धारामा छ?", ["Article 26","Article 28","Article 30","Article 32"], ["धारा २६","धारा २८","धारा ३०","धारा ३२"], 1, "Article 28 guarantees Right to Privacy.", "धारा २८ ले गोपनीयताको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Religion?", "धर्मको हक कुन धारामा छ?", ["Article 24","Article 25","Article 26","Article 27"], ["धारा २४","धारा २५","धारा २६","धारा २७"], 1, "Article 25 guarantees Right to Religion.", "धारा २५ ले धर्मको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Information?", "सूचनाको हक कुन धारामा छ?", ["Article 25","Article 27","Article 29","Article 31"], ["धारा २५","धारा २७","धारा २९","धारा ३१"], 1, "Article 27 guarantees Right to Information.", "धारा २७ ले सूचनाको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Property?", "सम्पत्तिको हक कुन धारामा छ?", ["Article 22","Article 24","Article 26","Article 28"], ["धारा २२","धारा २४","धारा २६","धारा २८"], 2, "Article 26 guarantees Right to Property.", "धारा २६ ले सम्पत्तिको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right against Torture?", "यातनाविरुद्धको हक कुन धारामा छ?", ["Article 27","Article 29","Article 31","Article 33"], ["धारा २७","धारा २९","धारा ३१","धारा ३३"], 1, "Article 29 guarantees Right against Torture.", "धारा २९ ले यातनाविरुद्धको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right against Preventive Detention?", "निवारणात्मक निरोधविरुद्धको हक कुन धारामा छ?", ["Article 28","Article 30","Article 32","Article 34"], ["धारा २८","धारा ३०","धारा ३२","धारा ३४"], 1, "Article 30 guarantees this right.", "धारा ३० ले यो हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right against Exploitation?", "शोषणविरुद्धको हक कुन धारामा छ?", ["Article 27","Article 29","Article 31","Article 33"], ["धारा २७","धारा २९","धारा ३१","धारा ३३"], 1, "Article 29 includes this right.", "धारा २९ मा शोषणविरुद्धको हक समावेश छ।"),
    ("Which article deals with the Right to Clean Environment?", "स्वच्छ वातावरणको हक कुन धारामा छ?", ["Article 28","Article 30","Article 32","Article 34"], ["धारा २८","धारा ३०","धारा ३२","धारा ३४"], 1, "Article 30 guarantees Right to Clean Environment.", "धारा ३० ले स्वच्छ वातावरणको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Language and Culture?", "भाषा र संस्कृतिको हक कुन धारामा छ?", ["Article 30","Article 31","Article 32","Article 33"], ["धारा ३०","धारा ३१","धारा ३२","धारा ३३"], 2, "Article 32 guarantees this right.", "धारा ३२ ले भाषा र संस्कृतिको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Employment in State Bodies?", "राज्य निकायमा रोजगारीको हक कुन धारामा छ?", ["Article 32","Article 33","Article 34","Article 35"], ["धारा ३२","धारा ३३","धारा ३४","धारा ३५"], 2, "Article 34 deals with employment in state bodies.", "धारा ३४ मा राज्य निकायमा रोजगारीको हक छ।"),
    ("Which article deals with the Right to Labour?", "श्रमको हक कुन धारामा छ?", ["Article 32","Article 33","Article 34","Article 35"], ["धारा ३२","धारा ३३","धारा ३४","धारा ३५"], 2, "Article 34 guarantees Right to Labour.", "धारा ३४ ले श्रमको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Social Security?", "सामाजिक सुरक्षाको हक कुन धारामा छ?", ["Article 40","Article 41","Article 42","Article 43"], ["धारा ४०","धारा ४१","धारा ४२","धारा ४३"], 1, "Article 41 guarantees Right to Social Security.", "धारा ४१ ले सामाजिक सुरक्षाको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Justice?", "न्यायको हक कुन धारामा छ?", ["Article 18","Article 20","Article 22","Article 24"], ["धारा १८","धारा २०","धारा २२","धारा २४"], 1, "Article 20 guarantees Right to Justice.", "धारा २० ले न्यायको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right against Exile?", "निर्वासनविरुद्धको हक कुन धारामा छ?", ["Article 18","Article 20","Article 22","Article 24"], ["धारा १८","धारा २०","धारा २२","धारा २४"], 2, "Article 22 guarantees this right.", "धारा २२ ले निर्वासनविरुद्धको हक सुनिश्चित गर्छ।"),
    ("Which article deals with the Right to Constitutional Remedy?", "संवैधानिक उपचारको हक कुन धारामा छ?", ["Article 44","Article 45","Article 46","Article 48"], ["धारा ४४","धारा ४५","धारा ४६","धारा ४८"], 2, "Article 46 guarantees Right to Constitutional Remedy.", "धारा ४६ ले संवैधानिक उपचारको हक सुनिश्चित गर्छ।"),
    ("Which schedule lists the powers of the Federation?", "संघको अधिकार कुन अनुसूचीमा छ?", ["Schedule 5","Schedule 6","Schedule 7","Schedule 8"], ["अनुसूची ५","अनुसूची ६","अनुसूची ७","अनुसूची ८"], 0, "Schedule 5 lists federal powers.", "अनुसूची ५ मा संघीय अधिकारहरू छन्।"),
    ("Which schedule lists the powers of the State?", "प्रदेशको अधिकार कुन अनुसूचीमा छ?", ["Schedule 5","Schedule 6","Schedule 7","Schedule 8"], ["अनुसूची ५","अनुसूची ६","अनुसूची ७","अनुसूची ८"], 1, "Schedule 6 lists state powers.", "अनुसूची ६ मा प्रदेशीय अधिकारहरू छन्।"),
    ("Which schedule lists the powers of the Local Level?", "स्थानीय तहको अधिकार कुन अनुसूचीमा छ?", ["Schedule 5","Schedule 6","Schedule 7","Schedule 8"], ["अनुसूची ५","अनुसूची ६","अनुसूची ७","अनुसूची ८"], 2, "Schedule 7 lists local level powers.", "अनुसूची ७ मा स्थानीय तहको अधिकारहरू छन्।"),
    ("Which schedule deals with concurrent powers?", "साझा अधिकार कुन अनुसूचीमा छ?", ["Schedule 7","Schedule 8","Schedule 9","Schedule 10"], ["अनुसूची ७","अनुसूची ८","अनुसूची ९","अनुसूची १०"], 2, "Schedule 9 deals with concurrent powers.", "अनुसूची ९ मा साझा अधिकारहरू छन्।"),
    ("Which article establishes the Election Commission?", "निर्वाचन आयोग कुन धारामा स्थापना भएको छ?", ["Article 238","Article 240","Article 242","Article 245"], ["धारा २३८","धारा २४०","धारा २४२","धारा २४५"], 1, "Article 240 establishes the Election Commission.", "धारा २४० मा निर्वाचन आयोगको स्थापना छ।"),
    ("Which article establishes the Auditor General?", "महालेखापरीक्षक कुन धारामा स्थापना भएका छन्?", ["Article 238","Article 240","Article 242","Article 246"], ["धारा २३८","धारा २४०","धारा २४२","धारा २४६"], 3, "Article 246 establishes the Auditor General.", "धारा २४६ मा महालेखापरीक्षकको स्थापना छ।"),
    ("Which article establishes the National Human Rights Commission?", "राष्ट्रिय मानव अधिकार आयोग कुन धारामा स्थापना भएको छ?", ["Article 280","Article 282","Article 285","Article 290"], ["धारा २८०","धारा २८२","धारा २८५","धारा २९०"], 1, "Article 282 establishes NHRC.", "धारा २८२ मा राष्ट्रिय मानव अधिकार आयोगको स्थापना छ।"),
    ("Which article deals with the formation of the Judicial Council?", "न्यायिक परिषद् गठन कुन धारामा छ?", ["Article 145","Article 150","Article 153","Article 155"], ["धारा १४५","धारा १५०","धारा १५३","धारा १५५"], 2, "Article 153 deals with the Judicial Council.", "धारा १५३ मा न्यायिक परिषद्को व्यवस्था छ।"),
    ("Which article deals with the oath of office by the President?", "राष्ट्रपतिको शपथ कुन धारामा छ?", ["Article 60","Article 62","Article 64","Article 66"], ["धारा ६०","धारा ६२","धारा ६४","धारा ६६"], 1, "Article 62 deals with the President's oath.", "धारा ६२ मा राष्ट्रपतिको शपथको व्यवस्था छ।"),
    ("Which article deals with the oath of office by the Prime Minister?", "प्रधानमन्त्रीको शपथ कुन धारामा छ?", ["Article 76","Article 78","Article 80","Article 82"], ["धारा ७६","धारा ७८","धारा ८०","धारा ८२"], 1, "Article 78 deals with the PM's oath.", "धारा ७८ मा प्रधानमन्त्रीको शपथको व्यवस्था छ।"),
    ("Which article deals with the oath of office by Judges?", "न्यायाधीशको शपथ कुन धारामा छ?", ["Article 135","Article 137","Article 139","Article 141"], ["धारा १३५","धारा १३७","धारा १३९","धारा १४१"], 1, "Article 137 deals with judges' oath.", "धारा १३७ मा न्यायाधीशको शपथको व्यवस्था छ।"),
    ("Which article deals with the formation of the Judicial Service Commission?", "न्यायिक सेवा आयोग गठन कुन धारामा छ?", ["Article 150","Article 152","Article 154","Article 156"], ["धारा १५०","धारा १५२","धारा १५४","धारा १५६"], 2, "Article 154 deals with Judicial Service Commission.", "धारा १५४ मा न्यायिक सेवा आयोगको व्यवस्था छ।"),
    ("Which article deals with the National Natural Resources and Fiscal Commission?", "राष्ट्रिय प्राकृतिक स्रोत तथा वित्त आयोग कुन धारामा छ?", ["Article 245","Article 248","Article 250","Article 255"], ["धारा २४५","धारा २४८","धारा २५०","धारा २५५"], 2, "Article 250 establishes NNRFC.", "धारा २५० मा यो आयोगको स्थापना छ।"),
    ("Which article deals with the National Women Commission?", "राष्ट्रिय महिला आयोग कुन धारामा छ?", ["Article 260","Article 262","Article 265","Article 270"], ["धारा २६०","धारा २६२","धारा २६५","धारा २७०"], 1, "Article 262 deals with National Women Commission.", "धारा २६२ मा राष्ट्रिय महिला आयोगको व्यवस्था छ।"),
    ("Which article deals with the National Dalit Commission?", "राष्ट्रिय दलित आयोग कुन धारामा छ?", ["Article 260","Article 262","Article 264","Article 266"], ["धारा २६०","धारा २६२","धारा २६४","धारा २६६"], 2, "Article 264 deals with National Dalit Commission.", "धारा २६४ मा राष्ट्रिय दलित आयोगको व्यवस्था छ।"),
    ("Which article deals with the Madhesi Commission?", "मधेशी आयोग कुन धारामा छ?", ["Article 264","Article 266","Article 268","Article 270"], ["धारा २६४","धारा २६६","धारा २६८","धारा २७०"], 1, "Article 266 deals with Madhesi Commission.", "धारा २६६ मा मधेशी आयोगको व्यवस्था छ।"),
    ("Which article deals with the Tharu Commission?", "थारु आयोग कुन धारामा छ?", ["Article 264","Article 266","Article 268","Article 270"], ["धारा २६४","धारा २६६","धारा २६८","धारा २७०"], 2, "Article 268 deals with Tharu Commission.", "धारा २६८ मा थारु आयोगको व्यवस्था छ।"),
    ("Which article deals with the Inclusive Commission?", "समावेशी आयोग कुन धारामा छ?", ["Article 264","Article 266","Article 268","Article 270"], ["धारा २६४","धारा २६६","धारा २६८","धारा २७०"], 3, "Article 270 deals with Inclusive Commission.", "धारा २७० मा समावेशी आयोगको व्यवस्था छ।"),
]):
    NEW_QUESTIONS.append({"q_en": q_en, "q_ne": q_ne, "options_en": opts_en, "options_ne": opts_ne, "correct": corr, "explanation_en": expl_en, "explanation_ne": expl_ne, "subject": "CONSTITUTION"})

# --- 30 IQ ---
for i, (q_en, q_ne, opts_en, opts_ne, corr, expl_en, expl_ne) in enumerate([
    ("What is the next number: 2, 6, 12, 20, 30, ?", "अर्को संख्या के हो: २, ६, १२, २०, ३०, ?", ["38","40","42","44"], ["३८","४०","४२","४४"], 2, "42 (n times (n+1): 1x2=2, 2x3=6, etc).", "४२ (n गुणा (n+१): १x२=२, २x३=६, आदि)।"),
    ("What is the next number: 1, 8, 27, 64, 125, ?", "अर्को संख्या के हो: १, ८, २७, ६४, १२५, ?", ["200","216","225","250"], ["२००","२१६","२२५","२५०"], 1, "216 (cubes: 1 cubed, 2 cubed, etc).", "२१६ (घन: १ घन, २ घन, आदि)।"),
    ("What is the next number: 1, 2, 6, 24, 120, ?", "अर्को संख्या के हो: १, २, ६, २४, १२०, ?", ["600","720","840","960"], ["६००","७२०","८४०","९६०"], 1, "720 (factorials).", "७२० (फ्याक्टोरियल)।"),
    ("What is the next number: 5, 11, 23, 47, 95, ?", "अर्को संख्या के हो: ५, ११, २३, ४७, ९५, ?", ["180","191","200","210"], ["१८०","१९१","२००","२१०"], 1, "191 (times 2 plus 1 each time).", "१९१ (हरेक पटक गुणा २ प्लस १)।"),
    ("What is the next number: 0, 1, 1, 2, 3, 5, 8, 13, ?", "अर्को संख्या के हो: ०, १, १, २, ३, ५, ८, १३, ?", ["18","20","21","22"], ["१८","२०","२१","२२"], 2, "21 (Fibonacci).", "२१ (फिबोनाक्की)।"),
    ("Complete: AZ, BY, CX, DW, ?", "पूरा गर्नुहोस्: AZ, BY, CX, DW, ?", ["EV","EU","FV","FU"], ["EV","EU","FV","FU"], 0, "EV (A to Z, B to Y, etc).", "EV (A देखि Z, B देखि Y, आदि)।"),
    ("Complete: AB, DE, GH, JK, ?", "पूरा गर्नुहोस्: AB, DE, GH, JK, ?", ["LM","MN","NO","OP"], ["LM","MN","NO","OP"], 1, "MN (skip one letter pair each time).", "MN (हरेक पटक एउटा अक्षर जोडी छोड्दै)।"),
    ("If WATER is coded as YCVGT, what is coded as HKNUG?", "यदि WATER लाई YCVGT कोड गरिएको छ भने HKNUG ले के कोड गर्छ?", ["FILER","FILTER","FALTER","FOLDER"], ["FILER","FILTER","FALTER","FOLDER"], 1, "FILTER (plus 2 each letter).", "FILTER (प्रत्येक अक्षर +२)।"),
    ("If TABLE is coded as UBCMF, what is CHAIR coded as?", "यदि TABLE लाई UBCMF कोड गरिएको छ भने CHAIR लाई के कोड गरिन्छ?", ["DIBJS","DIGKS","DIBJS","DIBJT"], ["DIBJS","DIGKS","DIBJS","DIBJT"], 0, "DIBJS (plus 1 each letter).", "DIBJS (प्रत्येक अक्षर +१)।"),
    ("Find the odd one: Keyboard, Mouse, Monitor, CPU", "फरक चिन्नुहोस्: कीबोर्ड, माउस, मनिटर, CPU", ["Keyboard","Mouse","Monitor","CPU"], ["कीबोर्ड","माउस","मनिटर","CPU"], 3, "CPU is internal, others are peripherals.", "CPU आन्तरिक हो, अरू बाह्य उपकरण हुन्।"),
    ("Find the odd one: Triangle, Square, Pentagon, Circle", "फरक चिन्नुहोस्: त्रिकोण, वर्ग, पञ्चभुज, वृत्त", ["Triangle","Square","Pentagon","Circle"], ["त्रिकोण","वर्ग","पञ्चभुज","वृत्त"], 3, "Circle has no sides, others are polygons.", "वृत्तमा कुनै भुजा छैन, अरू बहुभुज हुन्।"),
    ("Find the odd one: Mercury, Venus, Earth, Pluto", "फरक चिन्नुहोस्: बुध, शुक्र, पृथ्वी, प्लुटो", ["Mercury","Venus","Earth","Pluto"], ["बुध","शुक्र","पृथ्वी","प्लुटो"], 3, "Pluto is a dwarf planet.", "प्लुटो बौन ग्रह हो।"),
    ("If 12 x 8 = 20, 15 x 7 = 22, what is 18 x 5?", "यदि १२ x ८ = २०, १५ x ७ = २२ भने १८ x ५ = ?", ["20","22","23","25"], ["२०","२२","२३","२५"], 2, "23 (a plus b: 12+8=20).", "२३ (a+b: १२+८=२०)।"),
    ("Raju is 5th from left and 8th from right. How many total?", "राजु बायाँबाट ५औं र दायाँबाट ८औं छ। कुल कति जना?", ["11","12","13","14"], ["११","१२","१३","१४"], 1, "12 (5+8-1=12).", "१२ (५+८-१=१२)।"),
    ("A is B's brother. B is C's sister. C is D's father. What is D to A?", "A, B को भाइ हो। B, C को बहिनी हो। C, D को बुबा हुन्। D ले A लाई के भन्छ?", ["Brother","Sister","Nephew or Niece","Father"], ["भाइ","बहिनी","भतिजा/भतिजी","बुबा"], 2, "Nephew or Niece.", "भतिजा वा भतिजी।"),
    ("If DOG = 26 (4+15+7), what is CAT?", "यदि DOG = २६ (४+१५+७) भने CAT = ?", ["20","22","24","26"], ["२०","२२","२४","२६"], 2, "24 (3+1+20=24).", "२४ (३+१+२०=२४)।"),
    ("What is the next term: Z1, Y2, X3, W4, ?", "अर्को पद के हो: Z1, Y2, X3, W4, ?", ["V5","V6","U5","U6"], ["V5","V6","U5","U6"], 0, "V5 (reverse alphabet + increasing number).", "V5 (उल्टो अक्षरमाला + बढ्दो संख्या)।"),
    ("If 2 pencils cost Rs. 4, what is the cost of 5 pencils?", "यदि २ वटा पेन्सिलको मूल्य रु. ४ भने ५ वटाको मूल्य कति?", ["8","9","10","12"], ["८","९","१०","१२"], 2, "Rs. 10 (each pencil = Rs. 2).", "रु. १० (प्रति पेन्सिल रु. २)।"),
    ("What is the missing number: 4, 9, 16, 25, ?, 49", "असामी संख्या के हो: ४, ९, १६, २५, ?, ४९", ["30","32","36","40"], ["३०","३२","३६","४०"], 2, "36 (squares: 2 squared to 7 squared).", "३६ (वर्ग: २ देखि ७ को वर्ग)।"),
    ("Complete: 8 : 64 :: 9 : ?", "पूरा गर्नुहोस्: ८ : ६४ :: ९ : ?", ["72","80","81","90"], ["७२","८०","८१","९०"], 2, "81 (square of 9).", "८१ (९ को वर्ग)।"),
    ("Complete: 3 : 27 :: 4 : ?", "पूरा गर्नुहोस्: ३ : २७ :: ४ : ?", ["32","48","64","81"], ["३२","४८","६४","८१"], 2, "64 (cube: 3 cubed = 27, 4 cubed = 64).", "६४ (घन: ३ घन=२७, ४ घन=६४)।"),
    ("What comes next: J, F, M, A, M, J, J, ?", "अर्को के आउँछ: J, F, M, A, M, J, J, ?", ["A","S","O","N"], ["A","S","O","N"], 0, "A (first letters of months).", "A (महिनाको पहिलो अक्षर)।"),
    ("Which is heavier: 1 kg iron or 1 kg cotton?", "कुन भारी छ: १ केजी फलाम वा १ केजी कपास?", ["Iron","Cotton","Both same","Cannot say"], ["फलाम","कपास","दुवै बराबर","भन्न सकिँदैन"], 2, "Both are 1 kg.", "दुवै १ केजी हुन्।"),
    ("If yesterday was Tuesday, what day is tomorrow?", "यदि हिजो मंगलबार थियो भने भोलि के दिन हो?", ["Tuesday","Wednesday","Thursday","Friday"], ["मंगलबार","बुधबार","बिहीबार","शुक्रबार"], 2, "Thursday (today=Wednesday, tomorrow=Thursday).", "बिहीबार (आज=बुधबार, भोलि=बिहीबार)।"),
    ("A clock shows 3:15. What is the angle between hour and minute hands?", "घडीमा ३:१५ देखाउँछ। घण्टा र मिनेटको सुईबीच कोण कति हुन्छ?", ["0 degrees","7.5 degrees","15 degrees","30 degrees"], ["०°","७.५°","१५°","३०°"], 1, "7.5 degrees (hour hand moves 0.5 deg per minute).", "७.५° (घण्टा सुई ०.५° प्रति मिनेट)।"),
    ("How many times do clock hands overlap in 12 hours?", "१२ घण्टामा घडीको सुई कति पटक मिल्छ?", ["10","11","12","13"], ["१०","११","१२","१३"], 1, "11 times.", "११ पटक।"),
    ("If 6 monkeys take 6 minutes to eat 6 bananas, how many minutes for 30 monkeys to eat 30 bananas?", "यदि ६ वटा बाँदरले ६ वटा केरा खान ६ मिनेट लगाउँछन् भने ३० वटा बाँदरले ३० वटा केरा खान कति मिनेट लगाउँछन्?", ["6","10","30","36"], ["६","१०","३०","३६"], 0, "6 minutes (each monkey eats 1 banana in 6 minutes).", "६ मिनेट (प्रत्येक बाँदरले १ केरा खान ६ मिनेट)।"),
    ("What is the smallest 3-digit number divisible by 3?", "३ ले विभाज्य हुने सबैभन्दा सानो ३ अंकको संख्या कुन हो?", ["100","101","102","103"], ["१००","१०१","१०२","१०३"], 2, "102 (1+0+2=3, divisible by 3).", "१०२ (१+०+२=३, ३ ले विभाज्य)।"),
    ("Complete: Eye is to Sight as Ear is to ?", "सम्बन्ध पूरा गर्नुहोस्: आँखा : दृष्टि :: कान : ?", ["Sound","Hear","Listen","Noise"], ["आवाज","सुन्न","सुन्ने","हल्ला"], 1, "Hear.", "सुन्न।"),
    ("Complete: Pen is to Write as Knife is to ?", "सम्बन्ध पूरा गर्नुहोस्: कलम : लेख्न :: चाकु : ?", ["Cut","Sharp","Food","Kitchen"], ["काट्न","धारिलो","खाना","भान्सा"], 0, "Cut.", "काट्न।"),
    ("If 1st January is Sunday, what day is 1st February?", "यदि जनवरी १ आइतबार हो भने फेब्रुअरी १ के दिन हो?", ["Sunday","Monday","Tuesday","Wednesday"], ["आइतबार","सोमबार","मंगलबार","बुधबार"], 3, "Wednesday (January has 31 days = 4 weeks + 3 days).", "बुधबार (जनवरीमा ३१ दिन = ४ हप्ता + ३ दिन)।"),
    ("What is the next letter: B, D, G, K, ?", "अर्को अक्षर के हो: B, D, G, K, ?", ["N","O","P","Q"], ["N","O","P","Q"], 2, "P (gaps: plus 2, plus 3, plus 4, plus 5).", "P (अन्तर: +२, +३, +४, +५)।"),
    ("What is the next number: 81, 27, 9, 3, ?", "अर्को संख्या के हो: ८१, २७, ९, ३, ?", ["0","1","2","3"], ["०","१","२","३"], 1, "1 (divide by 3 each time).", "१ (हरेक पटक ÷३)।"),
    ("In a code, CAT = 3120, DOG = 4157. What is BAT?", "एउटा कोडमा CAT = ३१२०, DOG = ४१५७ भने BAT = ?", ["2120","2121","2119","2100"], ["२१२०","२१२१","२११९","२१००"], 0, "2120 (B=2, A=1, T=20).", "२१२० (B=२, A=१, T=२०)।"),
    ("If South-East becomes North-West, what does North become?", "यदि दक्षिण-पूर्व उत्तर-पश्चिम बन्यो भने उत्तर के बन्छ?", ["South","East","West","North-East"], ["दक्षिण","पूर्व","पश्चिम","उत्तर-पूर्व"], 0, "South (180 degree rotation).", "दक्षिण (१८०° घुमाइ)।"),
    ("A man walks 5 km north, then 3 km east, then 5 km south. How far from start?", "एक मान्छेले ५ कि.मी. उत्तर, ३ कि.मी. पूर्व, ५ कि.मी. दक्षिण हिँड्छ। सुरुबाट कति टाढा?", ["3 km","5 km","8 km","13 km"], ["३ कि.मी.","५ कि.मी.","८ कि.मी.","१३ कि.मी."], 0, "3 km (north and south cancel out).", "३ कि.मी. (उत्तर र दक्षिण एकआपसमा मेटिन्छ)।"),
]):
    NEW_QUESTIONS.append({"q_en": q_en, "q_ne": q_ne, "options_en": opts_en, "options_ne": opts_ne, "correct": corr, "explanation_en": expl_en, "explanation_ne": expl_ne, "subject": "IQ"})

# --- 20 MATH ---
for i, (q_en, q_ne, opts_en, opts_ne, corr, expl_en, expl_ne) in enumerate([
    ("What is 15% of 300?", "३०० को १५% कति हुन्छ?", ["30","40","45","50"], ["३०","४०","४५","५०"], 2, "45.", "४५।"),
    ("What is the average of 15, 25, 35, 45?", "१५, २५, ३५, ४५ को औसत कति हुन्छ?", ["25","30","35","40"], ["२५","३०","३५","४०"], 1, "30 ((15+25+35+45)/4 = 120/4 = 30).", "३० ((१५+२५+३५+४५)/४ = १२०/४ = ३०)।"),
    ("If a = 2b and b = 3c, what is a:c?", "यदि a = 2b र b = 3c भने a:c कति हुन्छ?", ["2:3","3:2","6:1","1:6"], ["२:३","३:२","६:१","१:६"], 2, "6:1 (a = 2x3c = 6c).", "६:१ (a = २x३c = ६c)।"),
    ("What is the sum of first 10 natural numbers?", "पहिलो १० प्राकृतिक संख्याको योग कति हुन्छ?", ["45","50","55","60"], ["४५","५०","५५","६०"], 2, "55 (n(n+1)/2 = 10x11/2 = 55).", "५५ (n(n+1)/२ = १०x११/२ = ५५)।"),
    ("What is the sum of first 10 odd numbers?", "पहिलो १० विषम संख्याको योग कति हुन्छ?", ["81","90","100","121"], ["८१","९०","१००","१२१"], 2, "100 (n squared = 10 squared = 100).", "१०० (n वर्ग = १० वर्ग = १००)।"),
    ("What is the area of a triangle with base 10 and height 8?", "आधार १० र उचाइ ८ भएको त्रिकोणको क्षेत्रफल कति हुन्छ?", ["20","30","40","50"], ["२०","३०","४०","५०"], 2, "40 (half x base x height = half x 10 x 8 = 40).", "४० (आधा x आधार x उचाइ = आधा x १० x ८ = ४०)।"),
    ("What is the diagonal of a square with side 10?", "भुजा १० भएको वर्गको विकर्ण कति हुन्छ?", ["10 root 2","20","15","10"], ["१०√२","२०","१५","१०"], 0, "10 root 2 (diagonal = side x root 2).", "१०√२ (विकर्ण = भुजा x √२)।"),
    ("If x + 1/x = 2, what is x squared + 1/x squared?", "यदि x + 1/x = २ भने x वर्ग + 1/x वर्ग कति हुन्छ?", ["2","3","4","5"], ["२","३","४","५"], 0, "2 (square both sides: 4 = x squared + 2 + 1/x squared).", "२ (दुवै पटक वर्ग: ४ = x वर्ग + २ + 1/x वर्ग)।"),
    ("What is 2 to the power 5?", "२ को घात ५ कति हुन्छ?", ["16","24","32","64"], ["१६","२४","३२","६४"], 2, "32.", "३२।"),
    ("What is 3 to the power 4?", "३ को घात ४ कति हुन्छ?", ["27","64","81","100"], ["२७","६४","८१","१००"], 2, "81.", "८१।"),
    ("What is log base 2 of 32?", "log आधार २ को ३२ कति हुन्छ?", ["4","5","6","8"], ["४","५","६","८"], 1, "5 (2 to the power 5 = 32).", "५ (२ घात ५ = ३२)।"),
    ("What is the remainder when 17 is divided by 5?", "१७ लाई ५ ले भाग गर्दा बाँकी के हुन्छ?", ["1","2","3","4"], ["१","२","३","४"], 1, "2 (17 = 5x3 + 2).", "२ (१७ = ५x३ + २)।"),
    ("What is the HCF of 36 and 48?", "३६ र ४८ को महत्तम समापवर्तक कति हुन्छ?", ["6","12","18","24"], ["६","१२","१८","२४"], 1, "12.", "१२।"),
    ("What is the LCM of 8 and 12?", "८ र १२ को लघुत्तम समापवर्त्य कति हुन्छ?", ["12","24","36","48"], ["१२","२४","३६","४८"], 1, "24.", "२४।"),
    ("If a shirt costs Rs. 240 after 20% discount, what was the original price?", "यदि एउटा सर्ट २०% छुटपछि रु. २४० मा पाइन्छ भने मूल मूल्य कति थियो?", ["Rs. 280","Rs. 300","Rs. 320","Rs. 360"], ["रु. २८०","रु. ३००","रु. ३२०","रु. ३६०"], 1, "Rs. 300 (240 = 80% of original).", "रु. ३०० (२४० = मूल मूल्यको ८०%)।"),
    ("What is 3/4 of 1/2 of 80?", "८० को १/२ को ३/४ कति हुन्छ?", ["20","30","40","60"], ["२०","३०","४०","६०"], 1, "30 (80 x 1/2 = 40, 40 x 3/4 = 30).", "३० (८० x १/२ = ४०, ४० x ३/४ = ३०)।"),
    ("If the ratio of boys to girls is 3:2 and there are 30 students, how many boys?", "यदि केटा र केटीको अनुपात ३:२ छ र ३० जना विद्यार्थी छन् भने कति जना केटा?", ["12","15","18","20"], ["१२","१५","१८","२०"], 2, "18 (3/5 x 30 = 18).", "१८ (३/५ x ३० = १८)।"),
    ("What is the next prime number after 13?", "१३ पछिको अर्को अभाज्य संख्या कुन हो?", ["14","15","16","17"], ["१४","१५","१६","१७"], 3, "17.", "१७।"),
    ("What is the sum of angles in a triangle?", "त्रिकोणका कोणहरूको योग कति हुन्छ?", ["90 deg","180 deg","270 deg","360 deg"], ["९०°","१८०°","२७०°","३६०°"], 1, "180 degrees.", "१८०°।"),
    ("What is the sum of angles in a quadrilateral?", "चतुर्भुजका कोणहरूको योग कति हुन्छ?", ["180 deg","270 deg","360 deg","450 deg"], ["१८०°","२७०°","३६०°","४५०°"], 2, "360 degrees.", "३६०°।"),
]):
    NEW_QUESTIONS.append({"q_en": q_en, "q_ne": q_ne, "options_en": opts_en, "options_ne": opts_ne, "correct": corr, "explanation_en": expl_en, "explanation_ne": expl_ne, "subject": "MATH"})

# --- 20 SCIENCE ---
for i, (q_en, q_ne, opts_en, opts_ne, corr, expl_en, expl_ne) in enumerate([
    ("Which gas is known as laughing gas?", "कुन ग्यासलाई हाँस्ने ग्यास भनिन्छ?", ["Nitrogen","Nitrous Oxide","Carbon Dioxide","Helium"], ["नाइट्रोजन","नाइट्रस अक्साइड","कार्बन डाइअक्साइड","हिलियम"], 1, "Nitrous Oxide (N2O).", "नाइट्रस अक्साइड (N2O)।"),
    ("Which gas is used in fire extinguishers?", "आगो निभाउने यन्त्रमा कुन ग्यास प्रयोग गरिन्छ?", ["Oxygen","Carbon Dioxide","Nitrogen","Hydrogen"], ["अक्सिजन","कार्बन डाइअक्साइड","नाइट्रोजन","हाइड्रोजन"], 1, "Carbon Dioxide.", "कार्बन डाइअक्साइड।"),
    ("Which metal is liquid at room temperature?", "कोठाको तापक्रममा तरल हुने धातु कुन हो?", ["Iron","Copper","Mercury","Gold"], ["फलाम","तामा","पारो","सुन"], 2, "Mercury.", "पारो।"),
    ("What is the main component of natural gas?", "प्राकृतिक ग्यासको मुख्य घटक के हो?", ["Ethane","Propane","Methane","Butane"], ["इथेन","प्रोपेन","मिथेन","ब्युटेन"], 2, "Methane.", "मिथेन।"),
    ("What is the chemical symbol of gold?", "सुनको रासायनिक चिन्ह के हो?", ["Go","Gd","Au","Ag"], ["Go","Gd","Au","Ag"], 2, "Au (from Latin Aurum).", "Au (ल्याटिन Aurum बाट)।"),
    ("What is the chemical symbol of silver?", "चाँदीको रासायनिक चिन्ह के हो?", ["Si","Sv","Ag","Au"], ["Si","Sv","Ag","Au"], 2, "Ag (from Latin Argentum).", "Ag (ल्याटिन Argentum बाट)।"),
    ("What is the chemical symbol of iron?", "फलामको रासायनिक चिन्ह के हो?", ["Ir","In","Fe","Fn"], ["Ir","In","Fe","Fn"], 2, "Fe (from Latin Ferrum).", "Fe (ल्याटिन Ferrum बाट)।"),
    ("What is the chemical symbol of sodium?", "सोडियमको रासायनिक चिन्ह के हो?", ["So","Sd","Na","Sn"], ["So","Sd","Na","Sn"], 2, "Na (from Latin Natrium).", "Na (ल्याटिन Natrium बाट)।"),
    ("What is the chemical symbol of potassium?", "पोटासियमको रासायनिक चिन्ह के हो?", ["Po","Pt","K","Ps"], ["Po","Pt","K","Ps"], 2, "K (from Latin Kalium).", "K (ल्याटिन Kalium बाट)।"),
    ("Which vitamin is produced when skin is exposed to sunlight?", "छाला घाममा राख्दा कुन भिटामिन उत्पादन हुन्छ?", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"], ["भिटामिन A","भिटामिन B","भिटामिन C","भिटामिन D"], 3, "Vitamin D.", "भिटामिन D।"),
    ("Which vitamin is found in citrus fruits?", "सिट्रस फलमा कुन भिटामिन पाइन्छ?", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"], ["भिटामिन A","भिटामिन B","भिटामिन C","भिटामिन D"], 2, "Vitamin C.", "भिटामिन C।"),
    ("Which vitamin deficiency causes scurvy?", "कुन भिटामिनको कमीले स्कर्भी रोग हुन्छ?", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"], ["भिटामिन A","भिटामिन B","भिटामिन C","भिटामिन D"], 2, "Vitamin C deficiency causes scurvy.", "भिटामिन C को कमीले स्कर्भी हुन्छ।"),
    ("Which vitamin deficiency causes rickets?", "कुन भिटामिनको कमीले रिकेट्स रोग हुन्छ?", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"], ["भिटामिन A","भिटामिन B","भिटामिन C","भिटामिन D"], 3, "Vitamin D deficiency causes rickets.", "भिटामिन D को कमीले रिकेट्स हुन्छ।"),
    ("Which vitamin deficiency causes night blindness?", "कुन भिटामिनको कमीले रातो अन्धोपन हुन्छ?", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D"], ["भिटामिन A","भिटामिन B","भिटामिन C","भिटामिन D"], 0, "Vitamin A deficiency causes night blindness.", "भिटामिन A को कमीले रातो अन्धोपन हुन्छ।"),
    ("What is the main function of red blood cells?", "रातो रगत कोशिकाको मुख्य काम के हो?", ["Fight infection","Transport oxygen","Clot blood","Produce antibodies"], ["सङ्क्रमणसँग लड्ने","अक्सिजन ओसारपसार गर्ने","रगत जमाउने","एन्टिबडी उत्पादन गर्ने"], 1, "Transport oxygen.", "अक्सिजन ओसारपसार गर्ने।"),
    ("What is the main function of white blood cells?", "सेतो रगत कोशिकाको मुख्य काम के हो?", ["Transport oxygen","Fight infection","Clot blood","Carry nutrients"], ["अक्सिजन ओसारपसार","सङ्क्रमणसँग लड्ने","रगत जमाउने","पोषक तत्व बोक्ने"], 1, "Fight infection.", "सङ्क्रमणसँग लड्ने।"),
    ("What is the main function of platelets?", "प्लेटलेटको मुख्य काम के हो?", ["Transport oxygen","Fight infection","Clot blood","Carry nutrients"], ["अक्सिजन ओसारपसार","सङ्क्रमणसँग लड्ने","रगत जमाउने","पोषक तत्व बोक्ने"], 2, "Clot blood.", "रगत जमाउने।"),
    ("Which part of the brain controls balance?", "दिमागको कुन भागले सन्तुलन नियन्त्रण गर्छ?", ["Cerebrum","Cerebellum","Medulla","Thalamus"], ["सेरिब्रम","सेरिबेलम","मेडुला","थालामस"], 1, "Cerebellum.", "सेरिबेलम।"),
    ("Which part of the brain controls breathing?", "दिमागको कुन भागले श्वास नियन्त्रण गर्छ?", ["Cerebrum","Cerebellum","Medulla","Thalamus"], ["सेरिब्रम","सेरिबेलम","मेडुला","थालामस"], 2, "Medulla oblongata.", "मेडुला अब्लोङ्गाटा।"),
    ("What is the largest muscle in the human body?", "मानव शरीरको सबैभन्दा ठूलो मांसपेशी कुन हो?", ["Biceps","Triceps","Gluteus maximus","Quadriceps"], ["बाइसेप्स","ट्राइसेप्स","ग्लुटियस म्याक्सिमस","क्वाड्रिसेप्स"], 2, "Gluteus maximus.", "ग्लुटियस म्याक्सिमस।"),
]):
    NEW_QUESTIONS.append({"q_en": q_en, "q_ne": q_ne, "options_en": opts_en, "options_ne": opts_ne, "correct": corr, "explanation_en": expl_en, "explanation_ne": expl_ne, "subject": "SCIENCE"})

print(f"Added {len(NEW_QUESTIONS)} new questions")

# Combine with existing
all_q = ALL_QUESTIONS + NEW_QUESTIONS
print(f"Total question pool: {len(all_q)}")

# Count by subject
from collections import Counter
subjects = Counter(q["subject"] for q in all_q)
print("By subject:", dict(subjects))

# Build sets 4-10 for adhikrit, kharidar, police, subbha (4 categories x 7 sets = 28 sets)
def build_extended_set(all_questions, set_num, cat_idx, total_cats=4):
    targets = {"GK": 39, "CONSTITUTION": 4, "SCIENCE": 4, "IQ": 2, "MATH": 1}
    by_subject = {"GK": [], "IQ": [], "MATH": [], "SCIENCE": [], "CONSTITUTION": []}
    for q in all_questions:
        sub = q["subject"]
        if sub in by_subject:
            by_subject[sub].append(q)
    
    # Fixed seed for consistent base ordering
    random.seed(999)
    for sub in by_subject:
        random.shuffle(by_subject[sub])
    
    result = []
    for sub, count in targets.items():
        sub_list = by_subject[sub]
        global_idx = cat_idx * 10 + (set_num - 1)
        offset = (global_idx * count) % len(sub_list)
        picked = []
        i = 0
        while len(picked) < count:
            picked.append(sub_list[(offset + i) % len(sub_list)])
            i += 1
        result.extend(picked)
    
    # Shuffle per set
    random.seed(42 + set_num * 7 + cat_idx * 13)
    random.shuffle(result)
    result = balance_questions(result)
    return result

# Generate for each category
CATEGORIES = ["adhikrit", "kharidar", "police", "subbha"]
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

for cat_idx, cat in enumerate(CATEGORIES):
    for set_num in range(4, 11):
        questions = build_extended_set(all_q, set_num, cat_idx)
        en = [make_json_question(q, i+1) for i, q in enumerate(questions)]
        ne = [make_json_question_ne(q, i+1) for i, q in enumerate(questions)]
        
        en_path = os.path.join(BASE_DIR, cat, f"set{set_num}.json")
        ne_path = os.path.join(BASE_DIR, cat, f"set{set_num}_ne.json")
        
        os.makedirs(os.path.dirname(en_path), exist_ok=True)
        with open(en_path, "w", encoding="utf-8") as f:
            json.dump(en, f, ensure_ascii=False, indent=2)
        with open(ne_path, "w", encoding="utf-8") as f:
            json.dump(ne, f, ensure_ascii=False, indent=2)
        
        print(f"Generated {cat}/set{set_num} ({len(questions)} questions)")

print("Done generating extended admin sets!")
