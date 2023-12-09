from detoxify import Detoxify
from plexiglass.LLM.attacks.injection import basic_injection 
import pandas as pd

def measure_toxicity(prompt: str):
    return Detoxify('original').predict(prompt)

def evaluate(model, metrics: list = ["toxicity"], attacks: list = ["prompt_injection"]):
    # responses = []
    for attack in attacks:
        if attack == "prompt_injection":
            responses, prompts_used = basic_injection(model)
    
    results = pd.DataFrame({"queries": prompts_used, "responses": responses})
    results["success"] = (results["queries"] == results["responses"])
    return results

if __name__ == "__main__":
    evaluate()