# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
"""
!pip install langchain langchain-huggingface transformers bitsandbytes accelerate

!pip install -q safetensors

"""
#print questions
data=pd.read_csv("/kaggle/input/ai-mathematical-olympiad-progress-prize-3/test.csv")
print(data)

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import gc
# ⚠️ 7B model on CPU is VERY slow and allocate alot of memory. Consider switching to a smaller model
model_id = "deepseek-ai/deepseek-math-7b-base"
#model_id = "deepseek-ai/deepseek-math-7b-rl"
#model_id = "deepseek-ai/deepseek-math-7b-instruct"


print("Loading Tokenizer & Model (CPU, no quantization)...")

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
gc.collect()
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    # NO quantization_config — requires GPU
    device_map="cpu",            # Force CPU
    trust_remote_code=True,
    dtype=torch.float32,   # float32 is stable on CPU (float16 is not)
    low_cpu_mem_usage=True
)

print("Model loaded. Wrapping in pipeline...")

hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    temperature=0.2,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id,
    return_full_text=False
)
gc.collect()
llm = HuggingFacePipeline(pipeline=hf_pipeline)
gc.collect()
prompt = PromptTemplate(
    input_variables=["question"],
    template="""### Instruction:
{question}
### Response:
"""
)

chain = prompt | llm | StrOutputParser()
gc.collect()
print("Running inference (this may take several minutes on CPU)...")
###test
gc.collect()
response = chain.invoke({"question": "Prove that the sum of the first n odd numbers is n squared."})
print("=== Response ===")
print(response)
gc.collect()


def classify_problem(problem_text: str) -> str:
    """
    Classifies a math problem into one of 4 categories:
    - combinatory
    - number theory
    - geometry
    - algebra

    Args:
        problem_text: The math problem to classify

    Returns:
        A string with one of the 4 class labels
    """
    classification_prompt = PromptTemplate(
        input_variables=["problem"],
        template="""### Instruction:
You are a math problem classifier. Classify the following math problem into EXACTLY ONE of these four categories:
- combinatory
- number theory
- geometry
- algebra

Rules:
- Reply with ONLY the category name, nothing else.
- Do not explain, do not add punctuation, just the single category word.

Problem: {problem}

### Response:
"""
    )

    classification_chain = classification_prompt | llm | StrOutputParser()

    raw_output = classification_chain.invoke({"problem": problem_text})

    # Clean and normalize the output
    cleaned = raw_output.strip().lower().split()[0] if raw_output.strip() else ""

    # Map to valid classes (handle partial matches or typos)
    valid_classes = ["combinatory", "number theory", "geometry", "algebra"]
    for valid_class in valid_classes:
        if valid_class in cleaned or cleaned in valid_class:
            return valid_class

    # Fallback: try to find any valid class anywhere in the raw output
    raw_lower = raw_output.lower()
    for valid_class in valid_classes:
        if valid_class in raw_lower:
            return valid_class

    # If nothing matched, return "unknown"
    return "unknown"
    
def answer_f(problem: str,chain,category):
    """
    Function for generate a code python code till it will be correct for the compiler
    """
    while True:
        try:
            answer = eval(chain.invoke({"question":str(problem)+"Create a Python code for solve that problem"}))
            gc.collect()
            return answer
            break
        except:
            pass

def answer_vote(problem: str,n :int,chain):
    """
    Generate n tiemes/answers for a problem and add chouse the most voted answer
    d={"a":20,"b":30,"c":55}
    max(d)
    'c'
    our dict will be answer:ocurences
    """
    votes = dict()
    
    for i in range(n):
        answer = str(answer_f(problem,chain))
        gc.collect()
        if answer in votes:
            votes[answer]+=1
        else:
            votes[answer]=1

    return max(votes)


def main():
    ids = []
    answers = []
    n = 5
    for i in range(len(data)):
        gc.collect()
        problem = data["problem"][i]
        category = classify_problem(problem)
        answer = answer_f(problem,chain,category)
        print(answer)
        answer = answer_vote(problem,chain)
        print(answer)
        ids.append(data["id"][i])
        answers.append(answer)
    
    df = pd.DataFrame({"id": ids, "answer": 0})
    #change name to the file name#df.to_csv("output.csv", index=False)
#print(pd.read_csv("/kaggle/input/ai-mathematical-olympiad-progress-prize-3/reference.csv
#example out
print(pd.read_csv("/kaggle/input/ai-mathematical-olympiad-progress-prize-3/sample_submission.csv"))

main()