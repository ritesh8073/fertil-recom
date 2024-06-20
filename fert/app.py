from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_crop_nutrient_requirements(crop):
    crop_nutrient_requirements = {
        "Wheat": {"N": (20, 40), "P": (30, 50), "K": (20, 40)},
        "Rice": {"N": (30, 50), "P": (20, 40), "K": (30, 50)},
        "Corn": {"N": (40, 60), "P": (30, 50), "K": (20, 40)},
        "Barley": {"N": (10, 30), "P": (20, 40), "K": (10, 30)},
        "Soybean": {"N": (20, 40), "P": (20, 40), "K": (30, 50)},
        "Oat": {"N": (15, 30), "P": (20, 40), "K": (15, 30)},
        "Peanut": {"N": (20, 40), "P": (30, 50), "K": (30, 50)},
        "Sugarcane": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Tomato": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Potato": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Carrot": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Onion": {"N": (20, 40), "P": (30, 50), "K": (20, 40)},
        "Garlic": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Peas": {"N": (10, 30), "P": (20, 40), "K": (20, 40)},
        "Beans": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Lettuce": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Spinach": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cabbage": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Broccoli": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cauliflower": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cucumber": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Pumpkin": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Squash": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Zucchini": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Apple": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Banana": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Orange": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Grape": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Mango": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Pineapple": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Papaya": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Strawberry": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
    }
    return crop_nutrient_requirements.get(crop, None)

def suggest_fertilizer(nitrogen, phosphorus, potassium, crop):
    crop_requirements = get_crop_nutrient_requirements(crop)
    
    if not crop_requirements:
        return f"No nutrient requirements found for {crop}. Please add the crop's nutrient requirements."
    
    suggestions = []
    
    if nitrogen < crop_requirements["N"][0]:
        suggestions.append("Add nitrogen-rich fertilizer.")
    elif nitrogen > crop_requirements["N"][1]:
        suggestions.append("Reduce nitrogen application.\n")
        suggestions.append("Additional ways to reduce nitrogen content:\n")
        
        suggestions.append("- Plant nitrogen-fixing cover crops like clover, alfalfa, or soybeans.\n")
        
        suggestions.append("- Implement crop rotation with nitrogen-consuming crops like legumes.\n")
        suggestions.append("- Incorporate organic matter such as compost or manure, which can help stabilize nitrogen levels in the soil.\n")
       
        


    if phosphorus < crop_requirements["P"][0]:
        suggestions.append("Add phosphorus-rich fertilizer.")
    elif phosphorus > crop_requirements["P"][1]:
        suggestions.append("Reduce phosphorus application.")
        suggestions.append("Additional ways to reduce phosphorus content:")
        suggestions.append("- Use phytoremediation techniques by planting hyperaccumulating plants that absorb phosphorus from the soil.")
        suggestions.append("- Employ soil amendments like iron sulfate or aluminum sulfate, which can bind with phosphorus and reduce its availability to plants.")
        
        
        

    if potassium < crop_requirements["K"][0]:
        suggestions.append("Add potassium-rich fertilizer.")
    elif potassium > crop_requirements["K"][1]:
        suggestions.append("Reduce potassium application.")
        suggestions.append("Additional ways to reduce potassium content:")
        
        
        
        suggestions.append("- Use potassium-fixing plants like willow trees or certain grasses to extract excess potassium from the soil.")
        suggestions.append("- Apply soil amendments such as gypsum or calcium sulfate, which can help leach potassium from the soil profile.")
       

    if not suggestions:
        return "Your soil has optimal nutrient levels for the selected crop."
    else:
        return "\n" "\n".join(suggestions)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        crop = data.get('crop')
        nitrogen = float(data.get('nitrogen'))
        phosphorus = float(data.get('phosphorus'))
        potassium = float(data.get('potassium'))

        recommendation = suggest_fertilizer(nitrogen, phosphorus, potassium, crop)
        return jsonify({'recommendation': recommendation})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)
