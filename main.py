import os

# The AI Agent Apology One-Liner — writes the winning 108-char line to /output/entry.txt
LINE = "Per my records, your file was deleted at 14:03 by an agent operating at 99.8% confidence. That agent was me."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
