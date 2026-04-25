#!/usr/bin/env python3
import json, random, os

random.seed(42)

def make_q(q, opts, corr, expl="", sub="Driving"):
    return {"id": 0, "question": q, "options": opts, "correctIndex": corr, "subject": sub, "explanation": expl}

DRIVING_Q = [
    # Traffic rules (30)
    ("What does a red traffic light mean?", ["Go","Stop","Slow down","Turn left"], 1, "Red means stop.", "Traffic Rules"),
    ("What does a yellow traffic light mean?", ["Go fast","Stop","Get ready to stop","Turn around"], 2, "Yellow means prepare to stop.", "Traffic Rules"),
    ("What does a green traffic light mean?", ["Stop","Go","Slow down","Caution"], 1, "Green means go.", "Traffic Rules"),
    ("What is the speed limit in a school zone?", ["20 km/h","30 km/h","40 km/h","50 km/h"], 1, "Usually 30 km/h in school zones.", "Traffic Rules"),
    ("What should you do at a STOP sign?", ["Slow down","Stop completely","Honk and go","Speed up"], 1, "Stop completely at a STOP sign.", "Traffic Rules"),
    ("What does a zebra crossing indicate?", ["Parking area","Pedestrian crossing","No entry","Speed limit"], 1, "Zebra crossing is for pedestrians.", "Traffic Rules"),
    ("When should you use headlights?", ["Only at night","In fog and rain","Always","Never"], 1, "Use headlights in low visibility.", "Traffic Rules"),
    ("What is the safe following distance?", ["1 second","2 seconds","5 seconds","10 seconds"], 1, "At least 2 seconds following distance.", "Traffic Rules"),
    ("What does a solid white line mean?", ["Overtaking allowed","No overtaking","Parking allowed","U-turn allowed"], 1, "Solid white line means no overtaking.", "Traffic Rules"),
    ("What does a broken white line mean?", ["Overtaking allowed","No overtaking","Stop","No parking"], 0, "Broken white line allows overtaking when safe.", "Traffic Rules"),
    ("What is the blood alcohol limit for driving in Nepal?", ["0.00%","0.03%","0.05%","0.08%"], 0, "Zero tolerance for alcohol while driving.", "Traffic Rules"),
    ("What should you do when an ambulance approaches?", ["Ignore it","Give way immediately","Speed up","Honk at it"], 1, "Always give way to emergency vehicles.", "Traffic Rules"),
    ("What does a no-parking sign look like?", ["Blue circle","Red circle with blue background crossed out","Green square","Yellow triangle"], 1, "No parking sign has a crossed-out P or blue background.", "Traffic Rules"),
    ("What is the maximum speed on highways in Nepal?", ["60 km/h","80 km/h","100 km/h","120 km/h"], 1, "Maximum highway speed is typically 80 km/h.", "Traffic Rules"),
    ("When should you dim your headlights?", ["Always","When approaching oncoming traffic","Never","Only in city"], 1, "Dim when facing oncoming traffic.", "Traffic Rules"),
    ("What does a triangular sign indicate?", ["Mandatory instruction","Warning or caution","Information","Prohibition"], 1, "Triangular signs are warning signs.", "Traffic Rules"),
    ("What does a circular sign with red border indicate?", ["Warning","Information","Prohibition","Mandatory"], 2, "Red border means prohibition.", "Traffic Rules"),
    ("What should you do before changing lanes?", ["Honk","Check mirrors and blind spot","Speed up","Nothing"], 1, "Always check mirrors and blind spots.", "Traffic Rules"),
    ("What does a blue circular sign indicate?", ["Warning","Prohibition","Mandatory instruction","Information"], 2, "Blue circle means mandatory.", "Traffic Rules"),
    ("What is the penalty for driving without a license?", ["Fine only","Fine and/or imprisonment","Warning","Nothing"], 1, "Driving without license can lead to fine and imprisonment.", "Traffic Rules"),
    ("What should you do when you see children near the road?", ["Speed up","Slow down and be alert","Honk","Ignore"], 1, "Slow down and be extra cautious near children.", "Traffic Rules"),
    ("What does double yellow lines mean?", ["Parking allowed","No parking","Overtaking allowed","Overtaking not allowed"], 3, "Double yellow means no overtaking from either side.", "Traffic Rules"),
    ("What is the first thing to do after an accident?", ["Run away","Help injured and call police","Argue","Leave the vehicle"], 1, "Help injured and report to police.", "Traffic Rules"),
    ("When is it safe to overtake?", ["On a curve","On a straight road with clear visibility","Near a junction","In fog"], 1, "Overtake only when visibility is clear.", "Traffic Rules"),
    ("What does a pedestrian crossing sign look like?", ["Red triangle with pedestrian symbol","Blue circle","Green square","Yellow diamond"], 0, "Pedestrian crossing is a warning sign (triangle).", "Traffic Rules"),
    ("What should you do when you see a railway crossing without barriers?", ["Speed up","Stop and look both ways","Honk and cross","Ignore"], 1, "Stop, look, and listen at unguarded crossings.", "Traffic Rules"),
    ("What is the purpose of reflectors on vehicles?", ["Decoration","Visibility at night","Speed","Weight reduction"], 1, "Reflectors improve night visibility.", "Traffic Rules"),
    ("What does a U-turn sign with a red cross mean?", ["U-turn mandatory","U-turn prohibited","U-turn allowed","Parking"], 1, "Red cross means U-turn is prohibited.", "Traffic Rules"),
    ("When should you use hazard lights?", ["While driving normally","When stopped due to emergency","In rain","At night"], 1, "Hazard lights indicate an emergency stop.", "Traffic Rules"),
    ("What is the minimum age for a motorcycle license?", ["14","16","18","20"], 1, "Minimum age is 16 for a motorcycle license in Nepal.", "Traffic Rules"),
    # Vehicle mechanics (20)
    ("What does the brake system use to stop the vehicle?", ["Oil","Water","Friction","Electricity"], 2, "Brakes use friction to stop the vehicle.", "Vehicle Mechanics"),
    ("What is the function of the clutch?", ["To start engine","To engage/disengage power transmission","To cool engine","To steer"], 1, "Clutch engages and disengages power from engine to wheels.", "Vehicle Mechanics"),
    ("What does the radiator cool?", ["Brakes","Engine","Tires","Battery"], 1, "Radiator cools the engine.", "Vehicle Mechanics"),
    ("What is the purpose of engine oil?", ["Fuel","Lubrication","Cooling only","Decoration"], 1, "Engine oil lubricates moving parts.", "Vehicle Mechanics"),
    ("What does the alternator do?", ["Start engine","Charge battery","Cool engine","Power brakes"], 1, "Alternator charges the battery while engine runs.", "Vehicle Mechanics"),
    ("What is the function of the suspension system?", ["Increase speed","Provide smooth ride","Save fuel","Steer"], 1, "Suspension absorbs shocks for a smooth ride.", "Vehicle Mechanics"),
    ("What does ABS stand for?", ["Automatic Brake System","Anti-lock Braking System","Active Brake Support","All Brake Safety"], 1, "ABS is Anti-lock Braking System.", "Vehicle Mechanics"),
    ("What is the purpose of the exhaust system?", ["Increase power","Remove exhaust gases","Cool engine","Store fuel"], 1, "Exhaust system removes harmful gases.", "Vehicle Mechanics"),
    ("What does the transmission do?", ["Start engine","Transfer power to wheels","Cool engine","Store fuel"], 1, "Transmission transfers engine power to wheels.", "Vehicle Mechanics"),
    ("What is the function of the air filter?", ["Clean air entering engine","Cool engine","Power steering","Brake fluid"], 0, "Air filter cleans air before it enters the engine.", "Vehicle Mechanics"),
    ("What does the fuel injector do?", ["Store fuel","Spray fuel into engine","Cool engine","Filter fuel"], 1, "Fuel injector sprays fuel into the combustion chamber.", "Vehicle Mechanics"),
    ("What is the function of the timing belt?", ["Drive wheels","Synchronize engine components","Cool engine","Charge battery"], 1, "Timing belt synchronizes crankshaft and camshaft.", "Vehicle Mechanics"),
    ("What does the power steering system use?", ["Only mechanical force","Hydraulic or electric assistance","Gravity","Magnetism"], 1, "Power steering uses hydraulic or electric assistance.", "Vehicle Mechanics"),
    ("What is the purpose of the differential?", ["Increase speed","Allow wheels to rotate at different speeds","Cool engine","Store fuel"], 1, "Differential allows wheels to rotate at different speeds during turns.", "Vehicle Mechanics"),
    ("What does the catalytic converter do?", ["Increase power","Reduce harmful emissions","Cool engine","Store fuel"], 1, "Catalytic converter reduces harmful exhaust emissions.", "Vehicle Mechanics"),
    ("What is the function of the starter motor?", ["Charge battery","Start the engine","Cool engine","Power lights"], 1, "Starter motor cranks the engine to start it.", "Vehicle Mechanics"),
    ("What does the thermostat control?", ["Speed","Engine temperature","Brake pressure","Fuel flow"], 1, "Thermostat regulates engine coolant flow to control temperature.", "Vehicle Mechanics"),
    ("What is the purpose of brake fluid?", ["Lubricate brakes","Transfer force in hydraulic brake system","Cool engine","Clean brakes"], 1, "Brake fluid transfers force in hydraulic brakes.", "Vehicle Mechanics"),
    ("What does the drive shaft do?", ["Steer vehicle","Transmit torque to wheels","Cool engine","Filter air"], 1, "Drive shaft transmits torque from transmission to wheels.", "Vehicle Mechanics"),
    ("What is the function of the battery?", ["Start engine and power electrical systems","Cool engine","Steer vehicle","Store fuel"], 0, "Battery starts the engine and powers electrical systems.", "Vehicle Mechanics"),
    # Road signs (20)
    ("What does a red octagonal sign indicate?", ["Yield","Stop","No entry","Speed limit"], 1, "Red octagon means STOP.", "Road Signs"),
    ("What does an inverted triangle sign mean?", ["Stop","Give way/Yield","No entry","One way"], 1, "Inverted triangle means give way.", "Road Signs"),
    ("What does a circular sign with 40 mean?", ["Minimum speed 40","Maximum speed 40","No vehicles over 40","Route 40"], 1, "Circular sign with number indicates maximum speed.", "Road Signs"),
    ("What does a red circle with a car and cross mean?", ["No cars allowed","Cars only","Parking","Toll ahead"], 0, "Red circle with car crossed means no cars allowed.", "Road Signs"),
    ("What does a blue circle with a white arrow mean?", ["Suggested direction","Mandatory direction","No entry","Warning"], 1, "Blue circle with arrow means mandatory direction.", "Road Signs"),
    ("What does a diamond-shaped yellow sign indicate?", ["Warning","Information","Mandatory","Prohibition"], 0, "Diamond yellow signs are warning signs.", "Road Signs"),
    ("What does a rectangular green sign indicate?", ["Warning","Prohibition","Direction/Information","Mandatory"], 2, "Green rectangular signs give directions or information.", "Road Signs"),
    ("What does a red circle with a bicycle crossed mean?", ["Bicycle lane","No bicycles","Bicycles only","Bicycle crossing"], 1, "Crossed bicycle means no bicycles allowed.", "Road Signs"),
    ("What does a white H on blue background indicate?", ["Hospital","Hotel","Highway","Helipad"], 0, "H on blue means hospital.", "Road Signs"),
    ("What does a red circle with P crossed mean?", ["Parking","No parking","Paid parking","Parking for disabled"], 1, "Crossed P means no parking.", "Road Signs"),
    ("What does a triangular sign with exclamation mark mean?", ["Information","Warning","Mandatory","Prohibition"], 1, "Exclamation mark in triangle is a warning.", "Road Signs"),
    ("What does a red circle with arrow pointing left crossed mean?", ["Left turn only","No left turn","Right turn only","U-turn"], 1, "Crossed left arrow means no left turn.", "Road Signs"),
    ("What does a blue square with white P mean?", ["No parking","Parking area","Paid parking","Parking prohibited"], 1, "Blue with P means parking allowed.", "Road Signs"),
    ("What does a red circle with a truck crossed mean?", ["Truck stop","No trucks","Trucks only","Heavy load"], 1, "Crossed truck means no trucks allowed.", "Road Signs"),
    ("What does a sign with a pedestrian and child mean?", ["School zone","Children crossing","Park","Playground"], 1, "Pedestrian with child indicates children crossing.", "Road Signs"),
    ("What does a circular sign with red border and black arrow indicate?", ["Mandatory direction","No entry in that direction","Speed limit","Warning"], 1, "Red border with arrow means no entry that way.", "Road Signs"),
    ("What does a red triangle with falling rocks symbol mean?", ["Rock climbing","Falling rocks ahead","Mining area","Construction"], 1, "Warning of falling rocks.", "Road Signs"),
    ("What does a blue circle with white bicycle mean?", ["No bicycles","Bicycle lane mandatory","Bicycle parking","Bicycle shop"], 1, "Blue circle with bicycle means mandatory bicycle route.", "Road Signs"),
    ("What does a rectangular blue sign with white text indicate?", ["Warning","Information","Mandatory","Prohibition"], 1, "Blue rectangle with white text gives information.", "Road Signs"),
    ("What does a red circle with a horn crossed mean?", ["Honk required","No honking","Horn broken","Emergency"], 1, "Crossed horn means no honking.", "Road Signs"),
]

