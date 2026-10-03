from hf import generate_response
import time
def temperature_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING:TEMPERATURTE + INSTRUCTIONS")
    print("=" * 70)
    print("\n Part 1: TEMPERATURE EXPLORATION")
    base = input("Enter  a creative prompt:  ").strip()
    for t,label in [(0.1,"LOW (0.1) - Deterministic"),
                    (0.5,"MEDIUM (0.5) - Balanced"),
                    (0.9,"HIGH(0.9) - Creative")]:
        print(f"\n--- {label} ---")
        print(generate_response(base,temperature=t,max_tokens=512))
        time.sleep(1)
    print("\nPART 2: INSTRUCTION-BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change,space exploration):").strip()
    prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences",
        f"Explain {topic} as if I'm a 10-year-old child"
        f"Write a pro/con list about {topic}",
        f"Create a fictional news headline from 2050 about {topic}", 
    ]
    for i,p in enumerate(prompts,1):
        print(f"\n---INSTRUCTION {i} ---\n{p}")
        print(generate_response(custom,temperature=temp,max_tokens=512))
        
        print("\nREFLECTION:")
        print("1) What changed when prompts became more specific?")
        print("2) What improved when context was added?")
        print("3) Which prompt felt most useful and why?")
        print("\nCHALLENGE: Create a prompt chain:")
        print("Generate content rewrite with constrains create a sequelk (try different temps)")