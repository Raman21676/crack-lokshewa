#!/usr/bin/env python3
import json, random, os

random.seed(42)

NURSING_Q = [
    # Anatomy & Physiology (20)
    ("How many bones are in the adult human body?", ["206","208","210","212"], 0, "Adult human body has 206 bones.", "Anatomy"),
    ("What is the largest organ in the human body?", ["Liver","Brain","Skin","Heart"], 2, "Skin is the largest organ.", "Anatomy"),
    ("How many chambers does the human heart have?", ["2","3","4","5"], 2, "Human heart has 4 chambers.", "Anatomy"),
    ("What is the normal adult heart rate per minute?", ["40-60","60-100","100-120","120-140"], 1, "Normal heart rate is 60-100 bpm.", "Anatomy"),
    ("What is the normal body temperature?", ["35.5°C","36.5°C","37°C","38°C"], 2, "Normal body temperature is approximately 37°C (98.6°F).", "Anatomy"),
    ("What is the normal blood pressure range?", ["80/50","90/60","120/80","140/90"], 2, "Normal BP is around 120/80 mmHg.", "Anatomy"),
    ("How many lobes does the human brain have?", ["2","3","4","5"], 2, "The brain has 4 lobes: frontal, parietal, temporal, occipital.", "Anatomy"),
    ("What is the function of the kidneys?", ["Digest food","Filter blood and produce urine","Pump blood","Produce hormones only"], 1, "Kidneys filter blood and produce urine.", "Anatomy"),
    ("How many teeth does an adult human have?", ["28","30","32","34"], 2, "Adults have 32 teeth.", "Anatomy"),
    ("What is the longest bone in the human body?", ["Humerus","Femur","Tibia","Fibula"], 1, "Femur is the longest bone.", "Anatomy"),
    ("What is the function of the liver?", ["Pump blood","Filter blood","Produce bile and detoxify","Produce insulin"], 2, "Liver produces bile and detoxifies substances.", "Anatomy"),
    ("What is the function of the pancreas?", ["Produce bile","Produce insulin and digestive enzymes","Filter blood","Store urine"], 1, "Pancreas produces insulin and digestive enzymes.", "Anatomy"),
    ("How many pairs of ribs do humans have?", ["10","12","14","16"], 1, "Humans have 12 pairs of ribs.", "Anatomy"),
    ("What is the smallest bone in the human body?", ["Stapes","Malleus","Incus","Cochlea"], 0, "Stapes in the ear is the smallest bone.", "Anatomy"),
    ("What is the function of the alveoli?", ["Pump blood","Gas exchange","Filter blood","Digest food"], 1, "Alveoli are where gas exchange occurs.", "Anatomy"),
    ("What is the function of the diaphragm?", ["Pump blood","Aid in breathing","Digest food","Filter blood"], 1, "Diaphragm aids in breathing.", "Anatomy"),
    ("How many vertebrae are in the human spine?", ["26","30","33","36"], 2, "Human spine has 33 vertebrae.", "Anatomy"),
    ("What is the function of the large intestine?", ["Digest proteins","Absorb water and form feces","Produce enzymes","Filter blood"], 1, "Large intestine absorbs water and forms feces.", "Anatomy"),
    ("What is the function of the small intestine?", ["Absorb water","Digest and absorb nutrients","Store food","Produce bile"], 1, "Small intestine digests and absorbs nutrients.", "Anatomy"),
    ("What is the function of the spleen?", ["Pump blood","Filter blood and store blood cells","Produce insulin","Digest food"], 1, "Spleen filters blood and stores blood cells.", "Anatomy"),
    # Nursing procedures (20)
    ("What is the first step in handwashing?", ["Apply soap","Wet hands","Dry hands","Turn off tap"], 1, "Wet hands first before applying soap.", "Nursing Procedures"),
    ("How long should you wash your hands?", ["10 seconds","20 seconds","30 seconds","1 minute"], 1, "Handwashing should last at least 20 seconds.", "Nursing Procedures"),
    ("What is the proper angle for intramuscular injection?", ["15 degrees","45 degrees","90 degrees","180 degrees"], 2, "IM injections are given at 90 degrees.", "Nursing Procedures"),
    ("What is the proper angle for subcutaneous injection?", ["15 degrees","45 degrees","90 degrees","180 degrees"], 1, "Subcutaneous injections are given at 45 degrees.", "Nursing Procedures"),
    ("What is the proper angle for intradermal injection?", ["5-15 degrees","45 degrees","90 degrees","180 degrees"], 0, "Intradermal injections are given at 5-15 degrees.", "Nursing Procedures"),
    ("What is the normal respiratory rate for adults?", ["8-12","12-20","20-30","30-40"], 1, "Normal respiratory rate is 12-20 breaths/minute.", "Nursing Procedures"),
    ("What is the first step in CPR?", ["Give rescue breaths","Check for responsiveness","Start chest compressions","Call for help"], 1, "First check if the person is responsive.", "Nursing Procedures"),
    ("What is the compression-to-breath ratio in adult CPR?", ["15:2","30:2","30:1","15:1"], 1, "Adult CPR ratio is 30 compressions to 2 breaths.", "Nursing Procedures"),
    ("How deep should chest compressions be for adults?", ["1-2 cm","2-3 cm","5-6 cm","8-10 cm"], 2, "Chest compressions should be 5-6 cm deep.", "Nursing Procedures"),
    ("What is the rate of chest compressions in CPR?", ["60-80/min","80-100/min","100-120/min","120-140/min"], 2, "Compress at 100-120 per minute.", "Nursing Procedures"),
    ("What does RICE stand for in injury treatment?", ["Rest, Ice, Compression, Elevation","Rest, Ice, Cover, Elevate","Run, Ice, Compress, Elevate","Rest, Inject, Compress, Elevate"], 0, "RICE = Rest, Ice, Compression, Elevation.", "Nursing Procedures"),
    ("What is the first step when a patient is choking?", ["Perform CPR","Perform Heimlich maneuver","Give water","Pat on back"], 1, "Heimlich maneuver for conscious choking patients.", "Nursing Procedures"),
    ("What is the correct site for checking pulse in adults?", ["Neck (carotid)","Wrist (radial)","Groin (femoral)","Foot (pedal)"], 1, "Radial pulse at the wrist is commonly checked.", "Nursing Procedures"),
    ("What is the normal urine output per hour?", ["10-20 ml","30-50 ml","60-80 ml","100-150 ml"], 1, "Normal urine output is about 30-50 ml/hour.", "Nursing Procedures"),
    ("What position is used for unconscious patients?", ["Supine","Prone","Recovery position","Sitting"], 2, "Recovery position prevents aspiration.", "Nursing Procedures"),
    ("What is the purpose of aseptic technique?", ["Speed up procedures","Prevent infection","Reduce pain","Save money"], 1, "Aseptic technique prevents infection.", "Nursing Procedures"),
    ("What is the gauge of a standard IV catheter?", ["14-16","18-20","22-24","26-28"], 1, "Standard IV catheter is 18-20 gauge.", "Nursing Procedures"),
    ("What is the first step in wound care?", ["Apply antibiotic","Assess the wound","Cover with dressing","Remove stitches"], 1, "First assess the wound.", "Nursing Procedures"),
    ("What does NPO stand for?", ["Nothing by mouth","Normal patient order","No pain observed","New patient only"], 0, "NPO = Nothing Per Os (nothing by mouth).", "Nursing Procedures"),
    ("What is the purpose of a bed bath?", ["Entertainment","Hygiene and comfort","Exercise","Medical treatment"], 1, "Bed bath maintains hygiene and comfort.", "Nursing Procedures"),
    # Pharmacology (15)
    ("What is an antibiotic used for?", ["Viral infections","Bacterial infections","Fungal infections","Cancer"], 1, "Antibiotics treat bacterial infections.", "Pharmacology"),
    ("What does analgesic mean?", ["Reduce fever","Relieve pain","Reduce inflammation","Kill bacteria"], 1, "Analgesics relieve pain.", "Pharmacology"),
    ("What is the antidote for paracetamol overdose?", ["Vitamin K","N-acetylcysteine","Atropine","Flumazenil"], 1, "N-acetylcysteine is the antidote for paracetamol overdose.", "Pharmacology"),
    ("What does antipyretic mean?", ["Reduce fever","Relieve pain","Reduce blood pressure","Kill bacteria"], 0, "Antipyretics reduce fever.", "Pharmacology"),
    ("What is insulin used for?", ["High blood pressure","Diabetes","Asthma","Infection"], 1, "Insulin is used to treat diabetes.", "Pharmacology"),
    ("What is the route of administration for sublingual medication?", ["Under the tongue","Into muscle","Into vein","On the skin"], 0, "Sublingual = under the tongue.", "Pharmacology"),
    ("What does IM stand for?", ["Internal Medicine","Intramuscular","Inhalation Method","Immediate"], 1, "IM = Intramuscular.", "Pharmacology"),
    ("What does IV stand for?", ["Internal Vein","Intravenous","In Vitro","In Vivo"], 1, "IV = Intravenous.", "Pharmacology"),
    ("What is a side effect?", ["Intended effect","Unwanted effect of medication","Allergic reaction only","Positive effect"], 1, "Side effect is an unwanted effect of medication.", "Pharmacology"),
    ("What is the therapeutic index?", ["Dose that cures","Ratio of toxic dose to effective dose","Time to effect","Cost of medicine"], 1, "Therapeutic index = toxic dose / effective dose.", "Pharmacology"),
    ("What does STAT mean in medication orders?", ["Give immediately","Give once daily","Give twice daily","Give as needed"], 0, "STAT = immediately.", "Pharmacology"),
    ("What does PRN mean?", ["Every hour","As needed","Before meals","After meals"], 1, "PRN = pro re nata (as needed).", "Pharmacology"),
    ("What does BID mean?", ["Once daily","Twice daily","Three times daily","Four times daily"], 1, "BID = bis in die (twice daily).", "Pharmacology"),
    ("What does TID mean?", ["Once daily","Twice daily","Three times daily","Four times daily"], 2, "TID = ter in die (three times daily).", "Pharmacology"),
    ("What is the five rights of medication administration?", ["Right patient, drug, dose, route, time","Right nurse, drug, patient, dose, time","Right room, drug, patient, dose, time","Right doctor, drug, patient, dose, time"], 0, "Five rights: patient, drug, dose, route, time.", "Pharmacology"),
    # Medical terminology (15)
    ("What does hypertension mean?", ["Low blood pressure","High blood pressure","Normal blood pressure","No blood pressure"], 1, "Hypertension = high blood pressure.", "Medical Terminology"),
    ("What does hypotension mean?", ["Low blood pressure","High blood pressure","Normal blood pressure","No blood pressure"], 0, "Hypotension = low blood pressure.", "Medical Terminology"),
    ("What does tachycardia mean?", ["Slow heart rate","Fast heart rate","Normal heart rate","No heart rate"], 1, "Tachycardia = fast heart rate (>100 bpm).", "Medical Terminology"),
    ("What does bradycardia mean?", ["Slow heart rate","Fast heart rate","Normal heart rate","No heart rate"], 0, "Bradycardia = slow heart rate (<60 bpm).", "Medical Terminology"),
    ("What does dyspnea mean?", ["Difficulty breathing","High blood pressure","Rapid heartbeat","Low temperature"], 0, "Dyspnea = difficulty breathing.", "Medical Terminology"),
    ("What does edema mean?", ["Fever","Swelling","Rash","Pain"], 1, "Edema = swelling due to fluid accumulation.", "Medical Terminology"),
    ("What does cyanosis mean?", ["Yellow skin","Blue skin","Red skin","Pale skin"], 1, "Cyanosis = bluish skin due to low oxygen.", "Medical Terminology"),
    ("What does jaundice mean?", ["Yellow skin","Blue skin","Red skin","Pale skin"], 0, "Jaundice = yellow skin due to bilirubin.", "Medical Terminology"),
    ("What does syncope mean?", ["Fainting","Vomiting","Coughing","Bleeding"], 0, "Syncope = fainting or temporary loss of consciousness.", "Medical Terminology"),
    ("What does hematuria mean?", ["Blood in urine","Blood in stool","Blood in vomit","Blood in sputum"], 0, "Hematuria = blood in urine.", "Medical Terminology"),
    ("What does hemoptysis mean?", ["Blood in urine","Blood in stool","Blood in vomit","Blood in sputum"], 3, "Hemoptysis = coughing up blood.", "Medical Terminology"),
    ("What does melena mean?", ["Blood in urine","Black tarry stool","Blood in vomit","Blood in sputum"], 1, "Melena = black tarry stool (digested blood).", "Medical Terminology"),
    ("What does epistaxis mean?", ["Nosebleed","Earbleed","Eyebleed","Mouthbleed"], 0, "Epistaxis = nosebleed.", "Medical Terminology"),
    ("What does pruritus mean?", ["Itching","Pain","Burning","Numbness"], 0, "Pruritus = itching.", "Medical Terminology"),
    ("What does paresthesia mean?", ["Itching","Pain","Burning","Tingling/numbness"], 3, "Paresthesia = tingling or numbness.", "Medical Terminology"),
]

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "nursing")

def build_set(questions, set_num, total_sets=7):
    shuffled = questions[:]
    random.seed(300 + set_num)
    random.shuffle(shuffled)
    start = ((set_num - 4) * 50) % len(shuffled)
    result = []
    for i in range(50):
        q, opts, corr, expl, sub = shuffled[(start + i) % len(shuffled)]
        result.append({"id": i+1, "question": q, "options": opts, "correctIndex": corr, "subject": sub, "explanation": expl})
    return result

for set_num in range(4, 11):
    en = build_set(NURSING_Q, set_num)
    ne = []
    for q in en:
        ne_q = q.copy()
        ne_q["options"] = q["options"][:]
        ne.append(ne_q)
    
    en_path = os.path.join(BASE_DIR, f"set{set_num}.json")
    ne_path = os.path.join(BASE_DIR, f"set{set_num}_ne.json")
    os.makedirs(BASE_DIR, exist_ok=True)
    
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en, f, ensure_ascii=False, indent=2)
    with open(ne_path, "w", encoding="utf-8") as f:
        json.dump(ne, f, ensure_ascii=False, indent=2)
    
    print(f"Generated nursing/set{set_num}")

print("Done generating nursing sets!")