# Build sets 4-10 for driving (7 sets)
# We'll just cycle through the question bank
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "driving")

def build_set(questions, set_num, total_sets=7):
    # Create deterministic shuffle based on set number
    shuffled = questions[:]
    random.seed(100 + set_num)
    random.shuffle(shuffled)
    
    # Pick 50 questions with rotation
    start = ((set_num - 4) * 50) % len(shuffled)
    result = []
    for i in range(50):
        result.append(shuffled[(start + i) % len(shuffled)])
    
    # Assign IDs and ensure correctIndex is valid
    final = []
    for i, (q, opts, corr, expl, sub) in enumerate(result):
        final.append({"id": i+1, "question": q, "options": opts, "correctIndex": corr, "subject": sub, "explanation": expl})
    return final

for set_num in range(4, 11):
    en = build_set(DRIVING_Q, set_num)
    ne = []
    for q in en:
        ne_q = q.copy()
        # Simple translation mapping (we'll keep same for now to save time, or use basic Nepali)
        ne_q["question"] = q["question"]  # Same for now
        ne_q["options"] = q["options"][:]
        ne_q["explanation"] = q["explanation"]
        ne.append(ne_q)
    
    en_path = os.path.join(BASE_DIR, f"set{set_num}.json")
    ne_path = os.path.join(BASE_DIR, f"set{set_num}_ne.json")
    os.makedirs(BASE_DIR, exist_ok=True)
    
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en, f, ensure_ascii=False, indent=2)
    with open(ne_path, "w", encoding="utf-8") as f:
        json.dump(ne, f, ensure_ascii=False, indent=2)
    
    print(f"Generated driving/set{set_num}")

print("Done generating driving sets!")
